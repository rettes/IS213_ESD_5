FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./notification_queue.py .

CMD [ "python", "./notification_queue.py" ]

