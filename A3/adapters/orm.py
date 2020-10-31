from sqlalchemy import (
    Table, MetaData, Column, Integer, String, Date, DateTime,
    ForeignKey
)
from sqlalchemy.orm import mapper, relationship

from A3.domainmodel.movie import Movie

#model.Article = Movie

metadata = MetaData()

#Rank,Title,Genre,Description,Director,Actors,Year,Runtime (Minutes),Rating,Votes,Revenue (Millions),Metascore
#1,Guardians of the Galaxy,"Action,Adventure,Sci-Fi",A group of intergalactic criminals are forced to work together to stop a fanatical warrior from taking control of the universe.,James Gunn,"Chris Pratt, Vin Diesel, Bradley Cooper, Zoe Saldana",2014,121,8.1,757074,333.13,76


movies = Table(
    'movies', metadata,
    Column('rank', Integer, primary_key=True, autoincrement=True),
    Column('title', String(1050), nullable=True),
    Column('genre', String(255), nullable=True),
    Column('description', String(1050), nullable=True),
    Column('director', String(255), nullable=True),
    Column('actors', String(255), nullable=True),
    Column('year', Integer, nullable=True),
    Column('runtime', Integer, nullable=True),
    Column('rating', String(255), nullable=True),
    Column('votes', Integer, nullable=True),
    Column('revenue', String(255), nullable=True),
    Column('metascore', Integer, nullable=True),

    #rank, title, genre, description, director, actors, year, runtime, rating, votes, revenue, metascore
)


def map_model_to_tables():

    mapper(Movie, movies, properties={
        '_rank': movies.c.rank,
        'movie_title': movies.c.title,
        '_genre': movies.c.genre,
        '_description': movies.c.description,
        '_director': movies.c.director,
        '_actors': movies.c.actors,
        'movie_year': movies.c.year,
        '_runtime': movies.c.runtime,
        '_rating': movies.c.rating,
        '_votes': movies.c.votes,
        '_revenue': movies.c.revenue,
        '_metascore': movies.c.metascore,
    })

