# Movie Recommendation System

A personalized **Movie Recommendation System** that suggests movies to users based on their preferences using **content-based filtering** and machine learning techniques.


##  Features
- Personalized movie recommendations
- Content-based filtering approach
- User–item similarity calculation
- Simple and interactive web interface
- Pre-trained recommendation model


##  Technologies Used
- Python
- Machine Learning
- Pandas & NumPy
- Scikit-learn
- Flask
- HTML / CSS


##  Project Structure

movie-recommendation-system/
│
├── templates/
│ └── index.html # Frontend UI
├── app.py # Flask application
├── movie_recommender_model.ipynb # Model training notebook
├── movies.csv # Movie dataset
├── submission_recommender_model.pkl
├── submission_user_item_matrix.pkl
├── test_model.py # Model testing script
├── demo recommendation.png # Output screenshot
├── README.md
└── .gitignore



## How It Works
- Movie features are extracted from the dataset
- Similarity between movies is calculated
- Based on user selection, similar movies are recommended
- Model uses **content-based filtering** logic


##  How to Run the Project

###  Clone the Repository
```bash
git clone https://github.com/Paras2602/movie-recommendation-system.git

