import sys

import pika
from pika.credentials import PlainCredentials
from pika import SSLOptions
from ssl import SSLContext, PROTOCOL_TLS


def main():

    user = "<USERNAME>"
    passwd = "<PASSWORD>"
    host = "<HOST>"
    port = "<PORT>"
    vhost = "<VHOST>"
    queue_name = "<QUEUENAME>"

    creds = PlainCredentials(username=user, password=passwd, erase_on_connect=True)

    ssl = SSLOptions(SSLContext(protocol=PROTOCOL_TLS), host)

    connection = pika.BlockingConnection(
        pika.ConnectionParameters(
            host=host,
            port=port,
            credentials=creds,
            ssl_options=ssl,
            virtual_host=vhost,
        )
    )

    channel = connection.channel()

    channel.queue_declare(queue=queue_name)

    def callback(ch, method, properties, body):
        print(f" [x] Received {body}")

    channel.basic_consume(queue=queue_name, auto_ack=False, on_message_callback=callback)

    print(" [*] Waiting for messages. To exit press CTRL+C")
    channel.start_consuming()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("Interrupted")
        try:
            sys.exit(0)
        except SystemExit:
            sys.exit(0)
