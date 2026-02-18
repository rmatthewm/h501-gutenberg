import pandas as pd 
import __init__

def get_merged_data():
    # Merge the databases using the indices they have in common
    languages_metadata = pd.merge(__init__.gutenberg_languages, __init__.gutenberg_metadata, on='gutenberg_id')
    return pd.merge(languages_metadata, __init__.gutenberg_authors, on='gutenberg_author_id')
