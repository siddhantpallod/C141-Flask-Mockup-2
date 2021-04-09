from flask import Flask, request, jsonify
import csv
import pandas as pd
from demographic import output
from content import getRec

allMovies = []
likedMovies = []
notLikedMovies = []
didNotWatchMovies = []

with open('final.csv', encoding = "utf8") as f:
    reader = csv.reader(f)

    df = list(reader)
    allMovies = df[1:]

app = Flask(__name__)

@app.route('/get-movie')

def getMovie():
    movieData = {
        'original_title': allMovies[0][8],
        'poster_link': allMovies[0][27],    
        'release_date': allMovies[0][13] or 'n/a',
        'duration': allMovies[0][15],
        'rating': allMovies[0][20],
        'overview': allMovies[0][9]
    }
    return jsonify({
        'data': movieData,
        'message': 'success'
    })

@app.route('/liked-movies', methods = ['POST'])

def likedMovie():
    movie = allMovies[0]
    likedMovies.append(movie)
    allMovies.pop(0)

    return jsonify({
        'message': 'success'
    })

@app.route('/unliked-movies', methods = ['POST'])

def unlikedMovies():
    movie = allMovies[0]
    notLikedMovies.append(movie)
    allMovies.pop(0)

    return jsonify({
        'message': 'success'
    })

@app.route('/did-not-watch', methods = ['POST'])

def didNotWatch():
    movie = allMovies[0]
    didNotWatchMovies.append(movie)
    allMovies.pop(0)

    return jsonify({
        'message': 'sucess'
    })

@app.route('/popular-movies')

def popularMovies():
    movieData = []

    for movie in output:
        d = {
            'original_title': movie[0], 
            'poster_link': movie[1],
            'release_date': movie[2] or 'n/a',
            'runtime': movie[3],
            'rating': movie[4],
            'overview': movie[5]
        }

        movieData.append(d)

    return jsonify({
        'data': movieData,
        'message': 'success'
    })

@app.route('/recommended-movies')

def recoMovies():
    recMovies = []

    for data in likedMovies:
        output = getRec(data[0])
        for data1 in output:
            recMovies.append(data1)

    import itertools
    recMovies.sort()
    recMovies = list(recMovies for recMovies, in itertools.groupby(recMovies))
    movieData = []

    for movie in recMovies:
        b = {
            'original_title': movie[0], 
            'poster_link': movie[1],
            'release_date': movie[2] or 'n/a',
            'runtime': movie[3],
            'rating': movie[4],
            'overview': movie[5]
        }

        movieData.append(b)

    return jsonify({
        'data': movieData,
        'message': 'success'
    })

if(__name__ == '__main__'):
    app.run()