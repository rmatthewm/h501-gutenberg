import pandas as pd
import data_merge


def list_authors(by_languages=False, by_alias=False):
    """ Returns the authors in the Gutenberg database as a list

    Args:
        by_languages (bool, optional): sorts the authors by the number of 
            languages their works are in. Defaults to False.
        by_alias (bool, optional): returns all the authors' aliases instead of just their name. Defaults to False.

    Returns:
        list(str): the list of authors
    """

    # Get the merged data
    df_gutenberg = data_merge.get_merged_data()
    not_na = df_gutenberg.notna()

    # Sort the authors by language if requested, then by alias
    if by_languages:
        if by_alias:
            return list(df_gutenberg[not_na].sort_values(by='total_languages')['aliases'].unique())
        else:
            return list(df_gutenberg[not_na].sort_values(by='total_languages')['author_x'].unique())
    else:

        if by_alias:
            return list(df_gutenberg[not_na]['aliases'].unique())
        else:
            return list(df_gutenberg[not_na]['author_x'].unique())
