from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

import pika
import json
import requests

def receiveNotificationUpdate():
    print("Notification service is working right now.")
    hostname = "localhost"
    port = 5672
    connection = pika.BlockingConnection(pika.ConnectionParameters(host = hostname , port= port))
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
    notificationURL = "http://localhost:5010/notification"
    print("Reaching notification")
    r= requests.post(notificationURL, json = json.loads(body))
    print("success")


if __name__ == "__main__":
    receiveNotificationUpdate()
    print("checking if appointment works as an external service;")