import requests
import pandas as pd


def get_user_location():
    """Fetch the user's location based on their IP address."""
    try:
        response = requests.get("https://ipinfo.io/json")
        data = response.json()
        return data["country"]
    except Exception as e:
        return None


def load_data(file_path):
    """Load the news data from a CSV file."""
    return pd.read_csv(file_path)


def filter_news(df, country=None, source=None, category=None):
    """Filter the news DataFrame based on user selections."""
    if country and country != "---":
        df = df[df["country"] == country]
    if source and source != "---":
        df = df[df["source"] == source]
    if category and category != "---":
        df = df[df["category"] == category]
    return df
