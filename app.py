from flask import Flask, render_template, request, jsonify
import json
import os
from datetime import datetime

app = Flask(__name__)

# Load movie data
def load_movies():
    movies = [
        {
            'id': 1,
            'title': 'The Shawshank Redemption',
            'genre': ['Drama'],
            'rating': 9.3,
            'year': 1994,
            'description': 'Two imprisoned men bond over a number of years, finding solace and eventual redemption through acts of common decency.'
        },
        {
            'id': 2,
            'title': 'The Godfather',
            'genre': ['Drama', 'Crime'],
            'rating': 9.2,
            'year': 1972,
            'description': 'The aging patriarch of an organized crime dynasty transfers control of his clandestine empire to his reluctant youngest son.'
        },
        {
            'id': 3,
            'title': 'The Dark Knight',
            'genre': ['Action', 'Crime', 'Drama'],
            'rating': 9.0,
            'year': 2008,
            'description': 'When the menace known as the Joker wreaks havoc on Gotham, Batman must accept one of the greatest tests.'
        },
        {
            'id': 4,
            'title': 'Pulp Fiction',
            'genre': ['Crime', 'Drama'],
            'rating': 8.9,
            'year': 1994,
            'description': 'The lives of two mob hitmen, a boxer, a gangster and his wife intertwine in four tales of violence and redemption.'
        },
        {
            'id': 5,
            'title': 'Forrest Gump',
            'genre': ['Drama', 'Romance'],
            'rating': 8.8,
            'year': 1994,
            'description': 'The presidencies of Kennedy and Johnson unfold from the perspective of an Alabama man with an IQ of 75.'
        },
        {
            'id': 6,
            'title': 'Inception',
            'genre': ['Action', 'Sci-Fi', 'Thriller'],
            'rating': 8.8,
            'year': 2010,
            'description': 'A thief who steals corporate secrets through the use of dream-sharing technology is given a chance for redemption.'
        },
        {
            'id': 7,
            'title': 'The Matrix',
            'genre': ['Action', 'Sci-Fi'],
            'rating': 8.7,
            'year': 1999,
            'description': 'A computer hacker learns from mysterious rebels about the true nature of his reality and his role in the war against its controllers.'
        },
        {
            'id': 8,
            'title': 'Interstellar',
            'genre': ['Adventure', 'Drama', 'Sci-Fi'],
            'rating': 8.6,
            'year': 2014,
            'description': 'A team of explorers travel through a wormhole in space in an attempt to ensure humanity\'s survival.'
        }
    ]
    return movies

# Get recommendations based on rating
def get_recommendations(min_rating=7.0, genre=None):
    movies = load_movies()
    recommendations = []
    
    for movie in movies:
        if movie['rating'] >= min_rating:
            if genre is None or genre in movie['genre']:
                recommendations.append(movie)
    
    # Sort by rating
    recommendations.sort(key=lambda x: x['rating'], reverse=True)
    return recommendations

@app.route('/')
def index():
    movies = load_movies()
    genres = set()
    for movie in movies:
        genres.update(movie['genre'])
    
    return render_template('index.html', movies=movies, genres=sorted(list(genres)))

@app.route('/recommend', methods=['GET', 'POST'])
def recommend():
    if request.method == 'POST':
        min_rating = float(request.form.get('min_rating', 7.0))
        genre = request.form.get('genre', None)
        
        if genre == 'all':
            genre = None
        
        recommendations = get_recommendations(min_rating, genre)
        movies = load_movies()
        genres = set()
        for movie in movies:
            genres.update(movie['genre'])
        
        return render_template('index.html', 
                             movies=movies, 
                             genres=sorted(list(genres)),
                             recommendations=recommendations,
                             selected_rating=min_rating,
                             selected_genre=genre)
    
    movies = load_movies()
    genres = set()
    for movie in movies:
        genres.update(movie['genre'])
    
    return render_template('index.html', movies=movies, genres=sorted(list(genres)))

@app.route('/api/movies')
def api_movies():
    movies = load_movies()
    return jsonify(movies)

@app.route('/api/recommend')
def api_recommend():
    min_rating = float(request.args.get('min_rating', 7.0))
    genre = request.args.get('genre', None)
    
    if genre == 'all':
        genre = None
    
    recommendations = get_recommendations(min_rating, genre)
    return jsonify(recommendations)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

if __name__ == '__main__':
    app.run(debug=True, port=5000)
