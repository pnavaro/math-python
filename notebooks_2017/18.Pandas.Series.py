# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.2.3
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ![pandas](http://pandas.pydata.org/_static/pandas_logo.png "Pandas Logo")
#
#
# - Started by Wes MacKinney with a first release in 2011.
# - Based on NumPy, it is the most used library for all things data.
# - Motivated by the toolbox in R for manipulating data easily.
# - A lot of names in Pandas come from R world.
# - It is Open source (BSD)
#
# https://pandas.pydata.org/

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Pandas 
#
# ```python
# import pandas as pd
# ```
#
# "*Pandas provides high-performance, easy-to-use data structures 
# and data analysis tools in Python*"
#
# - Self-describing data structures
# - Data loaders to/from common file formats
# - Plotting functions
# - Basic statistical tools.
#

# %% {"slideshow": {"slide_type": "slide"}}
%matplotlib inline  
%config InlineBackend.figure_format = 'retina'
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# %% {"slideshow": {"slide_type": "slide"}}
sns.set()
pd.set_option("display.max_rows", 8)
plt.rcParams['figure.figsize'] = (9, 6)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # [Series](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#series)
#
# - A Series contains a one-dimensional array of data, *and* an associated sequence of labels called the *index*.
# - The index can contain numeric, string, or date/time values.
# - When the index is a time value, the series is a [time series](https://en.wikipedia.org/wiki/Time_series).
# - The index must be the same length as the data.
# - If no index is supplied it is automatically generated as `range(len(data))`.

# %% {"slideshow": {"slide_type": "fragment"}}
pd.Series([1,3,5,np.nan,6,8])

# %% {"slideshow": {"slide_type": "slide"}}
pd.Series(index=pd.period_range('09/11/2017', '09/18/2017', freq="D"))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
# - Create a text with `lorem` and count word occurences with a `collection.Counter`. Put the result in a `dict`.

# %% {"slideshow": {"slide_type": "fragment"}}
import lorem 
from collections import Counter
import operator

text = lorem.text()
text

# %% {"slideshow": {"slide_type": "fragment"}}
c = Counter(filter(None,text.strip().replace('.','').replace('\n',' ').lower().split(' ')))
result = dict(sorted(c.most_common(),key=operator.itemgetter(1),reverse=True))
result

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
# - From the results create a Pandas series name latin_series with words in alphabetical order as index.

# %% {"slideshow": {"slide_type": "fragment"}}
df = pd.Series(result)
df

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# - Plot the series using 'bar' kind.

# %% {"slideshow": {"slide_type": "fragment"}}
df.plot(kind='bar')

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# ### Exercise
# - Pandas provides explicit functions for indexing `loc` and `iloc`.
#     - Use `loc` to display the number of occurrences of 'dolore'.
#     - Use `iloc` to diplay the number of occurrences of the last word in index.

# %%
df.loc['dolore'], df['dolore'], df.dolore

# %%
df.iloc[-1], df[-1], df[df.keys()[-1]]

# %% [markdown]
# ### Exercise
# - Sort words by number of occurrences.
# - Plot the Series.

# %%
df = df.sort_values()
df.plot(kind='bar')

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Full globe temperature between 1901 and 2000.
#
# We read the text file and load the results in a pandas dataframe. 
# In cells below you need to clean the data and convert the dataframe to a time series.

# %% {"slideshow": {"slide_type": "fragment"}}
import os
here = os.getcwd()

filename = os.path.join(here,"../data","monthly.land.90S.90N.df_1901-2000mean.dat.txt")

df = pd.read_table(filename, sep="\s+", 
                   names=["year", "month", "mean temp"])
df

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
# - Insert a third column with value one named "day" with `.insert`.
# - convert df index to datetime with `pd.to_datetime` function.
# - convert df to Series containing only "mean temp" column.

# %% {"slideshow": {"slide_type": "fragment"}}
df.insert(loc=2,column='day',value=1)
df

# %% {"slideshow": {"slide_type": "slide"}}
df.index = pd.to_datetime(df[['year','month','day']])
df

# %% {"slideshow": {"slide_type": "slide"}}
df = df['mean temp']
df

# %% {"slideshow": {"slide_type": "fragment"}}
type(df)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 
# - Display the beginning of the file with `.head`.

# %%
df.head()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 
# - Display the end of the file with `.tail`.

# %% {"slideshow": {"slide_type": "fragment"}}
df.tail()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# In the dataset, -999.00 was used to indicate that there was no value for that year.
#
# ### Exercise
#
# - Display values equal to -999 with `.values`. 
# - Replace the missing value (-999.000) by `np.nan` 
#

# %% {"slideshow": {"slide_type": "fragment"}}
df[df.values == -999]

# %%
pd.__version__

# %%

# %% {"slideshow": {"slide_type": "slide"}}
df2 = df.copy() 
df2[df == -999.0] = np.nan  # For this indexing we need a copy
df2.tail()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
#
# Once they have been converted to np.nan, missing values can be removed (dropped).
#
# ### Exercise 
# - Remove missing values with `.dropna`.

# %% {"slideshow": {"slide_type": "fragment"}}
df = df2.dropna()
df.tail()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
# - Generate a basic visualization using `.plot`.

# %% {"slideshow": {"slide_type": "fragment"}}
df.plot();

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# Convert df index from timestamp to period is more meaningfull since it was measured and averaged over the month. Use `to_period` method.
#

# %% {"slideshow": {"slide_type": "fragment"}}
df = df.to_period('M')
df

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Resampling
#
# Series can be resample, downsample or upsample.
# - Frequencies can be specified as strings: "us", "ms", "S", "T", "H", "D", "B", "W", "M", "A", "3min", "2h20", ...
# - More aliases at http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
#
# ### Exercise
#
# - With `resample` method, convert df Series to 10 year blocks:

# %%
df.resample('10A').mean()


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Rolling mean

# %% {"slideshow": {"slide_type": "fragment"}}
s = df.resample('10A')
s

# %% {"slideshow": {"slide_type": "slide"}}
r = df.rolling(window=120).mean().dropna()
type(r)

# %%
?pd.Series.rolling

# %%

# %%

# %% {"slideshow": {"slide_type": "fragment"}}
plt.figure()
s.plot(style='y.')
r.plot(style='r')

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Saving Work

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# Excel Writer does not work with Series.

# %% {"slideshow": {"slide_type": "fragment"}}
with pd.ExcelWriter("../data/test.xls") as writer:
    pd.DataFrame({"Full Globe Temperature": df}).to_excel(writer, sheet_name="Full Globe Temperature")

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# [HDF5](https://support.hdfgroup.org/HDF5/) is widely used and one of the most powerful file format to store binary data. It allows to store both Series and DataFrames.

# %% {"slideshow": {"slide_type": "fragment"}}
with pd.HDFStore("../data/pandas_series.h5") as writer:
    df.to_hdf(writer, "/temperatures/full_globe")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Reloading data

# %% {"slideshow": {"slide_type": "fragment"}}
with pd.HDFStore("../data/pandas_series.h5") as store:
    df = store["/temperatures/full_globe"]
