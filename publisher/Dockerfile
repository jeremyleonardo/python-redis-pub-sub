FROM python:3.8

WORKDIR /home/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

EXPOSE 5000

RUN groupadd -r flask && useradd --no-log-init -r -g flask flask
USER flask

ENV FLASK_APP app.py
CMD flask run --host=0.0.0.0
