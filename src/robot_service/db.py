from connection import Connection

from psycopg2.extras import execute_values


class MovieRegistryPostgre:
    def __init__(self):
        self.__connection = Connection()
        self.__cursor = self.__connection.conn.cursor()
        self.__conn = self.__connection.conn

    def __close(self):
        self.__cursor.close()
        self.__conn.close()

    def update(self, movie_ids: list) -> int:
        """
        Update with a random rating
        :param movie_ids:
        :return:
        """
        try:
            tuple_movies = tuple([(m_id,) for m_id in movie_ids])
            if not tuple_movies:
                return 0
            self.__cursor.execute("UPDATE movie SET rate=random()*100 WHERE id IN %s AND rate=0.0", (tuple_movies,))
            self.__conn.commit()
            return self.__cursor.rowcount
        except Exception as error:
            print(error)
            # send the "error" message to a logger system
            return 0
        finally:
            if self.__connection.conn:
                self.__close()

    def fetch(self) -> list:
        """
        Fetch five random movies to update the rating
        :return:
        """
        movies = []
        try:
            self.__cursor.execute("SELECT id FROM movie WHERE rate = 0.0 ORDER BY random() LIMIT 5")
            self.__conn.commit()
            for row in self.__cursor.fetchall():
                movies.append(row[0])
            print(movies)
            return movies
        except Exception as error:
            print(error)
            # send the "error" message to a logger system
            return []
        finally:
            if self.__connection.conn:
                self.__close()

    def best(self, positions=5) -> list:
        movies = []
        try:
            self.__cursor.execute("SELECT * FROM movie order by rate DESC, title ASC limit %s", str(positions))
            self.__conn.commit()
            for row in self.__cursor.fetchall():
                movies.append(
                    {
                        'id': row[0],
                        'title': row[1],
                        'year': row[2],
                        'rate': float(row[3]),
                    }
                )
            return movies
        except Exception as error:
            print(error)
            # send the "error" message to a logger system
            return []
        finally:
            if self.__connection.conn:
                self.__close()
