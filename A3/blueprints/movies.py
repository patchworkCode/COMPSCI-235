from flask import Blueprint
from flask import request, render_template, redirect, url_for, session


import A3.adapters.repository as repo
import A3.utilities.utilities as utilities
import A3.utilities.services as services

# Configure Blueprint.
movie_blueprint = Blueprint(
    'movie_bp', __name__)


@movie_blueprint.route('/movies_by_rank', methods=['GET'])
def movies_by_rank():
    '''

    Change for correct load

    '''
    target_date = request.args.get('date')


    # Fetch the first and last articles in the series.
    #------

    first_article = services.get_first_article(repo.repo_instance)
    last_article = services.get_last_article(repo.repo_instance)

    if target_date is None:
        # No date query parameter, so return articles from day 1 of the series.
        target_date = first_article.get('rank')
    else:
        # Convert target_date from string to date.
        target_date = target_date

    # Fetch article(s) for the target date. This call also returns the previous and next dates for articles immediately
    # before and after the target date.

    articles, previous_date, next_date = services.get_movies_by_rank(target_date, repo.repo_instance)
    first_article_url = None
    last_article_url = None
    next_article_url = None
    prev_article_url = None

    if len(articles) > 0:
        # There's at least one article for the target date.
        if previous_date is not None:
            # There are articles on a previous date, so generate URLs for the 'previous' and 'first' navigation buttons.
            prev_article_url = url_for('movie_bp.movies_by_rank', date=previous_date)
            first_article_url = url_for('movie_bp.movies_by_rank', date=first_article['rank'])

        # There are articles on a subsequent date, so generate URLs for the 'next' and 'last' navigation buttons.
        if next_date is not None:
            next_article_url = url_for('movie_bp.movies_by_rank', date=next_date)
            last_article_url = url_for('movie_bp.movies_by_rank', date=last_article['rank'])

        # Construct urls for viewing article comments and adding comments.
        """
        for article in articles:
            article['view_comment_url'] = url_for('movie_bp.movies_by_rank', date=target_date, view_comments_for=article['rank'])
            article['add_comment_url'] = url_for('movie_bp.comment_on_article', article=article['rank'])
        """

        # Generate the webpage to display the articles.
        return render_template(
            'news/articles.html',
            title='Articles',
            articles_title=articles,
            articles=articles,
            first_article_url=first_article_url,
            last_article_url=last_article_url,
            prev_article_url=prev_article_url,
            next_article_url=next_article_url
        )

    # No articles to show, so return the homepage.
    return redirect(url_for('home_bp.home'))


