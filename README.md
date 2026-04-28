# Movie Recommendation System

This project is a Machine Learning–based application that recommends movies to users using a content-based filtering approach. It suggests similar movies based on features such as genre, title, and other attributes.

---

## Features
- Content-based movie recommendation  
- Similarity calculation using cosine similarity  
- Simple and interactive web interface  
- Fast and efficient recommendation system  

---

## Technologies Used
- Python  
- Machine Learning  
- Pandas  
- NumPy  
- Scikit-learn  
- Flask  
- HTML / CSS  

---

## Dataset
- Movie dataset containing titles and features  
- Data preprocessed for similarity computation  

---

## Model
- Approach: Content-Based Filtering  
- Technique Used: Cosine Similarity  
- Feature Processing: Vectorization of movie data  

---

## Project Structure

```
movie-recommendation-system/
│
├── templates/
│   └── index.html
├── app.py
├── movie_recommender_model.ipynb
├── movies.csv
├── submission_recommender_model.pkl
├── submission_user_item_matrix.pkl
├── test_model.py
├── demo_recommendation.png
├── README.md
└── .gitignore
```

---

## How It Works
- Movie features are extracted from the dataset  
- Features are converted into vectors  
- Similarity between movies is calculated using cosine similarity  
- Based on user input, similar movies are recommended  

---

## How to Run the Project

1. Clone the repository  
   ```bash
   git clone https://github.com/Paras2602/movie-recommendation-system.git
   cd movie-recommendation-system
   ```

2. Install dependencies  
   ```bash
   pip install pandas numpy scikit-learn flask
   ```

3. Run the application  
   ```bash
   python app.py
   ```

4. Open in browser  
   ```
   http://127.0.0.1:5000/
   ```

---

## Sample User IDs
You can test the system using the following user IDs:

548, 626, 847, 997, 1401, 1652, 1748, 1920, 1977, 2003,  
2165, 2177, 2403, 2775, 2982, 3150, 3394, 3503, 3623, 3624

## Usage
- Enter a user ID from the sample list  
- Provide ratings for movies (if required)  
- The system recommends movies based on user preferences  

---

## Output
<img width="1051" height="582" alt="image" src="https://github.com/user-attachments/assets/ca3f11a2-ef36-4d20-ab7e-b24fec2410be" />
<img width="953" height="874" alt="image" src="https://github.com/user-attachments/assets/db3c6831-ad6d-43e3-9307-980d220381d7" />


---

## Future Improvements
- Add collaborative filtering  
- Improve recommendation accuracy  
- Build UI using Streamlit  

---

## Author
Paras JB
