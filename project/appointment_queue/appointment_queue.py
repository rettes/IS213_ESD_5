from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import pika
import json
import requests

def receiveAppointmentUpdate():
    print("testing")
    hostname = "host.docker.internal"
    port = 5672
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname, port= port))
    channel = connection.channel()

    exchangename = "payment_fanout"
    channel.exchange_declare(exchange=exchangename, exchange_type ="fanout")
    channelqueue = channel.queue_declare(queue="", exclusive=True)
    queue_name = channelqueue.method.queue
    channel.queue_bind(exchange=exchangename, queue=queue_name, routing_key="")

    channel.basic_consume(queue=queue_name, on_message_callback=callback, auto_ack=True)
    channel.start_consuming()

def callback(channel,method, properties, body):
    print("Receive from payment.")
    appointmentServiceURL = "http://appointmentservice:5003/appointment"
    r= requests.post(appointmentServiceURL, json = json.loads(body))
    print("success")


if __name__ == "__main__":
    receiveAppointmentUpdate()
    print("checking if appointment works as an external service;")