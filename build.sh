#!/usr/bin/env bash
docker build -t rmq-h .
docker run -v /etc/hostname:/srv/hostname -v /tmp:/tmp rmq-h:latest bash
