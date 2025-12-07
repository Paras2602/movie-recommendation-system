import pickle

# Load the trained model and user-item matrix
with open("submission_recommender_model.pkl", "rb") as f:
    knn_model = pickle.load(f)

with open("submission_user_item_matrix.pkl", "rb") as f:
    user_item_matrix = pickle.load(f)

# Test with User ID 1 (guaranteed to exist in our dataset)
user_id = 1
if user_id in user_item_matrix.index:
    print(f"✅ User ID {user_id} exists in the dataset")
    
    # Generate recommendations directly
    distances, indices = knn_model.kneighbors(
        user_item_matrix.loc[user_id].values.reshape(1, -1),
        n_neighbors=10
    )
    similar_users = user_item_matrix.index[indices.flatten()[1:]]
    similar_ratings = user_item_matrix.loc[similar_users].mean(axis=0)
    top_recs = similar_ratings.sort_values(ascending=False).head(5)
    
    print("\n✅ Top 5 Recommendations:")
    for title in top_recs.index:
        print(f"- {title}")
else:
    print(f"❌ User ID {user_id} not found")