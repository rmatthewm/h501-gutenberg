import pandas as pd 
from tt_gutenberg.__init__ import *

def get_merged_data():
    """ Merges the databases loaded by __init__ into a single dataframe

    Returns:
        pandas.DataFrame: a pandas dataframe with the merged data 
    """

    # Merge the databases using the indices they have in common
    languages_metadata = pd.merge(gutenberg_languages, gutenberg_metadata, on='gutenberg_id')
    return pd.merge(languages_metadata, gutenberg_authors, on='gutenberg_author_id')
