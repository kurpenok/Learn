#! /usr/bin/env python3

import pandas as pd

reviews = pd.read_csv(
    "../input/wine-reviews/winemag-data-130k-v2.csv",
    index_col=0)

desc = reviews.description

first_description = reviews.description[0]

first_row = reviews.iloc[0]

first_descriptions = reviews.description.iloc[:10]

sample_reviews = reviews.iloc[[1, 2, 3, 5, 8]]

cols = ['country', 'province', 'region_1', 'region_2']
indices = [0, 1, 10, 100]
df = reviews.loc[indices, cols]

df = reviews.loc[:99, ["country", "variety"]]

italian_wines = reviews[reviews.country == "Italy"]

top_oceania_wines = reviews[(reviews.points >= 95) & (reviews.country.isin(["Australia", "New Zealand"]))]
