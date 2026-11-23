import pandas as pd
import re

def load_products():
    return pd.read_csv("data/products.csv")


def search_product(search_text):
    products = load_products()

    # Convert customer message to lowercase
    search_text = search_text.lower()

    # Remove common question words
    remove_words = [
        "what", "is", "the", "price", "of",
        "do", "you", "have", "show", "me",
        "tell", "about", "please", "how", "much"
    ]

    # Clean the message
    search_text = re.sub(r"[^a-zA-Z0-9\s]", "", search_text)

    words = search_text.split()

    # Keep useful product and brand words
    keywords = [word for word in words if word not in remove_words]

    if not keywords:
        return products.iloc[0:0]

    # Search product name, category and brand
    searchable_data = (
        products["product_name"].fillna("").astype(str) + " " +
        products["brand"].fillna("").astype(str) + " " +
        products["category"].fillna("").astype(str)
    ).str.lower()

    # Match all useful keywords
    results = products[
        searchable_data.apply(
            lambda text: all(word in text for word in keywords)
        )
    ]

    return results