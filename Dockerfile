FROM python:2.7
ENV PYTHONUNBUFFERED 1
RUN mkdir /dataset
WORKDIR /dataset
ADD requirements.txt /dataset/
RUN pip install -r requirements.txt
ADD . /dataset/