import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

df = pd.read_csv('final.csv')

df = df[df['metadata'].notna()]

count = CountVectorizer(stop_words = 'english')
countMatrix = count.fit_transform(df['metadata'])

cosine_sim = cosine_similarity(countMatrix, countMatrix)
df = df.reset_index()
indices = pd.Series(df.index, index = df['original_title'])

def getRec(title, cosine_sim):
    i = indices[title]
    simScores = list(enumerate(cosine_sim[i]))
    simScores = sorted(simScores, key = lambda x:x[1], reverse = True)
    simScores = simScores[1:11]
    movieIndices = [i[0] for i in simScores]
    return df['original_title', 'poster_link', 'release_date', 'runtime', 'vote_average', 'overview'].iloc[movieIndices].values.tolist()

