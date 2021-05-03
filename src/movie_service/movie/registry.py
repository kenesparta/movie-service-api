import abc


class MovieRegistry(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def fetch(self, id_movie: str) -> object:
        pass

    @abc.abstractmethod
    def fetch_all(self) -> list:
        pass

    @abc.abstractmethod
    def save(self, movies: list) -> int:
        pass
