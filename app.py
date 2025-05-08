import streamlit as st
import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.preprocessing import MinMaxScaler
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Load Dataset
@st.cache_data
def load_data():
    file_path = "C:\\Cognifyz Technologies\\Tasks\\task 2 - restaurent recomendation\\Dataset .csv"
    df = pd.read_csv(file_path)
    df['Cuisines'] = df['Cuisines'].fillna('Unknown')
    return df

df = load_data()

# Encode 'Cuisines' using TF-IDF
tfidf = TfidfVectorizer(stop_words='english')
tfidf_matrix = tfidf.fit_transform(df['Cuisines'])

# Normalize numerical features
scaler = MinMaxScaler()
numerical_features = scaler.fit_transform(df[['Average Cost for two', 'Price range', 'Aggregate rating']])
combined_features = np.hstack([tfidf_matrix.toarray(), numerical_features])

# Streamlit UI
st.title("Restaurant Recommendation System 🍽️")
#cuisine_pref = st.text_input("Enter preferred cuisine (e.g., Italian)")
available_cuisines = [
    "Afghan", "African", "American", "Andhra", "Arabian", "Argentine", "Asian", "Assamese", "Awadhi", "BBQ",
    "Bakery", "Bar Food", "Belgian", "Beverages", "Bihari", "Biryani", "Brazilian", "British", "Bubble Tea", "Burmese",
    "Cafe", "Cantonese", "Charcoal Chicken", "Chettinad", "Chinese", "Coffee", "Continental", "Cuban", "Desserts", "European",
    "Fast Food", "Finger Food", "French", "German", "Goan", "Greek", "Grill", "Gujarati", "Healthy Food", "Hyderabadi",
    "Ice Cream", "Indian", "Indonesian", "Iranian", "Italian", "Japanese", "Juices", "Kebab", "Kerala", "Korean",
    "Lebanese", "Lucknowi", "Maharashtrian", "Malaysian", "Malwani", "Mangalorean", "Mediterranean", "Mexican", "Middle Eastern", "Mithai",
    "Modern Indian", "Mughlai", "Naga", "Nepalese", "North Eastern", "North Indian", "Oriya", "Parsi", "Pizza", "Portuguese",
    "Punjabi", "Rajasthani", "Rolls", "Russian", "Salad", "Sandwich", "Seafood", "Sichuan", "Singaporean", "South American",
    "South Indian", "Sri Lankan", "Steak", "Street Food", "Sushi", "Tea", "Thai", "Tibetan", "Turkish", "Vietnamese"
]

# Create a dropdown selection for cuisine preference
cuisine_pref = st.selectbox("Select preferred cuisine", available_cuisines)
# get other requirements for recomendation
min_cost = st.number_input("Enter minimum cost", min_value=0, step=100)
max_cost = st.number_input("Enter maximum cost", min_value=0, step=100)
min_rating = st.slider("Select minimum rating", 0.0, 5.0, 4.0)# slider 

# Function for recommendation
def recommend_restaurants(cuisine_pref, min_cost, max_cost, min_rating, top_n=5):
    dummy = pd.DataFrame({
        'Cuisines': [cuisine_pref],
        'Average Cost for two': [(min_cost + max_cost) / 2],
        'Price range': [2],
        'Aggregate rating': [min_rating]
    })

    dummy_tfidf = tfidf.transform(dummy['Cuisines'])
    dummy_scaled = scaler.transform(dummy[['Average Cost for two', 'Price range', 'Aggregate rating']])
    dummy_combined = np.hstack([dummy_tfidf.toarray(), dummy_scaled])
    similarity_scores = cosine_similarity(dummy_combined, combined_features).flatten()
    top_indices = similarity_scores.argsort()[-top_n:][::-1]

    return df.loc[top_indices, ['Restaurant Name', 'Cuisines', 'Average Cost for two', 'Aggregate rating']].assign(Similarity=similarity_scores[top_indices])

if st.button("Recommend Restaurants"):
    recommendations = recommend_restaurants(cuisine_pref, min_cost, max_cost, min_rating)
    st.write("### Top Recommended Restaurants")
    st.dataframe(recommendations)