# pylint: disable=C0103, missing-docstring

def detailed_movies(db):
    '''return the list of movies with their genres and director name'''
    query = """
        SELECT
            movies.title,
            movies.genres,
            directors.name
            FROM directors
        JOIN movies on movies.director_id = directors.id
        """
    db.execute(query)
    movies = db.fetchall()
    return movies

def late_released_movies(db):
    '''return the list of all movies released after their director death'''
    query = """
        SELECT
            movies.title
        FROM directors
        JOIN movies on movies.director_id = directors.id
        WHERE directors.death_year < movies.start_year
    """
    db.execute(query)
    movies = db.fetchall()
    return [movie[0] for movie in movies]


def stats_on(db, genre_name):
    '''return a dict of stats for a given genre'''
    query = """
        SELECT
            movies.genres,
            COUNT(*),
            ROUND(AVG(movies.minutes))
        FROM movies
        WHERE movies.genres = ?
    """
    db.execute(query, (genre_name,))
    movies = db.fetchone()
    print(movies)
    return {
        'genre': movies[0],
        'number_of_movies': movies[1],
        'avg_length': movies[2]
    }

def top_five_directors_for(db, genre_name):
    '''return the top 5 of the directors with the most movies for a given genre'''
    query = """
        SELECT
            directors.name,
            COUNT(*) as c
        FROM movies
        JOIN directors ON directors.id = movies.director_id
        WHERE movies.genres = ?
        GROUP BY directors.name
        ORDER BY c DESC, directors.name
        LIMIT 5
    """
    db.execute(query,(genre_name,))
    directors = db.fetchall()
    return directors

def movie_duration_buckets(db):
    '''return the movie counts grouped by bucket of 30 min duration'''
    query = """
        SELECT
            (movies.minutes / 30 + 1) * 30 time_range,
            COUNT(*)
        FROM movies
        WHERE movies.minutes NOTNULL
        GROUP BY time_range
    """
    db.execute(query)
    buckets = db.fetchall()
    return buckets


def top_five_youngest_newly_directors(db):
    '''return the top 5 youngest directors when they direct their first movie'''
    query = """
        SELECT
            directors.name,
            movies.start_year - directors.birth_year AS age
        FROM directors
        JOIN movies on movies.director_id = directors.id
        GROUP BY directors.name
        HAVING age IS NOT NULL
        ORDER BY age
        LIMIT 5
    """
    db.execute(query)
    directors = db.fetchall()
    return directors
