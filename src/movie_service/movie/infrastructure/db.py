from movie.registry import MovieRegistry
from movie.infrastructure.connection import Connection
from psycopg2.extras import execute_values


class MovieRegistryPostgre(MovieRegistry):
    def __init__(self):
        self.__connection = Connection()
        self.__cursor = self.__connection.conn.cursor()
        self.__conn = self.__connection.conn

    def fetch(self, id_movie: str) -> object:
        pass

    def fetch_all(self) -> list:
        pass

    def save(self, movies: list) -> int:
        try:
            execute_values(
                self.__cursor,
                """ INSERT INTO movie (id, title, year) VALUES %s ON CONFLICT DO NOTHING""",
                movies
            )
            self.__conn.commit()
            return self.__cursor.rowcount
        except Exception as error:
            print(error)
            # send the "error" message to a logger system
            return 0
        finally:
            if self.__connection.conn:
                self.__cursor.close()
                self.__conn.close()
