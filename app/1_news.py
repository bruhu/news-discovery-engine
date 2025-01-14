import streamlit as st
import pandas as pd
import requests
import random

# Load the DataFrame
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
st.title("Top News Dashboard")

# Button to request location
if st.button("📍 Allow Location Access"):
    user_country = get_user_location()
    if user_country:
        st.session_state.user_country = (
            user_country  # Store the country in session state
        )
        st.write(f"Your location: {user_country}")

# Dropdowns for filtering
countries = response_df["country"].unique().tolist()
sources = response_df["source"].unique().tolist()
categories = response_df["category"].unique().tolist()

selected_country = st.selectbox("Select Country", countries)
selected_source = st.selectbox("Select Source", sources)
selected_category = st.selectbox("Select Category", categories)


# Filter news based on user selections
filtered_news = response_df[
    (response_df["country"] == selected_country)
    & (response_df["source"] == selected_source)
    & (response_df["category"] == selected_category)
]

# Display top news articles based on filters
if not filtered_news.empty:
    st.write("Filtered news articles:")
    for index, row in filtered_news.head(5).iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        if pd.notna(row["url"]):  # Check if URL exists
            st.markdown(f"[Read more]({row['url']})", unsafe_allow_html=True)
else:
    st.write("No news articles found for the selected filters. Displaying random news.")
    random_news = response_df.sample(n=5)
    for index, row in random_news.iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        if pd.notna(row["url"]):  # Check if URL exists
            st.markdown(f"[Read more]({row['url']})", unsafe_allow_html=True)
