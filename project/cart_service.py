from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import json
import requests
from datetime import datetime



# initiate Flask
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/cart_service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)
class Addtocart(db.Model):
    __tablename__ = 'cart'
 
    tutorID = db.Column(db.Integer, primary_key=True)
    customerID = db.Column(db.Integer, primary_key=True)
    subject = db.Column(db.String(128), nullable=False)
    level = db.Column(db.String(128), nullable=False)
    timeslot = db.Column(db.DateTime, primary_key=True)
    price = db.Column(db.Float, nullable=False)
 
    def __init__(self, tutorID, customerID, subject, level, timeslot, price):
        
        self.tutorID = tutorID
        self.customerID = customerID
        self.subject = subject
        self.level = level
        self.timeslot = timeslot
        self.price = price

    def json(self):
        return {"tutorID": self.tutorID, "customerID": self.customerID, "subject": self.subject, "level": self.level, "timeslot": self.timeslot, "price": self.price}


#(GET, POST, DELETE, PUT)
#get is a query, post is to create, delete and put is to update
#@app.route("/") will return a default route if you don't specify any routes at all 
@app.route("/cart/<int:customerID>")
def get_all(customerID):
    try:
        print("hello")
        ID = int(customerID)
        cart_details = Addtocart.query.filter_by(customerID=ID).all()
        if cart_details:
            cart = jsonify({"Cart": [cart_details.json() for cart_details in cart_details]})
            cart = cart.get_json(force=False, silent=False, cache=True)['Cart']
            print (cart)
            for item in cart:
                year = str(datetime.strptime(cart['timeslot'][5:25],"%d %b %Y %H:%M:%S").year)
                month = str(datetime.strptime(cart['timeslot'][5:25],"%d %b %Y %H:%M:%S").month)
                day = str(datetime.strptime(cart['timeslot'][5:25],"%d %b %Y %H:%M:%S").day)
                hour = str(datetime.strptime(cart['timeslot'][5:25],"%d %b %Y %H:%M:%S").hour)
                minutes = str(datetime.strptime(cart['timeslot'][5:25],"%d %b %Y %H:%M:%S").minute)
                seconds = str(datetime.strptime(cart['timeslot'][5:25],"%d %b %Y %H:%M:%S").second)
                date = year +  "-" + month + "-" + day + " "+ hour + ":"+ minutes + ":"+ seconds
                cart['timeslot'] = date
            print(cart)
            
            return cart
            
            

    except Exception as e:
        print(cart_details)
        print (e)
        return jsonify({"message": "Cart not found."}), 404

 
@app.route("/cart", methods=['POST'])
def add_to_cart():
    data = request.get_json()
    customerID = data['customerID']
    timeslot = data['timeslot']

    if (Addtocart.query.filter_by(customerID=customerID).filter_by(timeslot=timeslot).first()):
        selection = Addtocart(**data)

        try:
            db.session.delete(Addtocart.query.filter_by(customerID=customerID).filter_by(timeslot=timeslot).first())
            db.session.commit()
            db.session.add(selection)
            db.session.commit()
        except Exception as e:
            print(selection)
            print(e)
            return jsonify({"message": "An error occurred creating the selection."}), 500

        return jsonify(selection.json()), 201
    
    selection = Addtocart(**data)

    try:
        db.session.add(selection)
        db.session.commit()
    except Exception as e:
        print(selection)
        print(e)
        return jsonify({"message": "An error occurred creating the selection."}), 500

    return jsonify(selection.json()), 201



# if you import book.py in some other files, the __name__ will not be main therefore disallowing the program to run
if __name__ == "__main__":
    app.run(port=5006 , debug=True)


# Comments:

# - Have issue retrieving customer's cart details with customerID
# - How do we update the selection in our cart?
# - primary key consists of 3 variables, how do we filer them?

# Testing Data:

# {
#     "tutorID" : "001",
#     "customerID" : "123",
#     "subject" : "ESD",
#     "level" : "university",
#     "timeslot" : "2019-03-03 12:12:12",
#     "price" : "24"
# }