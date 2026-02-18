import pandas as pd
import data_merge


def list_authors(by_languages=False, by_alias=False):
    # Get the merged data
    df_gutenberg = data_merge.get_merged_data()

    # Sort the authors by language if requested
    if by_languages:
        df_gutenberg.sort_values(by='total_languages')
        print(df_gutenberg.groupby('gutenberg_author_id')['author_x'])

    print(list(df_gutenberg['author_x']))

list_authors(by_languages=True)    
