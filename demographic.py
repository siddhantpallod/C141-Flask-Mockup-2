import pandas as pd
import numpy as np

df = pd.read_csv('final.csv')

# # ((v/(v+m))*R)+((m/(v+m))*C) 

C = df['vote_average'].mean()

m = df['vote_count'].quantile(0.9)

listedMovies = df.copy().loc[df['vote_count'] >= m]

def weightedRating(x, m = m, C = C):
    v  = x['vote_count']
    R = x['vote_average']

    return ((v/(v+m))*R)+((m/(v+m))*C) 

listedMovies['score'] = listedMovies.apply(weightedRating, axis = 1)
listedMovies = listedMovies.sort_values('score', ascending = False)
output = listedMovies[['original_title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview']].head(20).values.tolist()