import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
ratings_matrix = np.array([
    [5, 4, 0, 0, 3],
    [0, 0, 5, 0, 4],
    [0, 0, 0, 3, 0],
    [4, 5, 0, 0, 0],
    [0, 0, 4, 0, 5]
])
def calculate_cosine_similarity(ratings_matrix):
    similarity_matrix = cosine_similarity(ratings_matrix)
    np.fill_diagonal(similarity_matrix, 0)  # Set self-similarity to 0
    return similarity_matrix
# Define a function to make movie recommendations for a user
def recommend_movies(user_id, ratings_matrix, similarity_matrix, num_recommendations=5):
    user_ratings = ratings_matrix[user_id]
    similar_users = similarity_matrix[user_id]

    # Find users most similar to the target user
    most_similar_users = np.argsort(similar_users)[::-1]

    # Initialize recommendation list
    recommendations = []

    for user in most_similar_users:
        if user_ratings[user] == 0:  # User hasn't rated this movie
            movie_ratings = ratings_matrix[user]
            rated_indices = np.where(movie_ratings > 0)
            movie_score = np.sum(movie_ratings[rated_indices] * similar_users[user])
            recommendations.append((movie_score, user))

        if len(recommendations) >= num_recommendations:
            break
    recommendations.sort(reverse=True)
    recommended_movie_indices = [user for _, user in recommendations]
    return recommended_movie_indices
user_id = 0  # Replace with the user ID you want to recommend movies for
similarity_matrix = calculate_cosine_similarity(ratings_matrix)
recommended_movies = recommend_movies(user_id, ratings_matrix, similarity_matrix)

print(f"Recommended movies for user {user_id}: {recommended_movies}")
