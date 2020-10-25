import abc
from typing import List
from datetime import date

from A3.domainmodel.movie import Movie


repo_instance = None


class RepositoryException(Exception):

    def __init__(self, message=None):
        pass


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add_article(self, article: Movie):
        """ Adds an Article to the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_movies_by_rank(self, target_date: date) -> List[Movie]:
        """ Returns a list of Articles that were published on target_date.

        If there are no Articles on the given date, this method returns an empty list.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_number_of_articles(self):
        """ Returns the number of Articles in the repository. """
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_article(self) -> Movie:
        """ Returns the first Article, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_last_article(self) -> Movie:
        """ Returns the last Article, ordered by date, from the repository.

        Returns None if the repository is empty.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_date_of_previous_article(self, article: Movie):
        """ Returns the date of an Article that immediately precedes article.

        If article is the first Article in the repository, this method returns None because there are no Articles
        on a previous date.
        """
        raise NotImplementedError

    @abc.abstractmethod
    def get_date_of_next_article(self, article: Movie):
        """ Returns the date of an Article that immediately follows article.

        If article is the last Article in the repository, this method returns None because there are no Articles
        on a later date.
        """
        raise NotImplementedError








