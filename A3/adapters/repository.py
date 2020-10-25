import abc
from typing import List

from A3.domainmodel.movie import Movie


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_movie(self, movie: Movie):
        """ Adds an movie to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_rank(self, target_rank) -> List[Movie]:
        """ Returns a list of movies that were published on target_rank.

        If there are no movies on the given rank, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_movies(self):
        """ Returns the number of movies in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_movie(self) -> Movie:
        """ Returns the first movie, ordered by rank, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_movie(self) -> Movie:
        """ Returns the last movie, ordered by rank, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_rank_of_previous_movie(self, movie: Movie):
        """ Returns the rank of an movie that immediately precedes movie.

        If movie is the first movie in the repository, this method returns None because there are no movies
        on a previous rank.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_rank_of_next_movie(self, movie: Movie):
        """ Returns the rank of an movie that immediately follows movie.

        If movie is the last movie in the repository, this method returns None because there are no movies
        on a later rank.
        """
        raise NotImplementedError








