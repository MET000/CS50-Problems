SELECT title, rating FROM movies, ratings WHERE movies.id = ratings.movie_id AND rating NOT NULL AND year = 2010 ORDER BY rating DESC, title;
