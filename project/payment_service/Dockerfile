FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install docker-py -U
COPY ./payment_service.py .



CMD [ "python", "./payment_service.py" ]

