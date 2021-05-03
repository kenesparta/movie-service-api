import pika
import config


class RabbitMq:
    def __init__(self):
        self.conn = None
        self.channel = None
        self.__queue_declare = None
        self.message = '[]'
        self.__message_count = 0
        self.__config = config.RABBITMQ
        self.__connect()

    def __connect(self):
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.__config['HOST']
            )
        )
        self.channel = self.conn.channel()
        self.__queue_declare = self.channel.queue_declare(queue=self.__config['QUEUE'])
        self.__message_count = self.__queue_declare.method.message_count

    def get_message(self):
        if not self.__message_count:
            return
        for method_frame, _, body in self.channel.consume(queue=self.__config['QUEUE']):
            self.message = body
            self.channel.basic_ack(method_frame.delivery_tag)
            if method_frame.delivery_tag == 1 or self.__message_count == 0:
                break
        self.channel.close()
        self.conn.close()
