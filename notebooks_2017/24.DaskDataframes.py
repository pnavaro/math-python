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
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %% {"slideshow": {"slide_type": "skip"}}
import pandas as pd
pd.set_option("max.rows", 8)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Dask DataFrames
#
# Dask dataframes look and feel (mostly) like Pandas dataframes but they run on the same infrastructure that powers dask.delayed.
#
# The `dask.dataframe` module implements a blocked parallel `DataFrame` object that mimics a large subset of the Pandas `DataFrame`. One dask `DataFrame` is comprised of many in-memory pandas `DataFrames` separated along the index. One operation on a dask `DataFrame` triggers many pandas operations on the constituent pandas `DataFrame`s in a way that is mindful of potential parallelism and memory constraints.
#
# **Related Documentation**
#
# *  [Dask DataFrame documentation](http://dask.pydata.org/en/latest/dataframe.html)
# *  [Pandas documentation](http://pandas.pydata.org/)
#
# In this notebook, we will extracts some historical flight data for flights out of NYC between 1990 and 2000. The data is taken from [here](http://stat-computing.org/dataexpo/2009/the-data.html). This should only take a few seconds to run.
#
# We will use `dask.dataframe` construct our computations for us.  The `dask.dataframe.read_csv` function can take a globstring like `"data/nycflights/*.csv"` and build parallel computations on all of our data at once.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Prep the Data

# %% {"slideshow": {"slide_type": "fragment"}}
import os  # library to get directory and file paths
import tarfile # this module makes possible to read and write tar archives

def extract_flight():
    flightdir = os.path.join('../data', 'nycflights')
    if not os.path.exists(flightdir):
       print("Extracting flight data")
       tar_path = os.path.join('../data', 'nycflights.tar.gz')
       with tarfile.open(tar_path, mode='r:gz') as flights:
          flights.extractall('../data/')
            
extract_flight() # this function call will extract 10 csv files in data/nycflights

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Load Data from CSVs in Dask Dataframes

# %% {"slideshow": {"slide_type": "fragment"}}
import os
filename = os.path.join('../data', 'nycflights', '*.csv')
filename

# %% {"slideshow": {"slide_type": "fragment"}}
import dask
import dask.dataframe as dd

df = dd.read_csv(filename,
                 parse_dates={'Date': [0, 1, 2]})

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Let's take a look to the dataframe

# %% {"slideshow": {"slide_type": "fragment"}}
df

# %% {"slideshow": {"slide_type": "slide"}}
# Get the first 5 rows
df.head()

# %% {"slideshow": {"slide_type": "slide"}}
# Get the last 5 rows
import traceback
try:
    df.tail()
except: 
    traceback.print_exc()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### What just happened?
#
# Unlike `pandas.read_csv` which reads in the entire file before inferring datatypes, `dask.dataframe.read_csv` only reads in a sample from the beginning of the file (or first file if using a glob). These inferred datatypes are then enforced when reading all partitions.
#
# In this case, the datatypes inferred in the sample are incorrect. The first `n` rows have no value for `CRSElapsedTime` (which pandas infers as a `float`), and later on turn out to be strings (`object` dtype). When this happens you have a few options:
#
# - Specify dtypes directly using the `dtype` keyword. This is the recommended solution, as it's the least error prone (better to be explicit than implicit) and also the most performant.
# - Increase the size of the `sample` keyword (in bytes)
# - Use `assume_missing` to make `dask` assume that columns inferred to be `int` (which don't allow missing values) are actually floats (which do allow missing values). In our particular case this doesn't apply.
#
# In our case we'll use the first option and directly specify the `dtypes` of the offending columns. 

# %% {"slideshow": {"slide_type": "slide"}}
df.dtypes

# %% {"slideshow": {"slide_type": "slide"}}
df = dd.read_csv(filename,
                 parse_dates={'Date': [0, 1, 2]},
                 dtype={'TailNum': str,
                        'CRSElapsedTime': float,
                        'Cancelled': bool})

# %% {"slideshow": {"slide_type": "slide"}}
df.tail()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Let's take a look at one more example to fix ideas.

# %% {"slideshow": {"slide_type": "fragment"}}
len(df)

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# ### Why df is ten times longer ?

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# - Dask investigated the input path and found that there are ten matching files. 
# - A set of jobs was intelligently created for each chunk - one per original CSV file in this case. 
# - Each file was loaded into a pandas dataframe, had `len()` applied to it.
# - The subtotals were combined to give you the final grant total.

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Computations with `dask.dataframe`
#
# We compute the maximum of the `DepDelay` column.  With `dask.delayed` we could create this computation as follows:
#
# ```python
# maxes = []
# for fn in filenames:
#     df = dask.delayed(pd.read_csv)(fn)
#     maxes.append(df.DepDelay.max())
#     
# final_max = dask.delayed(max)(maxes)
# final_max.compute()
# ```
#
# Now we just use the normal Pandas syntax as follows:

# %% {"slideshow": {"slide_type": "fragment"}}
%time df.DepDelay.max().compute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# This writes the delayed computation for us and then runs it. Recall that the delayed computation is a dask graph made of up of key-value pairs.
#
# Some things to note:
#
# 1.  As with `dask.delayed`, we need to call `.compute()` when we're done.  Up until this point everything is lazy.
# 2.  Dask will delete intermediate results (like the full pandas dataframe for each file) as soon as possible.
#     -  This lets us handle datasets that are larger than memory
#     -  This means that repeated computations will have to load all of the data in each time (run the code above again, is it faster or slower than you would expect?)
#     
# As with `Delayed` objects, you can view the underlying task graph using the `.visualize` method:

# %% {"slideshow": {"slide_type": "slide"}}
df.DepDelay.max().visualize()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Exercises

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# If you are already familiar with the Pandas API then know how to use `dask.dataframe`.  There are a couple of small changes.
#
# As noted above, computations on dask `DataFrame` objects don't perform work, instead they build up a dask graph.  We can evaluate this dask graph at any time using the `.compute()` method.

# %% {"slideshow": {"slide_type": "fragment"}}
result = df.DepDelay.mean()  # create the tasks graph

# %% {"slideshow": {"slide_type": "fragment"}}
result.compute()           # perform actual computation

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Use selections `df[...]` to find how many positive (late) departure times

# %% {"slideshow": {"slide_type": "fragment"}}
%%time
len(df[ df.DepDelay > 0])

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### and negative (early) departure times

# %% {"slideshow": {"slide_type": "fragment"}}
%%time
len(df[df.DepDelay < 0])

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### You can build a task graph to apply several functions and save computation time.

# %% {"slideshow": {"slide_type": "fragment"}}
%%time
import dask

early = df[df.DepDelay < 0].size
late = df[df.DepDelay > 0].size

early_res, late_res = dask.compute(early, late)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### How many non-cancelled flights were taken?
#
# hint: To invert a boolean pandas Series s, use ~s.

# %% {"slideshow": {"slide_type": "fragment"}}
s = pd.Series([True, True, False, True])
~s

# %% {"slideshow": {"slide_type": "fragment"}}
len(df[~df.Cancelled])

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Divisions and the Index
# ---------------------------
#
# The Pandas index associates a value to each record/row of your data.  Operations that align with the index, like `loc` can be a bit faster as a result.
#
# In `dask.dataframe` this index becomes even more important.  Recall that one dask `DataFrame` consists of several Pandas `DataFrame`s.  These dataframes are separated along the index by value.  For example, when working with time series we may partition our large dataset by month.
#
# Recall that these many partitions of our data may not all live in memory at the same time, instead they might live on disk; we simply have tasks that can materialize these pandas `DataFrames` on demand.
#
# Partitioning your data can greatly improve efficiency.  Operations like `loc`, `groupby`, and `merge/join` along the index are *much more efficient* than operations along other columns.  You can see how your dataset is partitioned with the `.divisions` attribute.  Note that data that comes out of simple data sources like CSV files aren't intelligently indexed by default.  In these cases the values for `.divisions` will be `None.`

# %% {"slideshow": {"slide_type": "slide"}}
df = dd.read_csv(filename,
                 dtype={'TailNum': str,
                        'CRSElapsedTime': float,
                        'Cancelled': bool})
df.divisions

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# However if we set the index to some new column then dask will divide our data roughly evenly along that column and create new divisions for us.  Warning, `set_index` triggers immediate computation.

# %% {"slideshow": {"slide_type": "fragment"}}
df2 = df.set_index('Year')
df2.divisions

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# We see here the minimum and maximum values (1990 and 1999) as well as the intermediate values that separate our data well.  This dataset has ten partitions, as the final value is assumed to be the inclusive right-side for the last bin.

# %% {"slideshow": {"slide_type": "fragment"}}
df2.npartitions

# %%
df2.head()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# One of the benefits of this is that operations like `loc` only need to load the relevant partitions

# %% {"slideshow": {"slide_type": "fragment"}}
df2.loc[1990]

# %%
df2.loc[1990].compute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Exercises
#
# In this section we do a few `dask.dataframe` computations. If you are comfortable with Pandas then these should be familiar. You will have to think about when to call `compute`.

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# ### In total, how many non-cancelled flights were taken from each airport?
#
# *Hint*: use [`df.groupby`](https://pandas.pydata.org/pandas-docs/stable/groupby.html). `df.groupby(df.A).B.func()`.

# %% {"slideshow": {"slide_type": "fragment"}}
%time df[~df.Cancelled].groupby('Origin').Origin.count().compute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### What was the average departure delay from each airport?
#
# Note, this is the same computation you did previously (is this approach faster or slower?)

# %% {"slideshow": {"slide_type": "fragment"}}
%time df.groupby('Origin').DepDelay.mean().compute()

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# ### What day of the week has the worst average departure delay?

# %% {"slideshow": {"slide_type": "fragment"}}
%time df.groupby('DayOfWeek').DepDelay.mean().compute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Sharing Intermediate Results
#
# When computing all of the above, we sometimes did the same operation more than once. For most operations, `dask.dataframe` hashes the arguments, allowing duplicate computations to be shared, and only computed once.
#
# For example, lets compute the mean and standard deviation for departure delay of all non-cancelled flights:

# %% {"slideshow": {"slide_type": "fragment"}}
non_cancelled = df[~df.Cancelled]
mean_delay = non_cancelled.DepDelay.mean()
std_delay = non_cancelled.DepDelay.std()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# #### Using two calls to `.compute`:

# %% {"slideshow": {"slide_type": "fragment"}}
%%time
mean_delay_res = mean_delay.compute()
std_delay_res = std_delay.compute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# #### Using one call to `dask.compute`:

# %% {"slideshow": {"slide_type": "fragment"}}
%%time
mean_delay_res, std_delay_res = dask.compute(mean_delay, std_delay)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Using `dask.compute` takes roughly 1/2 the time. This is because the task graphs for both results are merged when calling `dask.compute`, allowing shared operations to only be done once instead of twice. In particular, using `dask.compute` only does the following once:
#
# - the calls to `read_csv`
# - the filter (`df[~df.Cancelled]`)
# - some of the necessary reductions (`sum`, `count`)
#
# To see what the merged task graphs between multiple results look like (and what's shared), you can use the `dask.visualize` function (we might want to use `filename='graph.pdf'` to zoom in on the graph better):

# %% {"slideshow": {"slide_type": "slide"}}
dask.visualize(mean_delay, std_delay)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Converting `CRSDepTime` to a timestamp
#
# This dataset stores timestamps as `HHMM`, which are read in as integers in `read_csv`:

# %% {"slideshow": {"slide_type": "fragment"}}
# recreate the read_csv task with parsed dates
df = dd.read_csv(filename,
                 parse_dates={'Date': [0, 1, 2]},
                 dtype={'TailNum': str,
                        'CRSElapsedTime': float,
                        'Cancelled': bool})

# %% {"slideshow": {"slide_type": "fragment"}}
crs_dep_time = df.CRSDepTime.head(10)
crs_dep_time

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# To convert these to timestamps of scheduled departure time, we need to convert these integers into `pd.Timedelta` objects, and then combine them with the `Date` column.
#
# In pandas we'd do this using the `pd.to_timedelta` function, and a bit of arithmetic:

# %% {"slideshow": {"slide_type": "fragment"}}
import pandas as pd

# Get the first 10 dates to complement our `crs_dep_time`
date = df.Date.head(10)

# Get hours as an integer, convert to a timedelta
hours = crs_dep_time // 100
hours_timedelta = pd.to_timedelta(hours, unit='h')

# Get minutes as an integer, convert to a timedelta
minutes = crs_dep_time % 100
minutes_timedelta = pd.to_timedelta(minutes, unit='m')

# Apply the timedeltas to offset the dates by the departure time
departure_timestamp = date + hours_timedelta + minutes_timedelta
departure_timestamp

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Custom code and Dask Dataframe
#
# Unfortunately, `dask.dataframe` currently lacks the `to_timestamp` function. In general `dask.dataframe` tries hard to emulate the Pandas api (or at least the most commonly used subset of it),  but sometimes a method/function you need won't be implemented (yet), or you need to do some custom operation that there isn't a method for.
#
# To make this easier, `dask.dataframe` provides a few methods for implementing common patterns:
#
# - [`map_partitions`](http://dask.pydata.org/en/latest/dataframe-api.html#dask.dataframe.DataFrame.map_partitions)
# - [`map_overlap`](http://dask.pydata.org/en/latest/dataframe-api.html#dask.dataframe.DataFrame.map_overlap)
# - [`reduction`](http://dask.pydata.org/en/latest/dataframe-api.html#dask.dataframe.DataFrame.reduction)
#
# Here we'll just be discussing `map_partitions`, which we can use to implement `to_timestamp` on our own:

# %%
# Look at the docs for `map_partitions`

help(df.CRSDepTime.map_partitions)

# %% {"slideshow": {"slide_type": "slide"}}
hours = df.CRSDepTime // 100
# hours_timedelta = pd.to_timedelta(hours, unit='h')
hours_timedelta = hours.map_partitions(pd.to_timedelta, unit='h')

minutes = df.CRSDepTime % 100
# minutes_timedelta = pd.to_timedelta(minutes, unit='m')
minutes_timedelta = minutes.map_partitions(pd.to_timedelta, unit='m')

departure_timestamp = df.Date + hours_timedelta + minutes_timedelta

# %% {"slideshow": {"slide_type": "fragment"}}
departure_timestamp

# %% {"slideshow": {"slide_type": "fragment"}}
departure_timestamp.head()


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# ### Rewrite above to use a single call to `map_partitions`
#
# This will be slightly more efficient than two separate calls, as it reduces the number of tasks in the graph.

# %% {"slideshow": {"slide_type": "fragment"}}
def compute_departure_timestamp(df):
    hours = df.CRSDepTime // 100
    hours_timedelta = pd.to_timedelta(hours, unit='h')

    minutes = df.CRSDepTime % 100
    minutes_timedelta = pd.to_timedelta(minutes, unit='m')

    return df.Date + hours_timedelta + minutes_timedelta



# %% {"slideshow": {"slide_type": "fragment"}}
departure_timestamp = df.map_partitions(compute_departure_timestamp)

# %% {"slideshow": {"slide_type": "fragment"}}
departure_timestamp.head()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # References
#  - [Dask tutorial](https://github.com/dask/dask-tutorial)
#  - [Parallel Data Analysis tutorial](https://github.com/pydata/parallel-tutorial)

# %%
