from typing import Iterable
import random


from typing import Iterable

from A3.adapters.repository import AbstractRepository
from A3.domainmodel.movie import Movie


# ============================================
# Functions to convert dicts to model entities
# ============================================


""" 
useful one
"""

class NonExistentArticleException(Exception):
    pass


class UnknownUserException(Exception):
    pass


def get_article(article_id: int, repo: AbstractRepository):
    article = repo.get_article(article_id)

    if article is None:
        raise NonExistentArticleException

    return article_to_dict(article)


def get_first_article(repo: AbstractRepository):

    article = repo.get_first_article()

    return article_to_dict(article)


def get_last_article(repo: AbstractRepository):

    article = repo.get_last_article()
    return article_to_dict(article)


def get_movies_by_rank(rank, repo: AbstractRepository):
    # Returns articles for the target date (empty if no matches), the date of the previous article (might be null), the date of the next article (might be null)
    articles = repo.get_movies_by_rank(target_date=rank)

    articles_dto = list()
    prev_date = next_date = None

    if len(articles) > 0:
        prev_date = repo.get_date_of_previous_article(articles[0])
        next_date = repo.get_date_of_next_article(articles[0])

        # Convert Articles to dictionary form.
        articles_dto = articles_to_dict(articles)

    return articles_dto, prev_date, next_date


# ============================================
# Functions to convert model entities to dicts
# ============================================

def article_to_dict(article: Movie):
    article_dict = {
        'title': article.movie_title,
        'year': article.movie_year,
        'rank': article.rank
    }
    return article_dict


def articles_to_dict(articles: Iterable[Movie]):
    return [article_to_dict(article) for article in articles]

# ============================================
# Functions to convert dicts to model entities
# ============================================

def dict_to_article(dict):
    article = Movie(dict.title, dict.year, dict.rank)
    # Note there's no comments or tags.
    return article

