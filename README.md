# Overview

API
MOTIVATION
HOW IT WORKS
LINK TO ARCHI

# Requirements

* `pika==0.11.2` (because we need sometimes to feed our python with small rodents)

Pika has used for supplying pure-Python implementation of the AMQP 0-9-1 protocol including RabbitMQ’s extensions. That module gives us ability to perform any manipulations with RabbitMQ.

# Installation

All commands will be perform in terminal (`docker` must be installed).

First of all you need to raise up RabbitMQ server with command:

```ShellSession
docker run -d --hostname my-rabbit -p 0.0.0.0:5672:5672 -p 0.0.0.0:15672:15672  --name some-rabbit -e RABBITMQ_DEFAULT_USER=user_name -e RABBITMQ_DEFAULT_PASS=user_password rabbitmq:3-management
```

Ports ASMP:`5672` and HTTP:`15672` are defaults for backend(functional) and frontend(web) accordingly.
`0.0.0.0` means that RabbitMQ will listen for all hosts.

# Setup

File [config.py](https://github.com/vainia/RABBIT_MQ_H/blob/master/config.py) maintain configurations for micro-service(hereinafter "MS"):

```
SET = {
    'port':'5672', #default port
    'server':'0.0.0.0', #rabbit-mq server ip adres
    'name':'user_name', #name required for connection to server
    'passwd':'user_password', #password required for connection to server
    'queue_current':'RMQ-H-E', #name of the current queue, where initial JSON being preserved
    'queue_above':'RMQ-E-L' #name of the next queue, where JSON sends after processing
}
```

Everything above(excluding `queue` set and `server` ip) must be exactly the same as defined in command raising RabbitMQ server.

# Usage

* For launch up whole project (ensure that you have cloned all MSs and being in parent folder which contains them folders) execute next line:
```ShellSession
for i in */; do cd $i; ./build.sh; cd .. ;done
```

* If you want to run single MS just run [build.sh](https://github.com/vainia/RABBIT_MQ_H/blob/master/build.sh) placed in primary folder titled with MS name.
