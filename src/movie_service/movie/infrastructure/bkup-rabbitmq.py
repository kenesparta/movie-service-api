import time

import pika
import config


class RabbitMq:
    def __init__(self):
        self.conn = None
        self.channel = None
        self.message = ''
        self.__config = config.RABBITMQ
        self.__connect()

    def __connect(self):
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.__config['HOST']
            )
        )
        print('-----before1')
        self.channel = self.conn.channel()
        print('-----before2')
        self.channel.queue_declare(queue=self.__config['QUEUE'])

    def get_message(self):
        # print(g)
        self.channel.basic_qos(prefetch_count=1)
        try:
            print('-----consume1')
            self.channel.basic_consume(queue=self.__config['QUEUE'], on_message_callback=self.__callback)
            print('-----consume2')
            # self.conn.close()
            self.channel.start_consuming()
        except Exception:
            self.channel.stop_consuming()
        finally:
            self.channel.close()
            self.conn.close()

    def __callback(self, channel, method, _, body):
        print("Received %r" % body.decode())
        print(body.count(b'.'))
        self.message = body.decode()
        time.sleep(1)
        # print(" [x] Done")
        channel.basic_ack(delivery_tag=method.delivery_tag)
        # self.channel.close()
        # self.conn.close()
