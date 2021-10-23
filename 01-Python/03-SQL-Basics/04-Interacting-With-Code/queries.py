# pylint: disable=missing-docstring, C0103
import sqlite3

conn = sqlite3.connect('data/movies.sqlite')

def directors_count(db):
    # return the number of directors contained in the database
    query = '''
            SELECT COUNT(*)
            FROM directors
            '''
    db = conn.cursor()
    db.execute(query)
    results = db.fetchone()
    # results in a list (rows) of tuples (columns)
    return results[0]



def directors_list(db):
    # return the list of all the directors sorted in alphabetical order
    query = '''
            SELECT directors.name
            FROM directors
            ORDER BY directors.name ASC
            '''
    db = conn.cursor()
    db.execute(query)
    directors = db.fetchall()
    return [director[0] for director in directors]


def love_movies(db):
    # return the list of all movies which contain the word "love" in their title, sorted in alphabetical order
    query = '''
            SELECT movies.title
            FROM movies
            WHERE lower(movies.title) like "%love%"
            ORDER BY movies.title ASC
            '''
    db = conn.cursor()
    db.execute(query)
    movies = db.fetchall()
    return [movie[0] for movie in movies]


def directors_named_like_count(db, name):
    # return the number of directors which contain a given word in their name
    query = """
            SELECT COUNT(*)
            FROM directors
            WHERE directors.name like ?
            """
    db.execute(query, (f"%{name}%",))
    results = db.fetchone()
    return results[0]


def movies_longer_than(db, min_length):
    # return this list of all movies which are longer than a given duration, sorted in the alphabetical order
    query = '''
            SELECT movies.title
            FROM movies
            WHERE movies.minutes > ?
            ORDER BY movies.title ASC
            '''
    db = conn.cursor()
    db.execute(query, (min_length,))
    movies = db.fetchall()
    return [movie[0] for movie in movies]
