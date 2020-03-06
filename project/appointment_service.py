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
    __tablename__ = 'appointments'
 
    appointmentID = db.Column(db.Integer, primary_key=True)
    tutorID = db.Column(db.Integer, nullable=False)
    customerID = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(128), nullable=False)
    level = db.Column(db.String(128), nullable=False)
    timeslot = db.Column(db.DateTime, nullable=False)
 
    def __init__(self, appointmentID, tutorID, customerID, subject, level, timeslot):
        self.appointmentID = appointmentID
        self.tutorID = tutorID
        self.customerID = customerID
        self.subject = subject
        self.level = level
        self.timeslot = timeslot
    
    def json(self):
        return {"appointmentID": self.appointmentID, "tutorID": self.tutorID, "customerID": self.customerID, "subject": self.subject, "level": self.level, "timeslot": self.timeslot}


#(GET, POST, DELETE, PUT)
#get is a query, post is to create, delete and put is to update
#@app.route("/") will return a default route if you don't specify any routes at all 
@app.route("/appointment")
def get_all():
    return jsonify({"appointments": [appointments.json() for appointments in Appointment.query.all()]})

@app.route("/appointment/<int:appointmentID>")
def find_by_appointmentID(appointmentID):
    appointments = Appointment.query.filter_by(appointmentID=appointmentID).first()
    if appointments:
        return jsonify(appointments.json())
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

# Testing Data:

# {
#     "appointmentID" : "1",
#     "tutorID" : "123",
#     "customerID" : "2424"
#     "subject" : "python",
#     "level" : "primary",
#     "timeslot" : "2020-01-01 00:59"
# }

# Comments:
# - deleting/rescheduling of appointment? 