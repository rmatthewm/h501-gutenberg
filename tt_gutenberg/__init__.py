import pandas as pd
import os

# Save time for testing by storing the data locally
# Filenames
AUTHORS_FILE = 'gb_authors'
LANGUAGES_FILE = 'gb_languages'
METADATA_FILE = 'gb_metadata'
SUBJECTS_FILE = 'gb_subjects'

# Load the data, if not saved locally, save it to reduce runtime in the future
if os.path.isfile(f'{AUTHORS_FILE}.csv'):
    gutenberg_authors = pd.read_csv(f'{AUTHORS_FILE}.csv')
else:
    gutenberg_authors = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_authors.csv')
    gutenberg_authors.to_csv(f'{AUTHORS_FILE}.csv')

if os.path.isfile(f'{LANGUAGES_FILE}.csv'):
    gutenberg_languages = pd.read_csv(f'{LANGUAGES_FILE}.csv')
else:
    gutenberg_languages = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_languages.csv')
    gutenberg_languages.to_csv(f'{LANGUAGES_FILE}.csv', index=False)

if os.path.isfile(f'{METADATA_FILE}.csv'):
    gutenberg_metadata = pd.read_csv(f'{METADATA_FILE}.csv')
else:
    gutenberg_metadata = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_metadata.csv')
    gutenberg_metadata.to_csv(f'{METADATA_FILE}.csv', index=False)

if os.path.isfile(f'{SUBJECTS_FILE}.csv'):
    gutenberg_subjects = pd.read_csv(f'{SUBJECTS_FILE}.csv')
else:
    gutenberg_subjects = pd.read_csv('https://raw.githubusercontent.com/rfordatascience/tidytuesday/main/data/2025/2025-06-03/gutenberg_subjects.csv')
    gutenberg_subjects.to_csv(f'{SUBJECTS_FILE}.csv', index=False)

