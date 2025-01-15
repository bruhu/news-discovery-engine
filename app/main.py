import streamlit as st
import pandas as pd
from utils import get_user_location, load_data, filter_news

# Load the DataFrame
data_file_path = "data/clean/1_mediastack_news_cleaned.csv"
response_df = load_data(data_file_path)

# Initialize location_news
location_news = None

# Streamlit app
st.title("Top News Dashboard")


def display_news(articles):
    """Display news articles in the Streamlit app."""
    for index, row in articles.iterrows():
        st.subheader(row["title"])
        st.write(row["description"])
        if pd.notna(row["url"]):  # Check if URL exists
            st.markdown(f"[Read full article]({row['url']})", unsafe_allow_html=True)


def show_location_news():
    """Show news articles based on the user's location."""
    global location_news
    location_news = response_df[response_df["country"] == st.session_state.user_country]
    if not location_news.empty:
        st.write("News articles based on your location:")
        display_news(location_news.head(5))
    else:
        st.write("No news articles found for your location. Displaying random news.")
        location_news = None  # No location news found


def show_random_news():
    """Show random news articles."""
    st.write("Displaying random news:")
    random_news = response_df.sample(n=5)
    display_news(random_news)


def show_filters():
    """Display filter dropdowns and handle filtering logic."""
    countries = ["---"] + response_df["country"].unique().tolist()
    sources = ["---"] + response_df["source"].unique().tolist()
    categories = ["---"] + response_df["category"].unique().tolist()

    selected_country = st.selectbox("Select Country", countries)
    selected_source = st.selectbox("Select Source", sources)
    selected_category = st.selectbox("Select Category", categories)

    # Filter news based on user selections
    filtered_news = filter_news(
        response_df, selected_country, selected_source, selected_category
    )

    # Display top news articles based on filters
    if not filtered_news.empty:
        st.write("Filtered news articles:")
        display_news(filtered_news.head(5))
    else:
        st.write("No news articles found for the selected filters.")


# Button to request location
if st.button("📍 Allow Location Access"):
    user_country = get_user_location()
    if user_country:
        st.session_state.user_country = (
            user_country  # Store the country in session state
        )
        st.write(f"Your location: {user_country}")

# Show news based on location or random news
if "user_country" in st.session_state:
    show_location_news()
else:
    st.write("Location access not granted. Displaying random news.")
    show_random_news()

# Toggle for showing filters
if st.button("Show Filters"):
    show_filters()
else:
    st.write("Click 'Show Filters' to display the filtering options.")
