import pandas as pd
from tt_gutenberg.data_merge import *


def list_authors(by_languages=False, alias=False):
    """ Returns the authors in the Gutenberg database as a list

    Args:
        by_languages (bool, optional): sorts the authors by the number of 
            languages their works are in. Defaults to False.
        alias (bool, optional): returns all the authors' aliases instead of just their name. Defaults to False.

    Returns:
        list(str): the list of authors
    """

    # Get the merged data
    df_gutenberg = get_merged_data()
    alias_not_na = df_gutenberg['alias'].notna()
    author_not_na = df_gutenberg['author_x'].notna()

    # Sort the authors by language if requested, then by alias
    if by_languages:
        if alias:
            return list(df_gutenberg[alias_not_na].sort_values(by='total_languages')['aliases'].unique())
        else:
            return list(df_gutenberg[author_not_na].sort_values(by='total_languages')['author_x'].unique())
    else:

        if alias:
            return list(df_gutenberg[alias_not_na]['aliases'].unique())
        else:
            return list(df_gutenberg[author_not_na]['author_x'].unique())
