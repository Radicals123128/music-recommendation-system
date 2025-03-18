# Bollywood Songs Recommendation System

A content-based recommendation system for Bollywood songs using Flask API and a modern web interface.

## Features

- Search for Bollywood songs
- Get personalized song recommendations based on content similarity
- Modern and responsive user interface
- Real-time recommendations using TF-IDF and Cosine Similarity

## Project Structure

```
music-recommendation-system/
│── backend/               # Flask API
│   ├── app.py             # Main Flask application
│   ├── requirements.txt   # Dependencies
│── frontend/              # HTML, CSS, JavaScript frontend
│   ├── index.html         # Main UI
│   ├── styles.css         # CSS file
│   ├── script.js          # JavaScript file
│── Bollywood-songs.csv    # Dataset file
│── README.md              # Project documentation
```

## Setup Instructions

1. **Install Dependencies**
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

2. **Run the Backend**
   ```bash
   cd backend
   python app.py
   ```

3. **Open Frontend**
   - Open `frontend/index.html` in your web browser
   - Or use a local server to serve the frontend files

## Usage

1. Enter a Bollywood song name in the search box
2. Click "Recommend" or press Enter
3. View the recommended songs based on content similarity

## Technologies Used

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Recommendation Engine**: TF-IDF + Cosine Similarity
- **Dataset**: Bollywood Songs Dataset

## API Endpoint

- **GET** `/recommend?song=song_name`
  - Returns a list of 5 recommended songs based on the input song

## Contributing

Feel free to submit issues and enhancement requests! 