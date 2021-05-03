import pika
import config


class RabbitMq:
    def __init__(self):
        self.conn = None
        self.channel = None
        self.__config = config.RABBITMQ
        self.__connect()

    def __connect(self):
        self.conn = pika.BlockingConnection(
            pika.ConnectionParameters(
                host=self.__config['HOST']
            )
        )
        self.channel = self.conn.channel()
        self.channel.queue_declare(queue=self.__config['QUEUE'])

    def send_message(self, message: str):
        self.channel.basic_publish(
            exchange='',
            routing_key=self.__config['QUEUE'],
            body=message,
            properties=pika.BasicProperties(
                delivery_mode=2,
            )
        )
        self.conn.close()
