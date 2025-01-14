import pandas as pd
import re
import html
import http.client
import urllib.parse
import pycountry
import os
from datetime import datetime


# ------------------------------
# General DataFrame Info Functions
# ------------------------------


def show_data_types(df):
    """
    Show data types of all columns in the DataFrame.

    """
    print("Data Types of Columns:")
    print(df.dtypes)


def show_missing_values(df):
    """
    Show the number of missing values per column.

    """
    print("\nMissing Values in Columns:")
    print(df.isnull().sum())


def show_basic_info(df):
    """
    Show basic information about the DataFrame including shape, dtypes, and missing values.

    """
    print(f"\nDataFrame Shape: {df.shape}")
    print(f"Number of Rows: {df.shape[0]}")
    print(f"Number of Columns: {df.shape[1]}")
    print("\nData Types of Columns:")
    print(df.dtypes)
    print("\nMissing Values per Column:")
    print(df.isnull().sum())
    print("\nFirst 5 Rows of Data:")
    print(df.head())


def show_null_percentage(df):
    """
    Show percentage of missing values in each column.

    """
    null_percentage = df.isnull().mean() * 100
    print("\nPercentage of Missing Values in Each Column:")
    print(null_percentage)


# ------------------------------
# Column-Specific Functions
# ------------------------------


def show_column_summary(df):
    """
    Show summary statistics for all columns.

    """
    print("\nSummary Statistics for All Columns:")
    print(df.describe(include="all"))


def show_column_values(df, column_name):
    """
    Show unique values for a specific column.

    """
    if column_name in df.columns:
        print(f"\nUnique values in column {column_name}:")
        print(df[column_name].unique())
    else:
        print(f"Column {column_name} does not exist in the DataFrame.")


def show_column_value_counts(df, column_name):
    """
    Show value counts for a specific column.

    """
    if column_name in df.columns:
        print(f"\nValue counts for column {column_name}:")
        print(df[column_name].value_counts())
    else:
        print(f"Column {column_name} does not exist in the DataFrame.")


def show_column_info(df, column_name):
    """
    Show detailed information about a specific column.

    """
    if column_name in df.columns:
        print(f"\nColumn Info for {column_name}:")
        print(f"Data Type: {df[column_name].dtype}")
        print(f"Number of Unique Values: {df[column_name].nunique()}")
        print(f"Number of Missing Values: {df[column_name].isnull().sum()}")
        print(f"Unique Values:")
        print(df[column_name].unique())
    else:
        print(f"Column {column_name} does not exist in the DataFrame.")


# ------------------------------
# Data Quality Functions
# ------------------------------


def check_for_duplicates(df):
    """
    Check for duplicate rows in the DataFrame.

    """
    duplicates = df.duplicated().sum()
    if duplicates > 0:
        print(f"\nThere are {duplicates} duplicate rows in the DataFrame.")
    else:
        print("\nNo duplicate rows found in the DataFrame.")


# ------------------------------
# Data Cleaning Functions
# ------------------------------


def remove_duplicates(df):
    """
    Remove duplicate rows from a DataFrame.

    """
    before_count = len(df)
    df = df.drop_duplicates()
    after_count = len(df)
    removed_count = before_count - after_count
    print(f"Removed {removed_count} duplicate rows.")
    return df


def drop_empty_rows(df):
    """
    Cleans the DataFrame by removing rows with missing values and reports the number of rows removed.

    """
    original_row_count = df.shape[0]
    df = df.dropna()
    cleaned_row_count = df.shape[0]

    rows_removed = original_row_count - cleaned_row_count
    print(f"Rows removed: {rows_removed}")

    return df, rows_removed


def drop_empty_rows_from_column(df, column_name):
    """
    Drops rows where the specified column has missing values and returns the updated DataFrame.
    Also prints the number of rows deleted.

    """
    initial_rows = len(df)
    df = df.dropna(subset=[column_name])

    deleted_rows = initial_rows - len(df)
    print(f"Number of rows deleted: {deleted_rows}")

    return df


# ------------------------------
# Column Renaming and Standardization Functions
# ------------------------------


def rename_columns(df, rename_dict):
    """
    Rename columns based on a dictionary.

    """
    return df.rename(columns=rename_dict)


def standardize_column_names(df):
    """
    Standardize column names (lowercase, replace spaces with underscores, and convert camelCase to snake_case).

    """

    def camel_to_snake(name):
        return re.sub(
            r"([a-z0-9])([A-Z])", r"\1_\2", name
        ).lower()  # underscore before uppercase letters

    df.columns = [
        camel_to_snake(col.strip().replace(" ", "_")) for col in df.columns
    ]  # apply all transformations

    return df


# ------------------------------
# Data Type Conversion Functions
# ------------------------------


def convert_strings_to_lowercase(df, column_name):
    """
    Converts all string entries in a specified column of a DataFrame to lowercase,
    ensures there is a space after any comma in the strings, removes quote marks,
    and adjusts commas according to the specified conditions.

    """
    if column_name in df.columns and df[column_name].dtype in ["object", "string"]:
        df[column_name] = df[column_name].map(
            lambda x: (
                (
                    x.lower()
                    .replace('"', "")
                    .lstrip(",")
                    .replace(", ", ",")
                    .replace(",", ", ")
                )
                if isinstance(x, str)
                else x
            )
        )
    else:
        raise ValueError(
            f"Column '{column_name}' does not exist or is not of type object/string."
        )
    return df


def convert_columns_to_int(df, columns):
    """
    Converts specified columns in the DataFrame to Int64 type, handling errors gracefully.

    """
    columns_to_convert = [col for col in columns if col in df.columns]

    df[columns_to_convert] = (
        df[columns_to_convert].apply(pd.to_numeric, errors="coerce").astype("Int64")
    )  # convert to int, handle errors

    return df


# ------------------------------
# Other Functions
# ------------------------------


def clean_source_names(source):
    source = html.unescape(source)  # decode HTML entities
    source = re.sub(
        r"\.(com|net|org|info|cu|gb|au|de|fr|es|it|ca|us)$",
        "",
        source,
        flags=re.IGNORECASE,
    )
    source = source.replace("_", " ")  # replace underscores
    source = re.sub(r"[^\w\s-]", "", source)  # remove unwanted characters
    source = source.title()  # capitalize each word
    source = re.sub(r"\s+", " ", source).strip()  # remove extra spaces
    return source


def clean_text(text):
    """
    Clean and standardize the text by first removing links, then unwanted characters
    and patterns, including website references, query parameters, HTML entities, square brackets,
    and more.

    Args:
        text (str): The input string (text).

    Returns:
        str: The cleaned text.
    """
    text = re.sub(r"https?://\S+|www\.\S+", "", text)  # remove URLs

    text = re.sub(r"\(.*?\)", "", text)  # remove parentheses

    text = re.sub(r"\[.*?\]", "", text)  # remove square brackets

    text = re.sub(r"[\\/]", " ", text)  # remove slashes

    text = re.sub(r"[\u2013\u2014\u2212]", "-", text)  # remove hyphens

    text = re.sub(r"[-]{2,}", "-", text)  # remove double hyphens

    text = re.sub(r"\?[\w&=.-]*", "", text)  # remove query parameters

    text = re.sub(
        r"&[a-zA-Z#0-9]+;", "", text
    )  # remove HTML entities (e.g., &nbsp;, &amp;)

    text = re.sub(r"<.*?>", "", text)  # remove HTML tags

    text = re.sub(r"\s+", " ", text)  # remove extra spaces

    text = text.strip()  # trim leading and trailing spaces

    text = re.sub(r"^['\"']+|['\"']+$", "", text)  # remove quote marks

    return text


def fetch_news():
    """
    Fetch news from the MediaStack API.

    """
    conn = http.client.HTTPConnection("api.mediastack.com")

    params = urllib.parse.urlencode(
        {
            "access_key": os.getenv("MEDIASTACK_API_KEY"),  # Use the API key from .env
            "categories": "-general,-sports",
            "sort": "published_desc",
            "limit": 10,
        }
    )

    conn.request("GET", "/v1/news?{}".format(params))

    res = conn.getresponse()
    data = res.read()

    return data.decode("utf-8")


def format_response_data(input_data):
    """
    Format the response data from the MediaStack API.

    """
    input_data["published_at"] = datetime.strptime(
        input_data["published_at"],
        "%Y-%m-%dT%H:%M:%S+00:00",  # convert date to YYYY-MM-DD format
    ).strftime("%Y-%m-%d")

    language = pycountry.languages.get(
        alpha_2=input_data["language"]
    )  # get language name
    input_data["language"] = language.name if language else input_data["language"]

    country = pycountry.countries.get(alpha_2=input_data["country"])  # get country name
    input_data["country"] = country.name if country else input_data["country"]

    return input_data
