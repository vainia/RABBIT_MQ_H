FROM ubuntu:latest
LABEL maintainer="Ivan Napolskykh"
RUN apt-get update -y && apt-get install -y python3-pip python3-dev build-essential && rm -rfv /var/cache
RUN mkdir /RMQ_TEST
COPY ./requirements.txt /RMQ_TEST
WORKDIR /RMQ_TEST
RUN pip3 install --no-cache-dir -r requirements.txt
COPY ./*.py /RMQ_TEST/
# RUN for f in RABBIT_MQ_*; do mv "$f" "./RMQ_TEST/$f"; done
COPY ./RABBIT_MQ_H /RMQ_TEST/RABBIT_MQ_H
CMD ["python3", "main.py"]
