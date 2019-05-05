#!/usr/bin/env python
# coding: utf-8

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

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


sns.set()
pd.set_option("display.max_rows", 8)
plt.rcParams['figure.figsize'] = (9, 6)


# # [Series](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#series)
# 
# - A Series contains a one-dimensional array of data, *and* an associated sequence of labels called the *index*.
# - The index can contain numeric, string, or date/time values.
# - When the index is a time value, the series is a [time series](https://en.wikipedia.org/wiki/Time_series).
# - The index must be the same length as the data.
# - If no index is supplied it is automatically generated as `range(len(data))`.

# In[3]:


pd.Series([1,3,5,np.nan,6,8])


# In[4]:


pd.Series(index=pd.period_range('09/11/2017', '09/18/2017', freq="D"))


# ### Exercise
# - Create a text with `lorem` and count word occurences with a `collection.Counter`. Put the result in a `dict`.

# In[5]:


import lorem 
from collections import Counter
import operator

text = lorem.text()
text


# In[6]:


c = Counter(filter(None,text.strip().replace('.','').replace('\n',' ').lower().split(' ')))
result = dict(sorted(c.most_common(),key=operator.itemgetter(1),reverse=True))
result


# ### Exercise
# - From the results create a Pandas series name latin_series with words in alphabetical order as index.

# In[7]:


df = pd.Series(result)
df


# ### Exercise
# 
# - Plot the series using 'bar' kind.

# In[8]:


df.plot(kind='bar')


# ### Exercise
# - Pandas provides explicit functions for indexing `loc` and `iloc`.
#     - Use `loc` to display the number of occurrences of 'dolore'.
#     - Use `iloc` to diplay the number of occurrences of the last word in index.

# In[9]:


df.loc['dolore'], df['dolore'], df.dolore


# In[10]:


df.iloc[-1], df[-1], df[df.keys()[-1]]


# ### Exercise
# - Sort words by number of occurrences.
# - Plot the Series.

# In[11]:


df = df.sort_values()
df.plot(kind='bar')


# ### Full globe temperature between 1901 and 2000.
# 
# We read the text file and load the results in a pandas dataframe. 
# In cells below you need to clean the data and convert the dataframe to a time series.

# In[12]:


import os
here = os.getcwd()

filename = os.path.join(here,"../data","monthly.land.90S.90N.df_1901-2000mean.dat.txt")

df = pd.read_table(filename, sep="\s+", 
                   names=["year", "month", "mean temp"])
df


# ### Exercise
# - Insert a third column with value one named "day" with `.insert`.
# - convert df index to datetime with `pd.to_datetime` function.
# - convert df to Series containing only "mean temp" column.

# In[13]:


df.insert(loc=2,column='day',value=np.ones(len(df)))
df


# In[14]:


df.index = pd.to_datetime(df[['year','month','day']])
df


# In[15]:


df = df['mean temp']
df


# In[16]:


type(df)


# ### Exercise 
# - Display the beginning of the file with `.head`.

# In[17]:


df.head()


# ### Exercise 
# - Display the end of the file with `.tail`.

# In[18]:


df.tail()


# In the dataset, -999.00 was used to indicate that there was no value for that year.
# 
# ### Exercise
# 
# - Display values equal to -999 with `.values`. 
# - Replace the missing value (-999.000) by `np.nan` 
# 

# In[19]:


df[df.values == -999]


# In[20]:


df2 = df.copy() 
df2[df == -999.0] = np.nan  # For this indexing we need a copy
df2.tail()


# 
# Once they have been converted to np.nan, missing values can be removed (dropped).
# 
# ### Exercise 
# - Remove missing values with `.dropna`.

# In[21]:


df = df2.dropna()
df.tail()


# ### Exercise
# - Generate a basic visualization using `.plot`.

# In[22]:


df.plot();


# ### Exercise
# 
# Convert df index from timestamp to period is more meaningfull since it was measured and averaged over the month. Use `to_period` method.
# 

# In[23]:


df = df.to_period('M')
df


# ## Resampling
# 
# Series can be resample, downsample or upsample.
# - Frequencies can be specified as strings: "us", "ms", "S", "T", "H", "D", "B", "W", "M", "A", "3min", "2h20", ...
# - More aliases at http://pandas.pydata.org/pandas-docs/stable/timeseries.html#offset-aliases
# 
# ### Exercise
# 
# - With `resample` method, convert df Series to 10 year blocks:

# In[24]:


df.resample('10A').mean()


# # Rolling mean

# In[25]:


s = df.resample('10A')
s


# In[26]:


r = df.rolling(window=200).mean().dropna()
r


# In[27]:


s.plot(style='y.')
r.plot(style='r')


# # Saving Work

# Excel Writer does not work with Series.

# In[28]:


with pd.ExcelWriter("../data/test.xls") as writer:
    pd.DataFrame({"Full Globe Temperature": df}).to_excel(writer, sheet_name="Full Globe Temperature")


# [HDF5](https://support.hdfgroup.org/HDF5/) is widely used and one of the most powerful file format to store binary data. It allows to store both Series and DataFrames.

# In[29]:


with pd.HDFStore("../data/pandas_series.h5") as writer:
    df.to_hdf(writer, "/temperatures/full_globe")


# # Reloading data

# In[30]:


with pd.HDFStore("../data/pandas_series.h5") as store:
    df = store["/temperatures/full_globe"]

