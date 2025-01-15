import streamlit as st
import pandas as pd
import requests
import random

# Load the DataFrame
data = pd.read_csv("data/clean/1_mediastack_news_cleaned.csv")
response_df = pd.DataFrame(data)

# Initialize location_news
location_news = None


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

# Show random news or news based on location
if "user_country" in st.session_state:
    # Filter news based on user location
    location_news = response_df[response_df["country"] == st.session_state.user_country]
    if not location_news.empty:
        st.write("News articles based on your location:")
        for index, row in location_news.head(5).iterrows():
            st.subheader(row["title"])
            st.write(row["description"])
            if pd.notna(row["url"]):  # Check if URL exists
                st.markdown(
                    f"[Read full article]({row['url']})", unsafe_allow_html=True
                )
    else:
        st.write("No news articles found for your location. Displaying random news.")
        location_news = None  # No location news found
else:
    st.write("Location access not granted. Displaying random news.")

# If no location news, show random news
if location_news is None or location_news.empty:
    st.write("Displaying random news:")
    random_news = response_df.sample(n=5)
    for index, row in random_news.iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        if pd.notna(row["url"]):  # Check if URL exists
            st.markdown(f"[Read full article]({row['url']})", unsafe_allow_html=True)

# Toggle for showing filters
show_filters = st.button("Show Filters")

if show_filters:
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
                st.markdown(
                    f"[Read full article]({row['url']})", unsafe_allow_html=True
                )
    else:
        st.write("No news articles found for the selected filters.")
else:
    st.write("Click 'Show Filters' to display the filtering options.")
