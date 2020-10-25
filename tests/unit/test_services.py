from datetime import date

import pytest


from A3.utilities import services as news_services

from A3.utilities.services import NonExistentArticleException

def test_get_first_article(in_memory_repo):
    article_as_dict = news_services.get_first_article(in_memory_repo)

    assert article_as_dict['rank'] == 1


def test_get_last_article(in_memory_repo):
    article_as_dict = news_services.get_last_article(in_memory_repo)

    assert article_as_dict['rank'] == 6


def test_get_movies_by_rank_with_one_rank(in_memory_repo):
    target_date = 1

    articles_as_dict, prev_date, next_date = news_services.get_movies_by_rank(target_date, in_memory_repo)
    assert len(articles_as_dict) == 1
    assert articles_as_dict[0]['rank'] == 1

    assert prev_date is None
    assert next_date == 2

def test_get_articles_by_date_with_non_existent_date(in_memory_repo):
    target_date = 20

    articles_as_dict, prev_date, next_date = news_services.get_movies_by_rank(target_date, in_memory_repo)

    # Check that there are no articles dated 2020-03-06.
    assert len(articles_as_dict) == 0



