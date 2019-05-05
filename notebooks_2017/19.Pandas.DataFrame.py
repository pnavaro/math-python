#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


# In[2]:


pd.set_option("display.max_rows", 8)
plt.rcParams['figure.figsize'] = (9, 6)


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

# # Creation of [DataFrame](https://pandas.pydata.org/pandas-docs/stable/dsintro.html#dataframe) 

# In[3]:


dates = pd.date_range('20130101', periods=8)
pd.DataFrame(np.random.randn(8,4), index=dates, columns=list('ABCD'))


# In[4]:


pd.DataFrame({'A' : 1.,
              'B' : pd.Timestamp('20180620'),
              'C' : pd.Series(1,index=list(range(4)),dtype='float32'),
              'D' : np.arange(4,dtype='int32'),
              'E' : pd.Categorical(["test","train","test","train"]),
              'F' : 'foo' ,
              'G' : [ 3*n+1 for n in range(4)]})


# # Load Data from CSV File

# In[5]:


url = "https://www.fun-mooc.fr/c4x/agrocampusouest/40001S03/asset/AnaDo_JeuDonnees_TemperatFrance.csv"
french_cities = pd.read_csv(url, delimiter=";", encoding="latin1", index_col=0)
french_cities


# # Viewing Data

# In[6]:


french_cities.head()


# In[7]:


french_cities.tail()


# # Index

# In[8]:


french_cities.index


# We can rename an index by setting its name.

# In[9]:


french_cities.index.name = "City"
french_cities.head()


# # Exercise 
# ## Translate DataFrame names in English

# In[10]:


french_cities.rename(columns={'Moye':'Mean'}, inplace=True)
french_cities.rename(columns={'Région':'Region'}, inplace=True)


# In[11]:


import locale, calendar

locale.setlocale(locale.LC_ALL,'en_US.UTF-8')
months = list(calendar.month_abbr[1:])
months


# In[12]:


french_cities.rename(
  columns={ old : new 
           for old, new in zip(french_cities.columns[:12], months)
           if old != new }, inplace=True)
french_cities.columns


# In[13]:


french_cities


# # Indexing on DataFrames

# In[14]:


french_cities['Lati']  # DF [] accesses columns (Series)


# In[15]:


french_cities.Lati


# In[16]:


french_cities.values[:,12]


# `.loc` and `.iloc` allow to access individual values, slices or masked selections:

# In[17]:


french_cities.loc['Rennes', "Jun"]


# In[18]:


french_cities.iloc[-4, 5]


# In[19]:


french_cities.loc['Rennes', ["Jul", "Aug"]]


# In[20]:


french_cities.iloc[-4, [6,7]]


# In[21]:


french_cities.loc['Rennes', "Sep":"Dec"]


# In[22]:


french_cities.iloc[-4, 8:12]


# # Masking

# In[23]:


mask = french_cities.Mean > 12
mask


# In[24]:


french_cities[mask]


# In[25]:


french_cities.loc[mask]


# In[26]:


french_cities.iloc[mask.values]


# In[27]:


french_cities[french_cities.Region == 'NO']


# In[28]:


french_cities.loc[(french_cities.Region == 'NO') | (french_cities.Region == 'SO')]


# # New column
# 

# In[29]:


french_cities["std"] = french_cities.iloc[:,:12].std(axis=1)
french_cities


# In[30]:


french_cities = french_cities.drop("std", axis=1) # remove this new column


# In[31]:


french_cities


# # Modifying a dataframe with multiple indexing

# In[32]:


# french_cities['Rennes']['Sep'] = 25 # It does not works and breaks the DataFrame
french_cities.loc['Rennes']['Jun'] # = 25 is the right way to do it


# In[33]:


french_cities


# # Transforming datasets

# In[34]:


french_cities['Mean'].min(), french_cities['Ampl'].max()


# ## Apply
# 
# Let's convert the temperature mean from Celsius to Fahrenheit degree.

# In[35]:


fahrenheit = lambda T: T*9/5+32
french_cities['Mean'].apply(fahrenheit)


# ## Sort

# In[36]:


french_cities.sort_values(by='Lati')


# In[37]:


french_cities = french_cities.sort_values(by='Lati',ascending=False)
french_cities


# ## Stack and unstack
# 
# Instead of seeing the months along the axis 1, and the cities along the axis 0, let's try to convert these into an outer and an inner axis along only 1 time dimension.

# In[38]:


pd.set_option("display.max_rows", 20)
unstacked = french_cities.iloc[:,:12].unstack()
unstacked


# In[39]:


type(unstacked)


# ## Transpose

# The result is grouped in the wrong order since it sorts first the axis that was unstacked. We need to transpose the dataframe.

# In[40]:


city_temp = french_cities.iloc[:,:12].transpose()
city_temp


# In[41]:


city_temp[['Nantes','Rennes']].boxplot(rot=90);


# # Describing

# In[42]:


french_cities['Region'].describe()


# In[43]:


french_cities['Region'].unique()


# In[44]:


french_cities['Region'].value_counts()


# In[45]:


french_cities.Region.dtypes


# In[46]:


french_cities["Region"].memory_usage()


# In[47]:


# To save memory, we can convert it to a categorical column:
french_cities["Region"] = french_cities["Region"].astype("category")
french_cities.Region.dtype


# In[48]:


french_cities["Region"].memory_usage()


# # Data Aggregation/summarization
# 
# ## groupby

# In[49]:


fc_grouped_region = french_cities.groupby("Region")
type(fc_grouped_region)


# In[50]:


for group_name, subdf in fc_grouped_region:
    print(group_name)
    print(subdf)
    print("")


# ## Transferring R data sets into Python

# In[51]:


get_ipython().run_line_magic('load_ext', 'rpy2.ipython')


# - conversions of R to pandas objects will be done automatically

# In[52]:


from rpy2.robjects import r
x = r('c(1,2,3,4)')
type(x)


# In[53]:


v = r('seq(1:10)')
v


# In[54]:


from rpy2.robjects import pandas2ri

pandas2ri.activate()
r.library('missMDA')
r.data('orange')
orange = r('orange')


# In[55]:


orange


# In[56]:


get_ipython().run_cell_magic('R', '', "library('missMDA')\ndata(orange)\nestim_ncpPCA(orange)")


# In[57]:


from rpy2.robjects.packages import importr

miss_mda = importr('missMDA')
res = miss_mda.imputePCA(orange,ncp=2)
orange_r = res[0]
orange_r.colnames


# In[58]:


orange = pd.DataFrame(pandas2ri.ri2py(orange_r), 
                      columns=orange_r.colnames, 
                      index=orange_r.rownames)

orange


# In[59]:


from rpy2.robjects import r
r('library(missMDA)')
r('df <- imputePCA(orange,ncp=2) ')
r('res <- as.data.frame(df$completeObs)')
orange = r('res')
orange


# # Load data from a local or remote HTML file
# We can download and extract data about mean sea level stations around the world from the [PSMSL website](http://www.psmsl.org/).

# In[60]:


# Needs `lxml`, `beautifulSoup4` and `html5lib` python packages
table_list = pd.read_html("http://www.psmsl.org/data/obtaining/")


# In[61]:


# there is 1 table on that page which contains metadata about the stations where 
# sea levels are recorded
local_sea_level_stations = table_list[0]
local_sea_level_stations


# # Saving Work

# [HDF5](https://support.hdfgroup.org/HDF5/) is widely used and one of the most powerful file format to store binary data. It allows to store both Series and DataFrames.

# In[62]:


with pd.HDFStore("../data/pandas_nb.h5") as writer:
    local_sea_level_stations.to_hdf(writer, "/sea_level/stations")


# In[63]:


get_ipython().run_line_magic('ls', '../data/*.h5')


# # Reloading data

# In[64]:


with pd.HDFStore("../data/pandas_nb.h5") as store:
    local_sea_level_stations = store["/sea_level/stations"]


# In[65]:


local_sea_level_stations


# # References
# 
# - [Pandas website](http://pandas.pydata.org).
# - *Python for Data Analysis* by Wes McKinney ([O'Reilly Media](http://shop.oreilly.com/product/0636920023784.do)).
# - [Analyzing and Manipulating Data with Pandas Beginner](https://youtu.be/6ohWS7J1hVA) | SciPy 2016 Tutorial | Jonathan Rocher.
# - https://github.com/groverpr/learn_python_libraries
# - [Python Data Science Handbook](https://jakevdp.github.io/PythonDataScienceHandbook/)
# 
