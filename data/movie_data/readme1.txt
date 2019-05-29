source: B. Mon=basher, DePaul University

Description of the Data
=======================

The data set includes movie ratings collected through user
interactions with the site www.movielens.org. This includes
ratings on the scale of 1 (worst) to 5 (best) by 500 users
of 1000 movies.


Description of the Data Files
=============================

"movies.cod"
------------
This file contains the movies names.


"movies.std"
------------
This is the actual rating information for each user. Each line
contains ratings of one user (starting from user 0) for the 1000
movies (starting from movie 0). If the user has not rated a movie,
the entry in the table is a 0, otherwise, it is a number between
1 and 5. This file can be used for making collaborative 
recommendations.

"users.dat"
-----------
This file contains some additional demographic attributes for each
user. The format of the columns in this file is as follows:

	<age>	<gender>	<occupation>
	
The rows in this file correspond to the rows in the movies.std
file (i.e., one for each user). This file can be used to 
characterize the clusters of users.

