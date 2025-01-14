import streamlit as st
import pandas as pd
import requests
import random

# Sample DataFrame (replace this with your actual DataFrame)
data = pd.read_csv("data/clean/1_mediastack_news_cleaned.csv")
response_df = pd.DataFrame(data)


# Function to get user location
def get_user_location():
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data["country"]
    except Exception as e:
        st.error("Could not retrieve location. Defaulting to random news.")
        return None


# Streamlit app
st.title("Top News Based on Your Location")

# Ask for user permission to access location
if st.button("Allow Access to Location"):
    user_country = get_user_location()
    if user_country:
        st.write(f"Your location: {user_country}")

        # Filter news based on user location
        filtered_news = response_df[response_df["country"] == user_country]

        # Display top 5 news articles
        if not filtered_news.empty:
            st.write("Top 5 news articles:")
            for index, row in filtered_news.head(5).iterrows():
                st.subheader(row["title"])
                st.write(row["description"])
        else:
            st.write(
                "No news articles found for your location. Displaying random news."
            )
            random_news = response_df.sample(n=5)
            for index, row in random_news.iterrows():
                st.subheader(row["title"])
                st.write(row["description"])
else:
    st.write("You can choose to allow access to your location to see relevant news.")
    # Display random news if location is not provided
    random_news = response_df.sample(n=5)
    st.write("Displaying random news:")
    for index, row in random_news.iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
