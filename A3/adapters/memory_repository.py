import csv
import os
from bisect import bisect_left, insort_left
from typing import List

from A3.adapters.repository import AbstractRepository
from A3.domainmodel.movie import Movie


class MemoryRepository(AbstractRepository):
    # Articles ordered by date, not id. id is assumed unique.

    def __init__(self):
        self._articles = list()
        self._articles_index = dict()
        self._tags = list()
        self._users = list()
        self._comments = list()

    def add_article(self, article: Movie):
        insort_left(self._articles, article)
        self._articles_index[article.rank] = article

    def get_article(self, id: int) -> Movie:
        article = None

        try:
            article = self._articles_index[id]
        except KeyError:
            pass  # Ignore exception and return None.

        return article

    def get_movies_by_rank(self, target_date) -> List[Movie]:
        matching_articles = list()
        try:
            # index = self.article_index(target_article)
            for article in self._articles:
                if int(article.rank) == int(target_date):
                    matching_articles.append(article)
        except ValueError:
            # No articles for specified date. Simply return an empty list.
            pass
        return matching_articles
        # will always return one article

    def get_number_of_articles(self):
        return len(self._articles)

    def get_first_article(self):
        article = None

        if len(self._articles) > 0:
            article = self._articles[0]
        return article

    def get_last_article(self):
        article = None

        if len(self._articles) > 0:
            article = self._articles[-1]
        return article

    def get_date_of_previous_article(self, article: Movie):
        previous_date = None

        try:
            index = self.article_index(article)
            for stored_article in reversed(self._articles[0:index]):
                if stored_article.rank < article.rank:
                    previous_date = stored_article.rank
                    break
        except ValueError:
            # No earlier articles, so return None.
            pass
        #print(previous_date)
        return previous_date

    def get_date_of_next_article(self, article: Movie):
        next_date = None

        try:
            index = self.article_index(article)
            for stored_article in self._articles[index + 1:len(self._articles)]:
                if stored_article.rank > article.rank:
                    next_date = stored_article.rank
                    break
        except ValueError:
            # No subsequent articles, so return None.
            pass

        return next_date

    # Helper method to return article index.
    def article_index(self, article: Movie):
        index = bisect_left(self._articles, article)
        return index


def read_csv_file(filename: str):
    with open(filename, encoding='utf-8-sig') as infile:
        reader = csv.reader(infile)

        # Read first line of the the CSV file.
        headers = next(reader)

        # Read remaining rows from the CSV file.
        for row in reader:
            # Strip any leading/trailing white space from data read.
            row = [item.strip() for item in row]
            yield row


def load_articles_and_tags(data_path: str, repo: MemoryRepository):
    for data_row in read_csv_file(os.path.join(data_path, 'Data1000Movies.csv')):
        article = Movie(
            movie_title=data_row[1],
            movie_year=int(data_row[6]),
            rank=int(data_row[0])
        )
        # Add the Article to the repository.
        repo.add_article(article)

    # Create Tag objects, associate them with Articles and add them to the repository.


def populate(data_path: str, repo: MemoryRepository):
    # Load articles and tags into the repository.
    load_articles_and_tags(data_path, repo)
