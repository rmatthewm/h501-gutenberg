from gutenberg_pkg.utils import load_data

def list_authors(by_languages=True, alias=True):
    df = load_data()

    if alias:
        df = df.dropna(subset=["alias"])
        df = df[df["alias"].str.strip() != ""]
        col = "alias"
    else:
        col = "author"

    if by_languages:
        counts = df.groupby(col)["gutenberg_id"].count()
        counts = counts.sort_values(ascending=False)
        return counts.index.tolist()

    return df[col].dropna().drop_duplicates().tolist()


