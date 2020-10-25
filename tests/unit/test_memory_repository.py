from datetime import date

from A3.domainmodel.movie import Movie
from A3.adapters.repository import RepositoryException


def test_repository_can_retrieve_article_count(in_memory_repo):
    number_of_articles = in_memory_repo.get_number_of_articles()

    # Check that the query returned 6 Articles.
    assert number_of_articles == 6


def test_repository_can_add_article(in_memory_repo):
    test = Movie(
        7,
        "cool_movie",
        2016
    )
    in_memory_repo.add_article(test)

    assert in_memory_repo.get_article(7) is test


def test_repository_can_retrieve_article(in_memory_repo):
    article = in_memory_repo.get_article(1)

    # Check that the Article has the expected title.
    assert article.movie_title == 'Guardians of the Galaxy'


def test_repository_does_not_retrieve_a_non_existent_article(in_memory_repo):
    article = in_memory_repo.get_article(101)
    assert article is None


def test_repository_can_get_movies_by_rank(in_memory_repo):
    articles = in_memory_repo.get_movies_by_rank(3)

    # Check that the query returned 3 Articles.
    assert len(articles) == 1


def test_repository_does_not_retrieve_a_movie_when_there_are_no_movies_for_a_given_rank(in_memory_repo):
    articles = in_memory_repo.get_movies_by_rank(1001)
    assert len(articles) == 0


def test_repository_can_get_first_article(in_memory_repo):
    article = in_memory_repo.get_first_article()
    assert article.movie_title == 'Guardians of the Galaxy'


def test_repository_can_get_last_article(in_memory_repo):
    article = in_memory_repo.get_last_article()
    assert article.movie_title == 'The Great Wall'


def test_repository_returns_date_of_previous_article(in_memory_repo):
    article = in_memory_repo.get_article(6)
    previous_date = in_memory_repo.get_date_of_previous_article(article)

    assert previous_date == 5


def test_repository_returns_none_when_there_are_no_previous_articles(in_memory_repo):
    article = in_memory_repo.get_article(1)
    previous_date = in_memory_repo.get_date_of_previous_article(article)

    assert previous_date is None


def test_repository_returns_date_of_next_article(in_memory_repo):
    article = in_memory_repo.get_article(3)
    next_date = in_memory_repo.get_date_of_next_article(article)

    assert next_date == 4


def test_repository_returns_none_when_there_are_no_subsequent_articles(in_memory_repo):
    article = in_memory_repo.get_article(6)
    next_date = in_memory_repo.get_date_of_next_article(article)

    assert next_date is None





