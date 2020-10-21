from flask import Blueprint, render_template, url_for
from flask_wtf import FlaskForm
from wtforms import IntegerField, SubmitField
from wtforms.validators import DataRequired

#import people_web_app.adapters.repository as repo

movie_blueprint = Blueprint('movie_bp', __name__)


@movie_blueprint.route('/', methods=['GET'])
def home():
    return render_template('home.html')


@movie_blueprint.route('/movies', methods=['GET'])
def movies():
    return render_template('list_movies.html')