FROM python:3.8

WORKDIR /home/app

COPY requirements.txt ./

RUN pip install -r requirements.txt

COPY . ./

RUN groupadd -r flask && useradd --no-log-init -r -g flask flask
USER flask

CMD python app.py
