from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from os import environ
 
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = environ.get('tutor_serviceURL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
 
db = SQLAlchemy(app)
CORS(app)

class Tutor(db.Model):
    __tablename__ = 'tutor'
    tutorID  = db.Column(db.Integer, primary_key=True)
    tutor_email  = db.Column(db.String(128), nullable=False)
    name = db.Column(db.String(128), nullable=False)
    sex = db.Column(db.String(128), nullable=False)
    age = db.Column(db.Integer, nullable=False)
    subject = db.Column(db.String(128), nullable=False)
    level = db.Column(db.String(128), nullable=False)
    experience = db.Column(db.Integer, nullable=False)
    about = db.Column(db.String(1000), nullable=False)
    rates = db.Column(db.Integer, nullable=False)

    def init(tutorID, tutor_email, name, sex, age, subject, level, experience, about, rates):
        self.tutorID = tutorID
        self.tutor_email = tutor_email
        self.name = name
        self.sex = sex
        self.age = age
        self.subject = subject
        self.level = level
        self.experience = experience
        self.about = about
        self.rates = rates


    def json(self):
        return {"tutorID": self.tutorID, "tutor_email": self.tutor_email, "name": self.name, "sex": self.sex, "age": self.age, "subject": self.subject, "level": self.level, "experience": self.experience,"about": self.about, "rates": self.rates}

@app.route("/tutor")
def get_all():
    return jsonify({"tutor": [tutor.json() for tutor in Tutor.query.all()]})

@app.route("/tutor/<string:tutorID>")
def find_by_tutorID(tutorID):
    tutor = Tutor.query.filter_by(tutorID=tutorID).all()
    if tutor:
        return jsonify({"tutor": [tutor.json() for tutor in tutor]})
    return jsonify({"message": "Tutor not found."}), 404


# @app.route("/tutor/<string:sex>")
# def find_by_sex(sex):
#     tutor = Tutor.query.filter_by(sex=sex).all()
#     if tutor:
#         return jsonify({"tutor": [tutor.json() for tutor in tutor]})
#     return jsonify({"message": "Tutor not found."}), 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001, debug=True)