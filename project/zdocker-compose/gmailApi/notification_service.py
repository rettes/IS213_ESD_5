from __future__ import print_function
import httplib2
import os
import auth


from datetime import datetime

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import json
import requests


app = Flask(__name__)
CORS(app)

def get_labels():
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])

@app.route("/notification", methods=['POST'])
def send_email():
    #appointment data send over through http invocation
    info = request.get_json()
    print(info)
    messageToCustomer = ""
    check = 0
    totalPrice = 0
    for item in info:
        check += 1
    #getting name and email from client to email to them.
        accountURL = "http://accountservice:5004/account/" + str(item['customerID'])
        r= requests.get(accountURL)
        result = r.text
        customerData = json.loads(result)['Account']

        #getting name and email from tutor to email to them.
        tutorURL = "http://tutorservice:5001/tutor/" + str(item['tutorID'])
        r = requests.get(tutorURL)
        result = r.text
        tutorData = json.loads(result)['tutor'][0]

        try:
            import argparse
            flags = argparse.ArgumentParser(parents=[tools.argparser]).parse_args()
        except ImportError:
            flags = None
        
        import send_email
        SCOPES = 'https://mail.google.com/'
        CLIENT_SECRET_FILE = 'client_secret.json'
        APPLICATION_NAME = 'Gmail API Python Quickstart'
        authInst = auth.auth(SCOPES,CLIENT_SECRET_FILE,APPLICATION_NAME)
        credentials = authInst.get_credentials()

        http = credentials.authorize(httplib2.Http())
        service = discovery.build('gmail', 'v1', http=http)
        customer_name = customerData['name'].upper()
        tutor_name = tutorData["name"].upper()
        if(check == 1):
            messageToCustomer = "Hi " + customer_name +  ", this is a automated confirmation email from TutorLab. "
        date = datetime.strptime(str(item['timeslot']), '%Y-%m-%d %H:%M:%S').strftime('%B %d %Y %H:%M')
        statement2 = "Hi " + tutor_name + ", this is a confirmation email from TutorLab. \nA customer named " + customerData['name'].upper() + " has hired your services for " + tutorData['subject'] + " at the " + tutorData['level'] +" level. \nPlease take note in your working calender.\nThe date and time for the meetup is at " + str(date) +" PM" +".\nPlease come 10 minutes early to avoid being late for the appointment. Much thanks from TutorLabs."
        sendInst = send_email.send_email(service)
        message2 = sendInst.create_message_with_attachment('esdproject2@gmail.com',tutorData['tutor_email'],'Done',statement2, 'image.png' )
        sendInst.send_message('me',message2)
        totalPrice += item['price']
        statement = "\n\nYou have hired "+ tutorData['name'].upper() + ".\nYou have paid $" + str(item['price']) + " for this session." + "\nYou have hired his/her services for " + tutorData['subject'] + " at the " + tutorData['level'] +" level. \nPlease take note in your working calender.\nThe date and time for the meetup is at " + str(date) + " PM" + "."
        messageToCustomer += statement
        print(messageToCustomer)
        if(check == len(info)):
            messageToCustomer +="\n\nPlease come 10 minutes early to avoid being late for the appointment.\n\n" + "Total price paid " + str(totalPrice) + ".\nMuch thanks from TutorLabs!"
            message = sendInst.create_message_with_attachment('esdproject2@gmail.com',customerData['customer_email'],'Done',messageToCustomer, 'image.png' )
            sendInst.send_message('me',message)



    return jsonify({"message": "Email success"}), 201

if __name__ == '__main__':
    app.run(host ='0.0.0.0' , port=5010, debug=True)