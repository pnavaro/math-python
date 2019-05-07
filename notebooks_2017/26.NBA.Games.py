# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python (math-python)
#     language: python
#     name: math-python
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ###  NBA Games

# %% {"slideshow": {"slide_type": "slide"}}
import os, sys
from glob import glob
import pandas as pd

raw_data = {}
for year in range(2000,2017):

    fp = os.path.join("../data", f"nba-{year}.csv")

    if not os.path.exists(fp):
        url = f"http://www.basketball-reference.com/leagues/NBA_{year}_games.html"
        tables = pd.read_html(url)
        games = tables[0]
        games.to_csv(fp)
        raw_data[str(year)] = games
    else:
        raw_data[str(year)] = pd.read_csv(fp)

# %%
raw_data['2008'].head()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# As you can see, we have some extra rows of mostly NaNs, the column names aren't useful, and we have some dtypes to fix up.

# %%
%%time 
seasons = {}
for year, games in raw_data.items():
    
    column_names = {'Date': 'date', 'Start (ET)': 'start',
                'Unamed: 2': 'box', 'Visitor/Neutral': 'away_team', 
                'PTS': 'away_points', 'Home/Neutral': 'home_team',
                'PTS.1': 'home_points', 'Unamed: 7': 'n_ot'}

    seasons[str(year)] = (games.rename(columns=column_names)
        .dropna(thresh=4)
        [['date', 'away_team', 'away_points', 'home_team', 'home_points']]
        .assign(date=lambda x: pd.to_datetime(x['date'], format='%a, %b %d, %Y'))
        .set_index('date', append=True)
        .rename_axis(["game_id", "date"])
        .sort_index())
    

# %%
seasons['2014']

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# - `dropna` has a thresh argument. If at least thresh items are missing, the row is dropped. We used it to remove the "Month headers" that slipped into the table.
# - `assign` can take a callable. This lets us refer to the DataFrame in the previous step of the chain. Otherwise we would have to assign temp_df = games.dropna()... And then do the pd.to_datetime on that.
# -`set_index` has an append keyword. We keep the original index around since it will be our unique identifier per game.
# - `.rename_axis` is used to set the index names.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### How many days of rest did each team get between each game?
#

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# In this case, an observation is a (team, game) pair, which we don't have yet. Rather, we have two observations per row, one for home and one for away. We'll fix that with `pd.melt`.
#
# `pd.melt` works by taking observations that are spread across columns (away_team, home_team), and melting them down into one column with multiple rows. However, we don't want to lose the metadata (like game_id and date) that is shared between the observations. By including those columns as id_vars, the values will be repeated as many times as needed to stay with their observations.

# %%
%%time
tidy = {}
for year, games in seasons.items():
    tidy[str(year)] = pd.melt(games.reset_index(),
               id_vars=['game_id', 'date'], value_vars=['away_team', 'home_team'],
               value_name='team')

# %% {"slideshow": {"slide_type": "slide"}}
tidy['2014'].groupby('team')['date'].diff().dt.days - 1

# %%
tidy['2010'].groupby('team')['date'].diff().dt.days - 1

# %%
tidy['2010']['rest'] = tidy['2010'].sort_values('date').groupby('team').date.diff().dt.days - 1

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # References
# * [Modern Pandas (Part 5): Tidy Data by T. Augspurger](https://tomaugspurger.github.io/modern-5-tidy)
#
