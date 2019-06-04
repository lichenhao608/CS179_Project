import numpy as np
from sklearn.mixture import GaussianMixture
from collections import Counter

# data processing
category = np.loadtxt('data/movie_data/users.dat', dtype=object)
category[:, 1] = np.unique(category[:, 1], return_inverse=True)[1]
category[:, 2] = np.unique(category[:, 2], return_inverse=True)[1]
category = category[:, 1:]

ratings = np.loadtxt('data/movie_data/movies.std', dtype=int)

movies = np.loadtxt('data/movie_data/movies.cod',
                    dtype=str, usecols=1, ndmin=2)


# train and test set seperation
n_sample = category.shape[0]
n_movies = ratings.shape[1]
n_train = int(0.8 * n_sample)

train_sample = category[:n_train]
train_rating = ratings[:n_train]

test_sample = category[n_train:]
test_rating = ratings[n_train:]

mix_class = [GaussianMixture(n_components=6, covariance_type='tied')
             for _ in range(n_movies)]
for k in range(n_movies):
    mix_class[k].fit(train_sample)

a = mix_class[0].predict(test_sample)
b = mix_class[1].predict(test_sample)
temp = np.stack((a, b), axis=1)
for i in range(2, n_movies):
    temp = np.concatenate((temp, mix_class[i].predict(
        test_sample)[..., np.newaxis]), axis=1)

print(temp)
print(np.sum(np.abs(temp-test_rating))/np.product(test_rating.shape))
