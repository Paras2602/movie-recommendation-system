from flask import Flask, render_template, request, jsonify
import pickle
import requests
import os

# Initialize Flask app
app = Flask(__name__)

# --------------------------
# Critical File Checks (Prevents crashes for your submission)
# --------------------------
REQUIRED_FILES = [
    "submission_recommender_model.pkl",
    "submission_user_item_matrix.pkl"
]

for file in REQUIRED_FILES:
    if not os.path.exists(file):
        raise FileNotFoundError(f"Critical file missing: {file}. Please run the cell in your Jupyter notebook to generate it.")

# --------------------------
# Load Trained Model and Data
# --------------------------
print("Loading recommendation model...")
with open('submission_recommender_model.pkl', 'rb') as f:
    knn_model = pickle.load(f)

with open('submission_user_item_matrix.pkl', 'rb') as f:
    user_item_matrix = pickle.load(f)
print("Model loaded successfully!")

# --------------------------
# In-Memory Rating Storage (No MongoDB Needed)
# --------------------------
user_ratings_store = {}

def save_user_ratings(user_id, ratings_dict):
    """Save user ratings to in-memory storage"""
    user_ratings_store[user_id] = ratings_dict

def get_user_ratings(user_id):
    """Retrieve user ratings from in-memory storage"""
    return user_ratings_store.get(user_id, {})

# --------------------------
# Recommendation Logic
# --------------------------
def get_fast_recommendations(user_id, top_n=5):
    """Generate personalized movie recommendations"""
    try:
        user_id = int(user_id)
        
        # Validate user exists in the dataset
        if user_id not in user_item_matrix.index:
            return []
        
        # Find similar users using KNN
        distances, indices = knn_model.kneighbors(
            user_item_matrix.loc[user_id].values.reshape(1, -1),
            n_neighbors=10
        )
        
        # Get ratings from top similar users (exclude the user themselves)
        similar_users = user_item_matrix.index[indices.flatten()[1:]]
        similar_user_ratings = user_item_matrix.loc[similar_users]
        
        # Calculate average ratings and sort
        avg_ratings = similar_user_ratings.mean(axis=0)
        sorted_ratings = avg_ratings.sort_values(ascending=False)
        
        # Exclude movies the user already rated
        user_rated_movies = user_item_matrix.loc[user_id][user_item_matrix.loc[user_id] > 0].index
        recommendations = sorted_ratings.drop(user_rated_movies).head(top_n)
        
        return recommendations.index.tolist()
    
    except Exception as e:
        print(f"Error generating recommendations: {str(e)}")
        return []

# --------------------------
# OMDB API Integration (Your Valid Key: 89c4b1c7)
# --------------------------
def get_movie_details(title):
    """Fetch movie metadata from OMDB API"""
    OMDB_API_KEY = "89c4b1c7"
    clean_title = title.split(' (')[0].strip()
    
    try:
        url = f"http://www.omdbapi.com/?t={clean_title}&apikey={OMDB_API_KEY}"
        response = requests.get(url, timeout=5)
        response.raise_for_status()
        
        data = response.json()
        if data.get('Response') == 'True':
            return {
                "title": data.get('Title', title),
                "year": data.get('Year', "N/A"),
                "genre": data.get('Genre', "N/A"),
                "imdb_rating": data.get('imdbRating', "N/A"),
                "poster": data.get('Poster', "https://via.placeholder.com/100x150")
            }
    
    except Exception as e:
        print(f"OMDB API error: {str(e)}")
    
    # Fallback if API request fails
    return {
        "title": title,
        "year": "N/A",
        "genre": "N/A",
        "imdb_rating": "N/A",
        "poster": "https://via.placeholder.com/100x150"
    }

# --------------------------
# Flask Web Routes
# --------------------------
@app.route('/', methods=['GET', 'POST'])
def index():
    recommendations = None
    user_id = None
    error = None

    if request.method == 'POST':
        # Get user ID from form
        user_id = int(request.form.get('user_id'))
        if not user_id:
            error = "Please enter a valid User ID"
            return render_template('index.html', error=error)
        
        # Process user ratings from form
        ratings_dict = {}
        for key, value in request.form.items():
            if key.startswith('movie_') and value.strip():
                movie_title = key.replace('movie_', '', 1)
                try:
                    rating = float(value)
                    if 1 <= rating <= 5:
                        ratings_dict[movie_title] = rating
                except:
                    continue
        
        # Save ratings if any were provided
        if ratings_dict:
            save_user_ratings(user_id, ratings_dict)
        
        # Generate recommendations
        rec_titles = get_fast_recommendations(user_id, top_n=5)
        if rec_titles:
            recommendations = [get_movie_details(title) for title in rec_titles]
        else:
            error = "No recommendations found for this User ID"

    return render_template('index.html', recommendations=recommendations, user_id=user_id, error=error)

# Optional API endpoint for testing
@app.route('/api/recommend/<user_id>', methods=['GET'])
def api_recommend(user_id):
    rec_titles = get_fast_recommendations(user_id)
    if rec_titles:
        recommendations = [get_movie_details(title) for title in rec_titles]
        return jsonify({"user_id": user_id, "recommendations": recommendations})
    return jsonify({"error": "No recommendations found"}), 404

# --------------------------
# Run the App
# --------------------------
if __name__ == '__main__':
    app.run(debug=True, port=5000, use_reloader=False)