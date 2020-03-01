from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/customer_service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

class Account(db.Model):
    tablename = 'account'

    username = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), nullable=False)
    password = db.Column(db.String(64), nullable=False)
    customer_email = db.Column(db.String(64), nullable=False)
    dob = db.Column(db.Date(), nullable=False)

    def init(self, username, name, password, customer_email, dob):
        self.username = username
        self.name = name
        self.password = password
        self.customer_email = customer_email
        self.dob = dob

    def json(self):
        return {"username": self.username, "name": self.name, "password": self.password, "customer_email": self.customer_email, "dob": self.dob}

@app.route("/account")
def get_all():
  return jsonify({"Account": [account.json() for account in Account.query.all()]})
 
@app.route("/account/<string:username>")
def find_by_username(username):
    account = Account.query.filter_by(username=username).first()
    if account:
        return jsonify(account.json())
    return jsonify({"message": "Account not found."}), 404

@app.route("/account", methods=['POST'])
def create_account():
    info = request.get_json()
    username = info["username"]
    if (Account.query.filter_by(username=username).first()):
        return jsonify({"message": "An account with username '{}' already exists.".format(username)}), 400
 
    data = Account(**info)

    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)
        print(info)
        return jsonify({"message": "An error occurred creating the account."}), 500

    return jsonify(data.json()), 201

if __name__ == '__main__':
    app.run(port=5004, debug=True)