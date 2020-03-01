from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS



# initiate Flask
app = Flask(__name__) 
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+mysqlconnector://root@localhost:3306/appointment_service'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)
class Appointment(db.Model):
    __tablename__ = 'gentlemen_appointment'
 
    appointmentID = db.Column(db.Integer, primary_key=True)
    gentlemenID = db.Column(db.Integer, nullable=False)
    username = db.Column(db.String(128), nullable=False)
    timeslot = db.Column(db.DateTime, nullable=False)
    payment_status = db.Column(db.String(128), nullable=False)
 
    def __init__(self, appointmentID, gentlemenID, username, timeslot, payment_status):
        self.appointmentID = appointmentID
        self.gentlemenID = gentlemenID
        self.username = username
        self.timeslot = timeslot
        self.payment_status = payment_status
    def json(self):
        return {"appointmentID": self.appointmentID, "gentlemenID": self.gentlemenID, "username": self.username, "timeslot": self.timeslot, "payment_status": self.payment_status}


#(GET, POST, DELETE, PUT)
#get is a query, post is to create, delete and put is to update
#@app.route("/") will return a default route if you don't specify any routes at all 
@app.route("/appointment")
def get_all():
    return jsonify({"appointments": [gentlemen_appointment.json() for gentlemen_appointment in Appointment.query.all()]})

@app.route("/appointment/<int:appointmentID>")
def find_by_appointmentID(appointmentID):
    gentlemen_appointment = Appointment.query.filter_by(appointmentID=appointmentID).first()
    if gentlemen_appointment:
        return jsonify(gentlemen_appointment.json())
    return jsonify({"message": "Appointment not found."}), 404

 
@app.route("/appointment", methods=['POST'])
def create_appointment():
    data = request.get_json()
    appointmentID = data['appointmentID']
    if (Appointment.query.filter_by(appointmentID=appointmentID).first()):
        return jsonify({"message": "An appointment with appointmentID '{}' already exists.".format(appointmentID)}), 400
    
    appointment = Appointment(**data)

    try:
        db.session.add(appointment)
        db.session.commit()
    except Exception as e:
        print(appointment)
        print(e)
        return jsonify({"message": "An error occurred creating the appointment."}), 500

    return jsonify(appointment.json()), 201

# if you import book.py in some other files, the __name__ will not be main therefore disallowing the program to run
if __name__ == "__main__":
    app.run(port=5003 , debug=True)