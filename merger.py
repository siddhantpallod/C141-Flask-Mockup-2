import csv
import pandas as pd

allMovies = []
allMoviesLinks = []

with open('movies.csv', encoding = "utf8") as d:
    reader = csv.reader(d)
    df = list(reader)
    allMovies = df[1:]
    headers = df[0]

headers.append('poster_link')

with open('final.csv', 'a+', encoding = "utf8") as f:
    csvWriter = csv.writer(f)
    csvWriter.writerow(headers)

with open('movie_links.csv', encoding = "utf8") as a:
    reader = csv.reader(a)
    data = list(reader)

    allMoviesLinks = data[1:]

for movie in allMovies:
    posterFound = any(movie[8] in movieLink for movieLink in allMoviesLinks)
    if posterFound:
        for movieLink in allMoviesLinks:
            if movie[8] == movieLink[0]:
                movie.append(movieLink[1])
                if len(movie) == 28:
                    with open('final.csv', 'a+', encoding = "utf8") as c:
                        csvWriter = csv.writer(c)
                        csvWriter.writerow(movie)