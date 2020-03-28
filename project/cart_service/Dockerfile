FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./cart_service.py .
CMD [ "python", "./cart_service.py" ]

