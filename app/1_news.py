import streamlit as st
import pandas as pd
import requests


# Load CSS
def load_css():
    with open("app/styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


# Function to fetch the user's location based on their IP address
def get_user_location():
    """Fetch the user's location based on their IP address."""
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data["country"]
    except Exception as e:
        return None


# Function to load the news data from a CSV file
def load_data(file_path):
    """Load the news data from a CSV file."""
    return pd.read_csv(file_path)


# Function to filter the news DataFrame based on user selections
def filter_news(df, country=None, source=None, category=None):
    """Filter the news DataFrame based on user selections."""
    if country and country != "---":
        df = df[df["country"] == country]
    if source and source != "---":
        df = df[df["source"] == source]
    if category and category != "---":
        df = df[df["category"] == category]
    return df


# Function to extract the first few sentences from a description
def extract_sentences(text, num_sentences=2):
    """Extract the first few sentences from a given text based on periods."""
    # Find the positions of the periods
    period_indices = [i for i, char in enumerate(text) if char == "."]

    # If there are fewer periods than requested sentences, return the whole text
    if len(period_indices) < num_sentences:
        return text

    # Get the end index of the last sentence to include
    end_index = period_indices[num_sentences - 1] + 1  # Include the period
    return text[:end_index].strip()  # Return the text up to the end index


# Function to display news articles in the Streamlit app
def display_news(articles):
    """Display news articles in the Streamlit app."""
    for index, row in articles.iterrows():
        st.subheader(row["title"])
        description = extract_sentences(
            row["description"], num_sentences=2
        )  # Get first 2 sentences
        st.write(description)
        if pd.notna(row["url"]):  # Check if URL exists
            st.markdown(f"[Read full article]({row['url']})", unsafe_allow_html=True)


# Function to show news articles based on the user's location
def show_location_news(response_df):
    """Show news articles based on the user's location."""
    location_news = response_df[response_df["country"] == st.session_state.user_country]
    if not location_news.empty:
        st.write("News articles based on your location:")
        display_news(location_news.head(5))
    else:
        st.write("No news articles found for your location. Displaying random news.")


# Function to show random news articles
def show_random_news(response_df):
    """Show random news articles."""
    st.write("Displaying random news:")
    random_news = response_df.sample(n=5)
    display_news(random_news)


# Load the DataFrame
data_file_path = "data/clean/1_mediastack_news_cleaned.csv"
response_df = load_data(data_file_path)

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

# Show news based on location or random news
if "user_country" in st.session_state:
    show_location_news(response_df)
else:
    st.write("Location access not granted. Displaying random news.")
    show_random_news(response_df)

# Sidebar for filters
st.sidebar.header("Filter Options")
countries = ["---"] + response_df["country"].unique().tolist()
sources = ["---"] + response_df["source"].unique().tolist()
categories = ["---"] + [
    category.capitalize() for category in response_df["category"].unique().tolist()
]

selected_country = st.sidebar.selectbox("Select Country", countries)
selected_source = st.sidebar.selectbox("Select Source", sources)
selected_category = st.sidebar.selectbox("Select Category", categories)

# Filter news based on user selections
filtered_news = filter_news(
    response_df, selected_country, selected_source, selected_category
)

# Display top news articles based on filters
if not filtered_news.empty:
    st.sidebar.write("Filtered news articles:")
    display_news(filtered_news.head(5))
else:
    st.sidebar.write("No news articles found for the selected filters.")
