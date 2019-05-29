import numpy as np

category = np.loadtxt('data/movie_data/users.dat', dtype=object)
category[:, 0] = category[:, 0].astype(int)
print(category)

ratings = np.loadtxt('data/movie_data/movies.std', dtype=int)
print(ratings)

movies = np.loadtxt('data/movie_data/movies.cod',
                    dtype=str, usecols=1, ndmin=2)
print(movies)
