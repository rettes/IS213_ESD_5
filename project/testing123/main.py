from __future__ import print_function
import httplib2
import os
import auth

from apiclient import discovery
from oauth2client import client
from oauth2client import tools
from oauth2client.file import Storage

from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS


app = Flask(__name__)
db = SQLAlchemy(app)
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
    info = request.get_json()
    print(info)
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


    sendInst = send_email.send_email(service)
    message = sendInst.create_message_with_attachment('esdproject2@gmail.com','weixiang9655@gmail.com','Done','Hi there, This is a test from Python!', 'image.jpg' )
    sendInst.send_message('me',message)

if __name__ == '__main__':
    app.run(port=5010, debug=True)