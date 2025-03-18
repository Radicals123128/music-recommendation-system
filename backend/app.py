from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import os

app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing

# Load dataset
dataset_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), 'dataset', 'Bollywood-songs.csv')
try:
    # Try different encodings
    encodings = ['utf-8', 'latin1', 'iso-8859-1', 'cp1252']
    for encoding in encodings:
        try:
            df = pd.read_csv(dataset_path, encoding=encoding)
            print(f"Successfully loaded the dataset with {encoding} encoding")
            break
        except UnicodeDecodeError:
            continue
except Exception as e:
    print(f"Error loading the dataset: {str(e)}")
    raise

# Preprocess: Combine relevant features
df["combined_features"] = df["Singer/Artists"] + " " + df["Album/Movie"] + " " + df["Genre"]

# TF-IDF Vectorization
vectorizer = TfidfVectorizer(stop_words="english")
tfidf_matrix = vectorizer.fit_transform(df["combined_features"].fillna(""))

# Compute similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Function to recommend songs
def get_recommendations(song_name):
    if song_name not in df["Song-Name"].values:
        return ["Song not found"]
    
    idx = df[df["Song-Name"] == song_name].index[0]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)[1:6]
    
    recommended_songs = []
    for i in sim_scores:
        song_info = {
            "name": df.iloc[i[0]]["Song-Name"],
            "singer": df.iloc[i[0]]["Singer/Artists"],
            "movie": df.iloc[i[0]]["Album/Movie"],
            "genre": df.iloc[i[0]]["Genre"],
            "rating": df.iloc[i[0]]["User-Rating"]
        }
        recommended_songs.append(song_info)
    return recommended_songs

@app.route("/recommend", methods=["GET"])
def recommend():
    song_name = request.args.get("song")
    recommendations = get_recommendations(song_name)
    return jsonify({"recommendations": recommendations})

if __name__ == "__main__":
    app.run(debug=True) 