FROM python:3.11.4-slim-buster

WORKDIR /usr/src/app
ENV FLASK_APP=app

COPY ./requirements.txt ./

RUN pip install --upgrade pip \
    && pip install -r requirements.txt
