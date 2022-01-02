import pandas as pd
pd.set_option("display.max_rows", 5)
reviews = pd.read_csv("../input/wine-reviews/winemag-data-130k-v2.csv", index_col=0)

from learntools.core import binder; binder.bind(globals())
from learntools.pandas.summary_functions_and_maps import *
print("Setup complete.")

reviews.head()

median_points = reviews["points"].median()

countries = set(reviews["country"])

reviews_per_country = reviews.country.value_counts()

centered_price = reviews.price.map(lambda p: p - reviews.price.mean())

bargain_wine = reviews.title[reviews.apply(lambda row: row.points / row.price, axis="columns").idxmax()]

descriptor_counts = pd.Series([reviews.description.map(lambda x: "tropical" in x).sum(), reviews.description.map(lambda x: "fruity" in x).sum()], index=['tropical', 'fruity'])

def get_star(row) -> int:
    if row.points >= 95:
        return 3
    elif 95 > row.points >= 85:
        return 2
    else:
        return 1


star_ratings = reviews.apply(get_star, axis="columns")

