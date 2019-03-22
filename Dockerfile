FROM python:3.7.2-slim

ENV PYTHONUNBUFFERED 1

RUN mkdir -p /app/dataset

WORKDIR /app/dataset

RUN pip install --upgrade pip

ADD requirements.txt /app/dataset/

RUN pip install -r requirements.txt

ADD . /app/dataset/
