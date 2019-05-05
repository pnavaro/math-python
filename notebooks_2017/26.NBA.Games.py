#!/usr/bin/env python
# coding: utf-8

# ###  NBA Games

# In[1]:


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


# In[2]:


raw_data['2008'].head()


# As you can see, we have some extra rows of mostly NaNs, the column names aren't useful, and we have some dtypes to fix up.

# In[3]:


get_ipython().run_cell_magic('time', '', 'seasons = {}\nfor year, games in raw_data.items():\n    \n    column_names = {\'Date\': \'date\', \'Start (ET)\': \'start\',\n                \'Unamed: 2\': \'box\', \'Visitor/Neutral\': \'away_team\', \n                \'PTS\': \'away_points\', \'Home/Neutral\': \'home_team\',\n                \'PTS.1\': \'home_points\', \'Unamed: 7\': \'n_ot\'}\n\n    seasons[str(year)] = (games.rename(columns=column_names)\n        .dropna(thresh=4)\n        [[\'date\', \'away_team\', \'away_points\', \'home_team\', \'home_points\']]\n        .assign(date=lambda x: pd.to_datetime(x[\'date\'], format=\'%a, %b %d, %Y\'))\n        .set_index(\'date\', append=True)\n        .rename_axis(["game_id", "date"])\n        .sort_index())\n    ')


# In[4]:


seasons['2014']


# - `dropna` has a thresh argument. If at least thresh items are missing, the row is dropped. We used it to remove the "Month headers" that slipped into the table.
# - `assign` can take a callable. This lets us refer to the DataFrame in the previous step of the chain. Otherwise we would have to assign temp_df = games.dropna()... And then do the pd.to_datetime on that.
# -`set_index` has an append keyword. We keep the original index around since it will be our unique identifier per game.
# - `.rename_axis` is used to set the index names.

# ### How many days of rest did each team get between each game?
# 

# In this case, an observation is a (team, game) pair, which we don't have yet. Rather, we have two observations per row, one for home and one for away. We'll fix that with `pd.melt`.
# 
# `pd.melt` works by taking observations that are spread across columns (away_team, home_team), and melting them down into one column with multiple rows. However, we don't want to lose the metadata (like game_id and date) that is shared between the observations. By including those columns as id_vars, the values will be repeated as many times as needed to stay with their observations.

# In[5]:


get_ipython().run_cell_magic('time', '', "tidy = {}\nfor year, games in seasons.items():\n    tidy[str(year)] = pd.melt(games.reset_index(),\n               id_vars=['game_id', 'date'], value_vars=['away_team', 'home_team'],\n               value_name='team')")


# In[6]:


tidy['2014'].groupby('team')['date'].diff().dt.days - 1


# In[7]:


tidy['2010'].groupby('team')['date'].diff().dt.days - 1


# In[8]:


tidy['2010']['rest'] = tidy['2010'].sort_values('date').groupby('team').date.diff().dt.days - 1


# # References
# * [Modern Pandas (Part 5): Tidy Data by T. Augspurger](https://tomaugspurger.github.io/modern-5-tidy)
# 
