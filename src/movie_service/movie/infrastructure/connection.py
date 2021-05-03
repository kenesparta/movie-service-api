import psycopg2
import config


class Connection:
    def __init__(self):
        self.conn = None
        self.cursor = None
        self.__config = config.DATABASE
        self.__connect()

    def __connect(self):
        try:
            self.conn = psycopg2.connect(user=self.__config['USER'],
                                         password=self.__config['PASS'],
                                         host=self.__config['HOST'],
                                         port=self.__config['PORT'],
                                         database=self.__config['DATABASE'])
            self.cursor = self.conn.cursor()
        except (Exception, psycopg2.Error) as error:
            print(error)
            # send the "error" message to a logger system]
            self.conn = None
