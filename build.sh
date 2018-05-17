#!/usr/bin/env bash
docker build -t rmq-h .
docker run -d rmq-h:latest
