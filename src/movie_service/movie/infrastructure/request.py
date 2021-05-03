from http import HTTPStatus
import requests

from movie.registry import MovieRegistry


class Request:
    __DATA_KEY = 'Search'
    __HEADERS = {
        'Accept': 'application/json'
    }

    def __init__(self, api_key: str, url: str, movie_registry: MovieRegistry):
        self.__api_key = api_key
        self.__url = url
        self.__movies = []
        self.__movie_registry = movie_registry

    def __save(self) -> int:
        return self.__movie_registry.save(self.__movies)

    def import_movie(self, variables: dict) -> dict:
        response = requests.get(
            self.__url,
            params=variables,
            headers=self.__HEADERS
        )
        if response.status_code == HTTPStatus.OK:
            self.__filter_movies(response.json())
            return {
                "response": True,
                "rows_inserted": self.__save()
            }
        return {
            "response": False,
            "rows_inserted": 0
        }

    def __filter_movies(self, result: dict):
        """
        Transform the movies to a list of tuples that can be inserted on DB
        :param result:
        """
        if self.__DATA_KEY in result:
            for movie in result[self.__DATA_KEY]:
                self.__movies.append(
                    (
                        movie['imdbID'],
                        movie['Title'],
                        movie['Year']
                    )
                )
        print(self.__movies)
