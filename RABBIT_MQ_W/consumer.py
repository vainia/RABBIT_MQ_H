import pika, logging, sys, argparse, os
from argparse import RawTextHelpFormatter
from time import sleep
import sys
sys.path.append("..")
from settings import *
import time

def on_message(channel, method_frame, header_frame, body):
    #print(method_frame.delivery_tag)
    str=body.decode("utf-8").replace('!','?',1)
    #print(str)
    log=time.ctime()+' '+str+'\n'
    with open('log.log', 'a') as the_file:
        the_file.write(log)

    #print(LOG.info('Message has been received %s', body))
    #channel.basic_ack(delivery_tag=method_frame.delivery_tag)


if __name__ == '__main__':
    examples = sys.argv[0] + " -p 5672 -s rabbitmq "
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                 description='Run consumer.py',
                                 epilog=examples)
    parser.add_argument('-p', '--port', action='store', dest='port', help='The port to listen on.', required=False, default=SET['port'])
    parser.add_argument('-s', '--server', action='store', dest='server', help='The RabbitMQ server.', required=False, default=SET['server'])

    args = parser.parse_args()
    if args.port == None:
        print("Missing required argument: -p/--port")
        sys.exit(1)
    if args.server == None:
        print("Missing required argument: -s/--server")
        sys.exit(1)

    logging.basicConfig(level=logging.INFO)
    LOG = logging.getLogger(__name__)
    credentials = pika.PlainCredentials(SET['name'], SET['passwd'])
    parameters = pika.ConnectionParameters(args.server, int(args.port), '/', credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()

    channel.queue_declare('L-to-W')
    channel.basic_consume(on_message, 'L-to-W')

    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        channel.stop_consuming()
    connection.close()
