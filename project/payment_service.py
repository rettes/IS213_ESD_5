from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

# import datetime
# datetime_object = datetime.datetime.now()
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/payment_service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

class Payment(db.Model):
    __tablename__ = 'payment_record'

    appointmentID = db.Column(db.Integer, primary_key=True)
    tutorID = db.Column(db.Integer, nullable=False)
    customerID = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(64), nullable=False)
    level = db.Column(db.String(64), nullable=False)
    timeslot = db.Column(db.DateTime, nullable=False)
    price = db.Column(db.Float, nullable=False)
    payment_date = db.Column(db.DateTime, nullable=False)

    def init(self, appointmentID, tutorID, customerID, subject, level, timeslot, price, payment_date):
        self.appointmentID = appointmentID
        self.tutorID = tutorID
        self.customerID = customerID
        self.subject = subject
        self.level = level
        self.timeslot = timeslot
        self.price = price
        self.payment_date = payment_date

    def json(self):
        return {"appointmentID": self.appointmentID, "tutorID": self.tutorID, "customerID": self.customerID, "subject": self.subject, "level": self.level, "timeslot": self.timeslot, "price": self.price, "payment_date": self.payment_date}

@app.route("/payments")
def get_all():
  return jsonify({"Payment Records": [payment_record.json() for payment_record in Payment.query.all()]})
 
@app.route("/payments_aid/<int:appointmentID>")
def find_by_paymentID(appointmentID):
    payment = Payment.query.filter_by(appointmentID=appointmentID).first()
    if payment:
        return jsonify(payment.json())
    return jsonify({"message": "Payment not found."}), 404

@app.route("/payments_cid/<int:customerID>")
def find_by_customerid(customerID):
    payment = Payment.query.filter_by(customerID=customerID).first()
    if payment:
        return jsonify(payment.json())
    return jsonify({"message": "Payment not found."}), 404

@app.route("/payments", methods=['POST'])
def make_payment():
    info = request.get_json()
    # appointmentID = info["appointmentID"]
    # if (Payment.query.filter_by(appointmentID=appointmentID).first()):
    #     return jsonify({"message": "A transaction with appointment ID '{}' already exists.".format(appointmentID)}), 400
    print(info)
    data = Payment(**info) 

    try:
        db.session.add(data)
        db.session.commit()
    except Exception as e:
        print(e)
        print(info)
        return jsonify({"message": "An error occurred during payment."}), 500

    return jsonify(data.json()), 201

# @app.route("/payments", methods=['PUT'])
# def update_payment():
#     info = request.get_json()
#     appointmentID = info["appointmentID"]
#     status = info["payment_status"]

#     try:
#         data = Payment.query.filter_by(appointmentID=appointmentID).update(dict(payment_status=status))
#         db.session.commit()
#         data = Payment.query.filter_by(appointmentID=appointmentID).first()
#     except Exception as e:
#         print(e)
#         print(info)
#         return jsonify({"message": "An error occurred during payment."}), 500

#     return jsonify(data.json()), 201

if __name__ == '__main__':
    app.run(port=5005, debug=True)


# Comments:
# - Datetime is not intuitive enough
# - How does the .first() function work. If i search by username and there is more than 1 record. How?

# {
#     "tutorID" : "123",
#     "customerID" : "2424"
#     "subject" : "python",
#     "level" : "primary",
#     "timeslot" : "2020-01-01 00:59"
#     "price" : "24.24",
#     "payment_date" : "2019-03-03 12:12:12",
# }

# admin = User.query.filter_by(username='admin').update(dict(email='my_new_email@example.com')))
# db.session.commit()

# admin = User.query.filter_by(username='admin').first()
# admin.email = 'my_new_email@example.com'
# db.session.commit()

# user = User.query.get(5)
# user.name = 'New Name'
# db.session.commit()