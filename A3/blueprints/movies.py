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
    target_rank = request.args.get('rank')

    first_movie = services.get_first_movie(repo.repo_instance)
    last_movie = services.get_last_movie(repo.repo_instance)

    if target_rank is None:
        target_rank = first_movie.get('rank')
    else:
        target_rank = target_rank

    movies, previous_rank, next_rank = services.get_movies_by_rank(target_rank, repo.repo_instance)
    first_movie_url = None
    last_movie_url = None
    next_movie_url = None
    prev_movie_url = None

    if len(movies) > 0:
        if previous_rank is not None:
            prev_movie_url = url_for('movie_bp.movies_by_rank', rank=previous_rank)
            first_movie_url = url_for('movie_bp.movies_by_rank', rank=first_movie['rank'])

        if next_rank is not None:
            next_movie_url = url_for('movie_bp.movies_by_rank', rank=next_rank)
            last_movie_url = url_for('movie_bp.movies_by_rank', rank=last_movie['rank'])

        return render_template(
            'movies/movies.html',
            movies=movies,
            first_movie_url=first_movie_url,
            last_movie_url=last_movie_url,
            prev_movie_url=prev_movie_url,
            next_movie_url=next_movie_url
        )

    return redirect(url_for('home_bp.home'))


