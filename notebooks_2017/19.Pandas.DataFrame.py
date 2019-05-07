# -*- coding: utf-8 -*-
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

# %% {"slideshow": {"slide_type": "slide"}}
%matplotlib inline
%config InlineBackend.figure_format = 'retina'
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# %% {"slideshow": {"slide_type": "slide"}}
pd.set_option("display.max_rows", 8)
plt.rcParams['figure.figsize'] = (9, 6)

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
# ```sh
# conda install pandas
# pip3 install pandas
# ```
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

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Creation of [DataFrame](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) 

# %% {"slideshow": {"slide_type": "fragment"}}
dates = pd.date_range('20130101', periods=8)
pd.DataFrame(np.random.randn(8,4), index=dates, columns=list('ABCD'))

# %% {"slideshow": {"slide_type": "slide"}}
pd.DataFrame({'A' : 1.,
              'B' : pd.Timestamp('20180620'),
              'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
              'D' : np.arange(4,dtype='int32'),
              'E' : pd.Categorical(["test","train","test","train"]),
              'F' : 'foo' ,
              'G' : [ 3*n+1 for n in range(4)]})


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Load Data from CSV File

# %% {"slideshow": {"slide_type": "fragment"}}
url = "https://www.fun-mooc.fr/c4x/agrocampusouest/40001S03/asset/AnaDo_JeuDonnees_TemperatFrance.csv"
french_cities = pd.read_csv(url, delimiter=";", encoding="latin1", index_col=0)
french_cities

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Viewing Data

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.head()

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.tail()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Index

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.index

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# We can rename an index by setting its name.

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.index.name = "City"
french_cities.head()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Exercise 
# ## Translate DataFrame names in English

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.rename(columns={'Moye':'Mean'}, inplace=True)
french_cities.rename(columns={'Région':'Region'}, inplace=True)

# %% {"slideshow": {"slide_type": "slide"}}
import locale, calendar

locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
months = list(calendar.month_abbr[1:])
months

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.rename(
  columns={ old : new 
           for old, new in zip(french_cities.columns[:12], months)
           if old != new }, inplace=True)
french_cities.columns

# %% {"slideshow": {"slide_type": "slide"}}
french_cities

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Indexing on DataFrames

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities['Lati']  # DF [] accesses columns (Series)

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.Lati

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.values[:,12]

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# `.loc` and `.iloc` allow to access individual values, slices or masked selections:

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.loc['Rennes', "Jun"]

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.iloc[-4, 5]

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.loc['Rennes', ["Jul", "Aug"]]

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.iloc[-4, [6,7]]

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.loc['Rennes', "Sep":"Dec"]

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.iloc[-4, 8:12]

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Masking

# %% {"slideshow": {"slide_type": "fragment"}}
mask = french_cities.Mean > 12
mask

# %% {"slideshow": {"slide_type": "slide"}}
french_cities[mask]

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.loc[mask]

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.iloc[mask.values]

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities[french_cities.Region == 'NO']

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.loc[(french_cities.Region == 'NO') | (french_cities.Region == 'SO')]

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # New column
#

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities["std"] = french_cities.iloc[:,:12].std(axis=1)
french_cities

# %% {"slideshow": {"slide_type": "slide"}}
french_cities = french_cities.drop("std", axis=1) # remove this new column

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Modifying a dataframe with multiple indexing

# %% {"slideshow": {"slide_type": "fragment"}}
# french_cities['Rennes']['Sep'] = 25 # It does not works and breaks the DataFrame
french_cities.loc['Rennes']['Jun'] # = 25 is the right way to do it

# %% {"slideshow": {"slide_type": "skip"}}
french_cities

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Transforming datasets

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities['Mean'].min(), french_cities['Ampl'].max()

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# ## Apply
#
# Let's convert the temperature mean from Celsius to Fahrenheit degree.

# %% {"slideshow": {"slide_type": "fragment"}}
fahrenheit = lambda T: T*9/5+32
french_cities['Mean'].apply(fahrenheit)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Sort

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities.sort_values(by='Lati')

# %% {"slideshow": {"slide_type": "slide"}}
french_cities = french_cities.sort_values(by='Lati',ascending=False)
french_cities

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Stack and unstack
#
# Instead of seeing the months along the axis 1, and the cities along the axis 0, let's try to convert these into an outer and an inner axis along only 1 time dimension.

# %% {"slideshow": {"slide_type": "fragment"}}
pd.set_option("display.max_rows", 20)
unstacked = french_cities.iloc[:,:12].unstack()
unstacked

# %% {"slideshow": {"slide_type": "slide"}}
type(unstacked)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Transpose

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# The result is grouped in the wrong order since it sorts first the axis that was unstacked. We need to transpose the dataframe.

# %% {"slideshow": {"slide_type": "slide"}}
city_temp = french_cities.iloc[:,:12].transpose()
city_temp

# %% {"slideshow": {"slide_type": "slide"}}
city_temp[['Nantes','Rennes']].boxplot(rot=90);

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Describing

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities['Region'].describe()

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities['Region'].unique()

# %% {"slideshow": {"slide_type": "slide"}}
french_cities['Region'].value_counts()

# %% {"slideshow": {"slide_type": "slide"}}
french_cities.Region.dtypes

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities["Region"].memory_usage()

# %% {"slideshow": {"slide_type": "slide"}}
# To save memory, we can convert it to a categorical column:
french_cities["Region"] = french_cities["Region"].astype("category")
french_cities.Region.dtype

# %% {"slideshow": {"slide_type": "fragment"}}
french_cities["Region"].memory_usage()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Data Aggregation/summarization
#
# ## groupby

# %% {"slideshow": {"slide_type": "fragment"}}
fc_grouped_region = french_cities.groupby("Region")
type(fc_grouped_region)

# %% {"slideshow": {"slide_type": "slide"}}
for group_name, subdf in fc_grouped_region:
    print(group_name)
    print(subdf)
    print("")

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Transferring R data sets into Python

# %% {"slideshow": {"slide_type": "fragment"}}
%load_ext rpy2.ipython

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# - conversions of R to pandas objects will be done automatically

# %% {"slideshow": {"slide_type": "fragment"}}
from rpy2.robjects import r
x = r('c(1,2,3,4)')
type(x)

# %% {"slideshow": {"slide_type": "fragment"}}
v = r('seq(1:10)')
v

# %% {"slideshow": {"slide_type": "slide"}}
from rpy2.robjects import pandas2ri

pandas2ri.activate()
r.library('missMDA')
r.data('orange')
orange = r('orange')

# %% {"slideshow": {"slide_type": "slide"}}
orange

# %% {"slideshow": {"slide_type": "slide"}, "language": "R"}
# library('missMDA')
# data(orange)
# estim_ncpPCA(orange)

# %% {"slideshow": {"slide_type": "fragment"}}
from rpy2.robjects.packages import importr

miss_mda = importr('missMDA')
res = miss_mda.imputePCA(orange,ncp=2)
orange_r = res[0]
orange_r.colnames

# %% {"slideshow": {"slide_type": "slide"}}
orange = pd.DataFrame(pandas2ri.ri2py(orange_r), 
                      columns=orange_r.colnames, 
                      index=orange_r.rownames)

orange

# %% {"slideshow": {"slide_type": "slide"}}
from rpy2.robjects import r
r('library(missMDA)')
r('df <- imputePCA(orange,ncp=2) ')
r('res <- as.data.frame(df$completeObs)')
orange = r('res')
orange

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Load data from a local or remote HTML file
# We can download and extract data about mean sea level stations around the world from the [PSMSL website](http://www.psmsl.org/).

# %% {"slideshow": {"slide_type": "fragment"}}
# Needs `lxml`, `beautifulSoup4` and `html5lib` python packages
table_list = pd.read_html("http://www.psmsl.org/data/obtaining/")

# %% {"slideshow": {"slide_type": "fragment"}}
# there is 1 table on that page which contains metadata about the stations where 
# sea levels are recorded
local_sea_level_stations = table_list[0]
local_sea_level_stations

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Saving Work

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# [HDF5](https://support.hdfgroup.org/HDF5/) is widely used and one of the most powerful file format to store binary data. It allows to store both Series and DataFrames.

# %% {"slideshow": {"slide_type": "fragment"}}
with pd.HDFStore("../data/pandas_nb.h5") as writer:
    local_sea_level_stations.to_hdf(writer, "/sea_level/stations")

# %% {"slideshow": {"slide_type": "fragment"}}
%ls ../data/*.h5

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Reloading data

# %% {"slideshow": {"slide_type": "fragment"}}
with pd.HDFStore("../data/pandas_nb.h5") as store:
    local_sea_level_stations = store["/sea_level/stations"]

# %% {"slideshow": {"slide_type": "slide"}}
local_sea_level_stations

# %% [markdown] {"slideshow": {"slide_type": "skip"}}
# # References
#
# - [Pandas website](http://pandas.pydata.org).
# - *Python for Data Analysis* by Wes McKinney ([O'Reilly Media](http://shop.oreilly.com/product/0636920023784.do)).
# - [Analyzing and Manipulating Data with Pandas Beginner](https://youtu.be/6ohWS7J1hVA) | SciPy 2016 Tutorial | Jonathan Rocher.
# - https://github.com/groverpr/learn_python_libraries
# - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
#
