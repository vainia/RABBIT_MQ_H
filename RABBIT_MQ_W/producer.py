import pika, logging, sys, argparse
from argparse import RawTextHelpFormatter
from time import sleep
import sys
sys.path.append("./..")
from settings import *

if __name__ == '__main__':
    examples = sys.argv[0] + " -p 5672 -s rabbitmq -m 'Hello' "
    parser = argparse.ArgumentParser(formatter_class=RawTextHelpFormatter,
                                 description='Run producer.py',
                                 epilog=examples)
    parser.add_argument('-p', '--port', action='store', dest='port', help='The port to listen on.', required=False, default=SET['port'])
    parser.add_argument('-s', '--server', action='store', dest='server', help='The RabbitMQ server.', required=False, default=SET['server'])
    parser.add_argument('-m', '--message', action='store', dest='message', help='The message to send', required=False, default='Hello, World!')
    parser.add_argument('-r', '--repeat', action='store', dest='repeat', help='Number of times to repeat the message', required=False, default='1')

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
    parameters = pika.ConnectionParameters(args.server,
                                           int(args.port),
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    channel = connection.channel()
    q = channel.queue_declare('L-to-W')
    q_name = q.method.queue

    # Turn on delivery confirmations
    channel.confirm_delivery()

    for i in range(0, int(args.repeat)):
        if channel.basic_publish(exchange='', routing_key=q_name, body=args.message):
            LOG.info('Message has been delivered')
        else:
            LOG.warning('Message NOT delivered')

        sleep(2)

    connection.close()
