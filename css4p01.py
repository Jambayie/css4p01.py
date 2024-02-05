# -*- coding: utf-8 -*-
"""
Created on Mon Feb  5 18:51:02 2024

@author: Khosa Rito
"""

import pandas as pd
from collections import Counter
movie = pd.read_csv("movie_dataset.csv")
print(movie)

#question 1
highest_value = (movie['Rating'].max())
Name_of_Most_Rated_Movie = movie.loc[movie['Rating'].idxmax()]['Title']

#question 2
average_revenue = movie['Revenue (Millions)'].mean()
print("The average revenue of all movies in the dataset is:", average_revenue)

#question 3
filtered_data = movie[(movie['Year'] >= 2015) & (movie['Year'] <= 2017)]
average_revenue_2015_to_2017 = filtered_data['Revenue (Millions)'].mean()
print("The average revenue of movies from 2015 to 2017 in the dataset is:", average_revenue_2015_to_2017)

#question 4
number_of_movies_2016 = movie[movie['Year'] == 2016].shape[0]
print("The number of movies released in the year 2016 is:", number_of_movies_2016)

#question 5
number_of_movies_by_nolan = movie[movie['Director'] == 'Christopher Nolan'].shape[0]
print("The number of movies directed by Christopher Nolan is:", number_of_movies_by_nolan)

#question 6
number_of_highly_rated_movies = movie[movie['Rating'] >= 8.0].shape[0]
print("The number of movies with a rating of at least 8.0 is:", number_of_highly_rated_movies)

#question 7
nolan_movies = movie[movie['Director'] == 'Christopher Nolan']
median_rating_nolan_movies = nolan_movies['Rating'].median()
print("The median rating of movies directed by Christopher Nolan is:", median_rating_nolan_movies)

#question 8
average_rating_by_year = movie.groupby('Year')['Rating'].mean()
year_highest_avg_rating = average_rating_by_year.idxmax()
print("The year with the highest average rating is:", year_highest_avg_rating)

#question 9
movies_2006 = movie[movie['Year'] == 2006]
movies_2016 = movie[movie['Year'] == 2016]
num_movies_2006 = len(movies_2006)
num_movies_2016 = len(movies_2016)
percentage_increase = ((num_movies_2016 - num_movies_2006) / num_movies_2006) * 100
print(f"The percentage increase in the number of movies made between 2006 and 2016 is: {percentage_increase:.2f}%")

#question 10
all_actors = ','.join(movie['Actors'].dropna()).split(',')
actor_counts = Counter(all_actors)
most_common_actor = actor_counts.most_common(1)[0][0]
print("The most common actor in all movies is:", most_common_actor)

#question 11
all_genres = ','.join(movie['Genre'].dropna()).split(',')
unique_genres = set(all_genres)
num_unique_genres = len(unique_genres)
print("The number of unique genres in the dataset is:", num_unique_genres)

#question 12

#12.1
numerical_features = movie.select_dtypes(include=['int64', 'float64'])
correlation_matrix = numerical_features.corr()
print("Correlation Matrix:")
print(correlation_matrix)