FROM ubuntu:latest
LABEL maintainer="Ivan Napolskykh"
RUN apt-get update -y && apt-get install -y vim python3-pip python3-dev build-essential && rm -rfv /var/cache
RUN mkdir /RMQ_H
COPY ./requirements.txt /RMQ_H
WORKDIR /RMQ_H
RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./*.py /RMQ_H/
CMD ["python3", "main.py"]
