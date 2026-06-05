# Movie Recommender App

A Flask-based web application that recommends movies based on user preferences including rating and genre filtering.

## Features

- 🎬 Browse a curated collection of movies
- ⭐ Filter movies by minimum rating (5.0 - 10.0)
- 🎭 Filter by movie genre (Action, Drama, Sci-Fi, etc.)
- 🌐 Responsive web interface
- 📱 Mobile-friendly design
- 🔄 RESTful API endpoints for programmatic access

## Movie Database

The app includes a database of popular movies with:
- Movie titles
- Ratings (IMDb-style)
- Release years
- Genres
- Descriptions

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package manager)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/syedmujtabaquadhri-dotcom/movie-recomandation.git
cd Movie-Recommender-App
```

2. Create a virtual environment (recommended):
```bash
# On Windows
python -m venv venv
venv\Scripts\activate

# On macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the Application

1. Start the Flask development server:
```bash
python app.py
```

2. Open your web browser and navigate to:
```
http://localhost:5000
```

3. Use the filters to find movie recommendations:
   - Set your minimum acceptable rating
   - Choose a genre (or "All Genres")
   - Click "Get Recommendations"

## API Endpoints

### Get All Movies
```
GET /api/movies
```
Returns a JSON array of all movies.

### Get Recommendations
```
GET /api/recommend?min_rating=7.5&genre=Action
```
Query parameters:
- `min_rating` (optional): Minimum rating filter (default: 7.0)
- `genre` (optional): Genre filter (use "all" for no filter)

## Project Structure

```
Movie-Recommender-App/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # This file
├── templates/
│   ├── index.html        # Main page template
│   └── 404.html          # 404 error page
└── static/
    └── style.css         # CSS styling
```

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Database**: In-memory Python objects (can be extended to use databases)

## Future Enhancements

- Database integration (SQLite, PostgreSQL)
- User authentication and profiles
- Personalized recommendations using ML
- Movie search functionality
- User ratings and reviews
- Advanced filtering options
- Favorite movies list

## License

This project is open source and available under the MIT License.

## Contributing

Contributions are welcome! Feel free to:
1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## Support

For issues or questions, please open an issue on GitHub.

## Author

Movie Recommender App - Syed Mujtaba Quadhri
