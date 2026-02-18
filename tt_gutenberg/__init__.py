import pandas as pd
import os

# Save time for testing by storing the data locally
# Filenames
AUTHORS_FILE = 'gb_authors'
LANGUAGES_FILE = 'gb_languages'
METADATA_FILE = 'gb_metadata'
SUBJECTS_FILE = 'gb_subjects'

if os.path.isfile(f'{AUTHORS_FILE}.csv'):
    gutenberg_authors = pd.read(f'{AUTHORS_FILE}.csv')
else:
    gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    gutenberg_authors.to_csv(f'{AUTHORS_FILE}.csv')


gutenberg_languages = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
gutenberg_subjects = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')

