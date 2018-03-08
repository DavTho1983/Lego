"""all csvs from https://rebrickable.com/downloads/"""

import pandas as pd
import matplotlib.pyplot as plt

themes = pd.read_csv('themes.csv')
colors = pd.read_csv('colors.csv')
sets = pd.read_csv('sets.csv')


# print(themes.head())
#
# num_themes = themes.groupby('name')['id'].nunique().count()
# print('There are ' + str(num_themes) + ' themes in the technic lego range')
#
# colors_summary = colors.groupby('is_trans').count()
# print(colors_summary)

print(sets.head())
"""average parts by year"""
parts_by_year = sets[['year', 'num_parts']].mean(axis=1)
# print(parts_by_year)
# plt.plot(parts_by_year)
# plt.show()

# themes_by_year: Number of themes shipped by year
themes_by_year = sets[['year', 'theme_id']].groupby('year', as_index = False).agg({"theme_id": pd.Series.count})
print(themes_by_year.head())
