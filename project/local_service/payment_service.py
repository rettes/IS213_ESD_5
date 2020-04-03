from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ



import pika
import json
import requests
from datetime import datetime


 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/payment_service'
#app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('payment_serviceURL')
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

def send_order(payment):
    hostname = "host.docker.internal" # default broker hostname. Web management interface default at http://localhost:15672
    port = 5672 # default messaging port.
    # connect to the broker and set up a communication channel in the connection
    connection = pika.BlockingConnection(pika.ConnectionParameters(host=hostname ,port=port))
        # Note: various network firewalls, filters, gateways (e.g., SMU VPN on wifi), may hinder the connections;
        # If "pika.exceptions.AMQPConnectionError" happens, may try again after disconnecting the wifi and/or disabling firewalls
    channel = connection.channel()

    # set up the exchange if the exchange doesn't exist
    exchangename="payment_fanout"
    channel.exchange_declare(exchange=exchangename, exchange_type='fanout')

    # prepare the message body content
    message = json.dumps(payment, default=str) # convert a JSON object to a string

    channel.basic_publish(exchange=exchangename, routing_key="", body=message)
    print("Order sent to Appointment.")
    # close the connection to the broker
    connection.close()

@app.route("/payments/<int:customerID>")
def make_payment(customerID):
    #info = request.get_json()
    #print(info)
    #customerID = info["customerID"]
    cartserviceURL = "http://cartservice:5006/cart/" + str(customerID)
    r= requests.get(cartserviceURL)
    cartData = json.loads(r.text)["Cart"]
    
    # return data
    # cartData = data["Cart"]
    for item in cartData:
        item['payment_date'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        print(item)
        payment = Payment(**item) 
        try:
            db.session.add(payment)
            db.session.commit()
        except Exception as e:
            print(e)
            print(info)
            return jsonify({"message": "An error occurred during payment."}), 500
    send_order(cartData)
    print("Completed notification")


    return jsonify({"message": "Payment success"}), 201



if __name__ == '__main__':
    app.run(port=5005, debug=True)


