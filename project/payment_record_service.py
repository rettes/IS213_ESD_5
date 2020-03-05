from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# import datetime
# datetime_object = datetime.datetime.now()
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/payment_record_service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

class Payment(db.Model):
    __tablename__ = 'payment_record'

    paymentID = db.Column(db.Integer, primary_key=True)
    appointmentID = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(64), nullable=False)
    payment_status = db.Column(db.String(64), nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)

    def init(self, paymentID, appointmentID, username, payment_status, payment_date, price):
        self.paymentID = paymentID
        self.appointmentID = appointmentID
        self.username = username
        self.payment_status = payment_status
        self.payment_date = payment_date
        self.price = price

    def json(self):
        return {"paymentID": self.paymentID, "appointmentID": self.appointmentID, "username": self.username, "payment_status": self.payment_status, "payment_date": self.payment_date, "price": self.price}

@app.route("/payments")
def get_all():
  return jsonify({"Payment Records": [payment_record.json() for payment_record in Payment.query.all()]})
 
@app.route("/payments_pid/<string:paymentID>")
def find_by_paymentID(paymentID):
    payment = Payment.query.filter_by(paymentID=paymentID).first()
    if payment:
        return jsonify(payment.json())
    return jsonify({"message": "Payment not found."}), 404

@app.route("/payments_user/<string:username>")
def find_by_username(username):
    payment = Payment.query.filter_by(username=username).first()
    if payment:
        return jsonify(payment.json())
    return jsonify({"message": "Payment not found."}), 404

@app.route("/payments", methods=['POST'])
def make_payment():
    info = request.get_json()
    appointmentID = info["appointmentID"]
    if (Payment.query.filter_by(appointmentID=appointmentID).first()):
        return jsonify({"message": "A transaction with appointment ID '{}' already exists.".format(appointmentID)}), 400
 
    data = Payment(**info)

    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)
        print(info)
        return jsonify({"message": "An error occurred during payment."}), 500

    return jsonify(data.json()), 201

@app.route("/payments", methods=['PUT'])
def update_payment():
    info = request.get_json()
    appointmentID = info["appointmentID"]
    status = info["payment_status"]

    try:
        data = Payment.query.filter_by(appointmentID=appointmentID).update(dict(payment_status=status))
        db.session.commit()
        data = Payment.query.filter_by(appointmentID=appointmentID).first()
    except Exception as e:
        print(e)
        print(info)
        return jsonify({"message": "An error occurred during payment."}), 500

    return jsonify(data.json()), 201

if __name__ == '__main__':
    app.run(port=5005, debug=True)


# Comments:
# - Datetime is not intuitive enough
# - How does the .first() function work. If i search by username and there is more than 1 record. How?

# {
#     "appointmentID" : "123",
#     "username" : "joey_xoxo",
#     "payment_status" : "unpaid",
#     "payment_date" : "2019-03-03 12:12:12",
#     "price" : "24.24"
# }

# admin = User.query.filter_by(username='admin').update(dict(email='my_new_email@example.com')))
# db.session.commit()

# admin = User.query.filter_by(username='admin').first()
# admin.email = 'my_new_email@example.com'
# db.session.commit()

# user = User.query.get(5)
# user.name = 'New Name'
# db.session.commit()