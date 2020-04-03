FROM python:3
WORKDIR /usr/src/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY ./tutor_service.py .
CMD [ "python", "./tutor_service.py" ]

