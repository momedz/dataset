FROM python:2.7-slim
ENV PYTHONUNBUFFERED 1
RUN mkdir /datasetcontroller
WORKDIR /datasetcontroller
ADD requirements.txt /datasetcontroller/
RUN pip install -r requirements.txt
ADD . /datasetcontroller/
