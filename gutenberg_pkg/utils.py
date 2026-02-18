import pandas as pd

def load_data():
    gutenberg_authors = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv"
    )
    gutenberg_languages = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv"
    )
    gutenberg_metadata = pd.read_csv(
        "https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv"
    )

    df = pd.merge(gutenberg_languages, gutenberg_metadata, on="gutenberg_id")
    df = pd.merge(df, gutenberg_authors, on="gutenberg_author_id")

    return df
