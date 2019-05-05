#!/usr/bin/env python
# coding: utf-8

# from [101 Pandas Exercises for Data Analysis](https://www.machinelearningplus.com/python/101-pandas-exercises-python/)

# ### 1. How to import pandas and check the version?

# In[1]:


import pandas as pd

pd.__version__


# ### 2. How to create a series from a list, numpy array and dict?
# Create a pandas series from each of the items below: a list, numpy and a dictionary

# In[2]:


import numpy as np
mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))


# In[3]:


ser1 = pd.Series(mylist)
ser2 = pd.Series(myarr)
ser3 = pd.Series(mydict)


# ### 3. How to convert the index of a series into a column of a dataframe?
# 
# Convert the series ser into a dataframe with its index as another column on the dataframe.

# In[4]:


mylist = list('abcedfghijklmnopqrstuvwxyz')
myarr = np.arange(26)
mydict = dict(zip(mylist, myarr))
ser = pd.Series(mydict)


# In[5]:


df = ser.to_frame().reset_index()
df.head()


# ### 4. How to combine many series to form a dataframe?
# 
# Combine ser1 and ser2 to form a dataframe.

# In[6]:


import numpy as np
ser1 = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))
ser2 = pd.Series(np.arange(26))


# In[7]:


df = pd.DataFrame()
df['col1'] = ser1
df['col2'] = ser2
df.head()


# In[8]:


# Solution 1
df = pd.concat([ser1, ser2], axis=1)

# Solution 2
df = pd.DataFrame({'col1': ser1, 'col2': ser2})
df.head()


# ### 5. How to assign name to the series’ index?
# 
# Give a name to the series ser calling it ‘alphabets’.

# In[9]:


ser = pd.Series(list('abcedfghijklmnopqrstuvwxyz'))


# In[10]:


ser.name = 'alphabets'
ser.head()


# ### 6. How to get the items of series A not present in series B?
# 
# From ser1 remove items present in ser2.

# In[11]:


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


# ### 7. How to get the items not common to both series A and series B?
# 
# Get all items of ser1 and ser2 not common to both.
# 
# Input

# In[11]:


ser1 = pd.Series([1, 2, 3, 4, 5])
ser2 = pd.Series([4, 5, 6, 7, 8])


# ### 8. How to get the minimum, 25th percentile, median, 75th, and max of a numeric series?
# 
# Compute the minimum, 25th percentile, median, 75th, and maximum of ser.

# In[12]:


ser = pd.Series(np.random.normal(10, 5, 25))


# In[13]:


ser = pd.Series(np.take(list('abcdefgh'), np.random.randint(8, size=30)))


# ### 10. How to keep only top 2 most frequent values as it is and replace everything else as ‘Other’?
# 
# From ser, keep the top 2 most frequent items as it is and replace everything else as ‘Other’.
# 
# Input

# In[12]:


np.random.RandomState(100)
ser = pd.Series(np.random.randint(1, 5, [12]))


# ### 11. How to bin a numeric series to 10 groups of equal size?
# 
# Bin the series ser into 10 equal deciles and replace the values with the bin name.
# 
# Input

# In[13]:


ser = pd.Series(np.random.random(20))


# Desired Output
# ```
# # First 5 items
# 0    7th
# 1    9th
# 2    7th
# 3    3rd
# 4    8th
# dtype: category
# Categories (10, object): [1st < 2nd < 3rd < 4th ... 7th < 8th < 9th < 10th]
# ```

# ### 12. How to convert a numpy array to a dataframe of given shape? (L1)
# 
# Reshape the series ser into a dataframe with 7 rows and 5 columns
# 
# Input

# In[16]:


ser = pd.Series(np.random.randint(1, 10, 35))


# ### 13. How to find the positions of numbers that are multiples of 3 from a series?
# Difficulty Level: L2
# 
# Find the positions of numbers that are multiples of 3 from ser.
# 
# Input

# In[14]:


ser = pd.Series(np.random.randint(1, 10, 7))


# ### 14. How to extract items at given positions from a series
# 
# From ser, extract the items at positions in list pos.
# 
# Input

# In[15]:


ser = pd.Series(list('abcdefghijklmnopqrstuvwxyz'))
pos = [0, 4, 8, 14, 20]


# ### 15. How to stack two series vertically and horizontally ?
# 
# Stack ser1 and ser2 vertically and horizontally (to form a dataframe).
# 
# Input

# In[16]:


ser1 = pd.Series(range(5))
ser2 = pd.Series(list('abcde'))


# ### 16. How to get the positions of items of series A in another series B?
# 
# Get the positions of items of ser2 in ser1 as a list.
# 
# Input

# In[20]:


ser1 = pd.Series([10, 9, 6, 5, 3, 1, 12, 8, 13])
ser2 = pd.Series([1, 3, 10, 13])


# ### 17. How to compute the mean squared error on a truth and predicted series?
# 
# Compute the mean squared error of truth and pred series.
# 
# Input

# In[21]:


truth = pd.Series(range(10))
pred = pd.Series(range(10)) + np.random.random(10)


# ### 18. How to convert the first character of each element in a series to uppercase?
# 
# Change the first character of each word to upper case in each word of ser.

# In[22]:


ser = pd.Series(['how', 'to', 'kick', 'ass?'])


# ### 19. How to calculate the number of characters in each word in a series?
# Difficulty Level: L2
# 
# Input

# In[23]:


ser = pd.Series(['how', 'to', 'kick', 'ass?'])


# ### 20. How to compute difference of differences between consequtive numbers of a series?
# 
# Difference of differences between the consequtive numbers of ser.
# 
# Input

# In[24]:


ser = pd.Series([1, 3, 6, 10, 15, 21, 27, 35])


# Desired Output
# 
# [nan, 2.0, 3.0, 4.0, 5.0, 6.0, 6.0, 8.0]
# [nan, nan, 1.0, 1.0, 1.0, 1.0, 0.0, 2.0]

# ### 21. How to convert a series of date-strings to a timeseries?
# 
# Input

# In[25]:


ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])


# Desired Output
# ```
# 0   2010-01-01 00:00:00
# 1   2011-02-02 00:00:00
# 2   2012-03-03 00:00:00
# 3   2013-04-04 00:00:00
# 4   2014-05-05 00:00:00
# 5   2015-06-06 12:20:00
# dtype: datetime64[ns]
# ```

# ### 22. How to get the day of month, week number, day of year and day of week from a series of date strings?
# 
# Get the day of month, week number, day of year and day of week from ser.
# 
# Input

# In[26]:


ser = pd.Series(['01 Jan 2010', '02-02-2011', '20120303', '2013/04/04', '2014-05-05', '2015-06-06T12:20'])


# Desired output
# ```
# Date:  [1, 2, 3, 4, 5, 6]
# Week number:  [53, 5, 9, 14, 19, 23]
# Day num of year:  [1, 33, 63, 94, 125, 157]
# Day of week:  ['Friday', 'Wednesday', 'Saturday', 'Thursday', 'Monday', 'Saturday']
# ```

# 23. How to convert year-month string to dates corresponding to the 4th day of the month?
# 
# Change ser to dates that start with 4th of the respective months.
# 
# Input

# In[78]:


ser = pd.Series(['Jan 2010', 'Feb 2011', 'Mar 2012'])


# Desired Output
# ```
# 0   2010-01-04
# 1   2011-02-04
# 2   2012-03-04
# dtype: datetime64[ns]
# ```

# 24. How to filter words that contain atleast 2 vowels from a series?
# 
# From ser, extract words that contain atleast 2 vowels.
# 
# Input

# In[79]:


ser = pd.Series(['Apple', 'Orange', 'Plan', 'Python', 'Money'])


# Desired Output
# ```
# 0     Apple
# 1    Orange
# 4     Money
# dtype: object
# ```

# 25. How to filter valid emails from a series?
# 
# Extract the valid emails from the series emails. The regex pattern for valid emails is provided as reference.
# 
# Input

# In[80]:


emails = pd.Series(['buying books at amazom.com', 'rameses@egypt.com', 'matt@t.co', 'narendra@modi.com'])
pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\.[A-Za-z]{2,4}'


# Desired Output
# ```
# 1    rameses@egypt.com
# 2            matt@t.co
# 3    narendra@modi.com
# dtype: object
# ```

# 26. How to get the mean of a series grouped by another series?
# 
# Compute the mean of weights of each fruit.
# 
# Input

# In[81]:


fruit = pd.Series(np.random.choice(['apple', 'banana', 'carrot'], 10))
weights = pd.Series(np.linspace(1, 10, 10))
print(weights.tolist())
print(fruit.tolist())


# Desired output
# ```
# # values can change due to randomness
# apple     6.0
# banana    4.0
# carrot    5.8
# dtype: float64
# ```

# 27. How to compute the euclidean distance between two series?
# Difficiulty Level: L2
# 
# Compute the euclidean distance between series (points) p and q, without using a packaged formula.
# 
# Input

# In[32]:


p = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
q = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])


# Desired Output
# 
# 18.165

# 28. How to find all the local maxima (or peaks) in a numeric series?
# 
# Get the positions of peaks (values surrounded by smaller values on both sides) in ser.
# 
# Input

# In[33]:


ser = pd.Series([2, 10, 3, 4, 9, 10, 2, 7, 3])


# Desired output
# 
# array([1, 5, 7])

# 29. How to replace missing spaces in a string with the least frequent character?
# Replace the spaces in my_str with the least frequent character.
# 
# Input

# In[83]:


my_str = 'dbc deb abed gade'


# Desired Output
# ```
# 'dbccdebcabedcgade'  # least frequent is 'c'
# ```

# 30. How to create a TimeSeries starting ‘2000-01-01’ and 10 weekends (saturdays) after that having random numbers as values?
# 
# Desired output
# ```
# # values can be random
# 2000-01-01    4
# 2000-01-08    1
# 2000-01-15    8
# 2000-01-22    4
# 2000-01-29    4
# 2000-02-05    2
# 2000-02-12    4
# 2000-02-19    9
# 2000-02-26    6
# 2000-03-04    6
# ```

# 31. How to fill an intermittent time series so all missing dates show up with values of previous non-missing date?
# 
# ser has missing dates and values. Make all missing dates appear and fill up with value from previous date.
# 
# Input

# In[84]:


ser = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2000-01-01', '2000-01-03', '2000-01-06', '2000-01-08']))
print(ser)


# 
# Desired Output
# ```
# 2000-01-01     1.0
# 2000-01-02     1.0
# 2000-01-03    10.0
# 2000-01-04    10.0
# 2000-01-05    10.0
# 2000-01-06     3.0
# 2000-01-07     3.0
# 2000-01-08     NaN
# ```

# 32. How to compute the autocorrelations of a numeric series?
# 
# Compute autocorrelations for the first 10 lags of ser. Find out which lag has the largest correlation.
# 
# Input

# In[85]:


ser = pd.Series(np.arange(20) + np.random.normal(1, 10, 20))


# Desired output
# ```
# # values will change due to randomness
# [0.29999999999999999, -0.11, -0.17000000000000001, 0.46000000000000002, 0.28000000000000003, -0.040000000000000001, -0.37, 0.41999999999999998, 0.47999999999999998, 0.17999999999999999]
# Lag having highest correlation:  9
# ```

# 33. How to import only every nth row from a csv file to create a dataframe?
# 
# Import every 50th row of BostonHousing dataset as a dataframe.

# 34. How to change column values when importing csv to a dataframe?
# 

# Import the boston housing dataset, but while importing change the 'medv' (median house value) column so that values < 25 becomes ‘Low’ and > 25 becomes ‘High’.

#  
# 35. How to create a dataframe with rows as strides from a given series?
# 

# Input

# In[86]:


L = pd.Series(range(15))


# Desired Output
# ```
# array([[ 0,  1,  2,  3],
#        [ 2,  3,  4,  5],
#        [ 4,  5,  6,  7],
#        [ 6,  7,  8,  9],
#        [ 8,  9, 10, 11],
#        [10, 11, 12, 13]])
# ```

# 36. How to import only specified columns from a csv file?
# 
# Import ‘crim’ and ‘medv’ columns of the BostonHousing dataset as a dataframe.

# 37. How to get the nrows, ncolumns, datatype, summary stats of each column of a dataframe? Also get the array and list equivalent.
# 
# Get the number of rows, columns, datatype and summary statistics of each column of the Cars93 dataset. Also get the numpy array and list equivalent of the dataframe.

# 38. How to extract the row and column number of a particular cell with given criterion?
# 
# Input

# In[87]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


# Which manufacturer, model and type has the highest Price? What is the row and column number of the cell with the highest Price value?

# 39. How to rename a specific columns in a dataframe?
# 
# Rename the column Type as CarType in df and replace the ‘.’ in column names with ‘_’.
# 
# Input

# In[88]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')
print(df.columns)


# Desired Solution
# ```
# print(df.columns)
# #> Index(['Manufacturer', 'Model', 'CarType', 'Min_Price', 'Price', 'Max_Price',
# #>        'MPG_city', 'MPG_highway', 'AirBags', 'DriveTrain', 'Cylinders',
# #>        'EngineSize', 'Horsepower', 'RPM', 'Rev_per_mile', 'Man_trans_avail',
# #>        'Fuel_tank_capacity', 'Passengers', 'Length', 'Wheelbase', 'Width',
# #>        'Turn_circle', 'Rear_seat_room', 'Luggage_room', 'Weight', 'Origin',
# #>        'Make'],
# #>       dtype='object')
# ```

# 40. How to check if a dataframe has any missing values?
# 
# Check if df has any missing values.
# 
# Input

# In[89]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


# 41. How to count the number of missing values in each column?
# 
# Count the number of missing values in each column of df. Which column has the maximum number of missing values?
# 
# Input

# In[90]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


# 42. How to replace missing values of multiple numeric columns with the mean?
# 
# Replace missing values in Min.Price and Max.Price columns with their respective mean.
# 
# Input

# In[91]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


# 43. How to use apply function on existing columns with global variables as additional arguments?
# 
# In df, use apply method to replace the missing values in Min.Price with the column’s mean and those in Max.Price with the column’s median.
# 
# Input

# In[92]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


# Use Hint from StackOverflow

# 44. How to select a specific column from a dataframe as a dataframe instead of a series?
# 
# Get the first column (a) in df as a dataframe (rather than as a Series).
# 
# Input

# In[93]:


df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


# 45. How to change the order of columns of a dataframe?
# 
# Actually 3 questions.
# 
# In df, interchange columns 'a' and 'c'.
# 
# Create a generic function to interchange two columns, without hardcoding column names.
# 
# Sort the columns in reverse alphabetical order, that is colume 'e' first through column 'a' last.
# 
# Input

# In[94]:


df = pd.DataFrame(np.arange(20).reshape(-1, 5), columns=list('abcde'))


# 46. How to set the number of rows and columns displayed in the output?
# 
# Change the pamdas display settings on printing the dataframe df it shows a maximum of 10 rows and 10 columns.
# 
# Input

# In[95]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


# 47. How to format or suppress scientific notations in a pandas dataframe?
# 
# Suppress scientific notations like ‘e-03’ in df and print upto 4 numbers after decimal.
# 
# Input

# In[96]:


df = pd.DataFrame(np.random.random(4)**10, columns=['random'])
df


# Desired Output
# ```
# #>    random
# #> 0  0.0035
# #> 1  0.0000
# #> 2  0.0747
# #> 3  0.0000
# ```

# 48. How to format all the values in a dataframe as percentages?
# 
# Format the values in column 'random' of df as percentages.
# 
# Input

# In[97]:


df = pd.DataFrame(np.random.random(4), columns=['random'])
df


# Desired Output
# ```
# #>      random
# #> 0    68.97%
# #> 1    95.72%
# #> 2    15.91%
# #> 3    2.10%
# ```

# 49. How to filter every nth row in a dataframe?
# 
# From df, filter the 'Manufacturer', 'Model' and 'Type' for every 20th row starting from 1st (row 0).
# 
# Input

# In[98]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv')


# 50. How to create a primary key index by combining relevant columns?
# 
# In df, Replace NaNs with ‘missing’ in columns 'Manufacturer', 'Model' and 'Type' and create a index as a combination of these three columns and check if the index is a primary key.
# 
# Input

# In[99]:


df = pd.read_csv('https://raw.githubusercontent.com/selva86/datasets/master/Cars93_miss.csv', usecols=[0,1,2,3,5])


# Desired Output

# ```
# Manufacturer    Model     Type  Min.Price  Max.Price
# Acura_Integra_Small           Acura  Integra    Small       12.9       18.8
# missing_Legend_Midsize      missing   Legend  Midsize       29.2       38.7
# Audi_90_Compact                Audi       90  Compact       25.9       32.3
# Audi_100_Midsize               Audi      100  Midsize        NaN       44.6
# BMW_535i_Midsize                BMW     535i  Midsize        NaN        NaN
# ```

# 51. How to get the row number of the nth largest value in a column?
# 
# Find the row position of the 5th largest value of column 'a' in df.
# 
# Input

# In[50]:


df = pd.DataFrame(np.random.randint(1, 30, 30).reshape(10,-1), columns=list('abc'))


# 52. How to find the position of the nth largest value greater than a given value?
# 
# In ser, find the position of the 2nd largest value greater than the mean.
# 
# Input

# In[100]:


ser = pd.Series(np.random.randint(1, 100, 15))


# 53. How to get the last n rows of a dataframe with row sum > 100?
# 
# Get the last two rows of df whose row sum is greater than 100.

# In[101]:


df = pd.DataFrame(np.random.randint(10, 40, 60).reshape(-1, 4))


# 54. How to find and cap outliers from a series or dataframe column?
# 
# Replace all values of ser in the lower 5%ile and greater than 95%ile with respective 5th and 95th %ile value.
# 
# Input

# In[53]:


ser = pd.Series(np.logspace(-2, 2, 30))


# 55. How to reshape a dataframe to the largest possible square after removing the negative values?
# 
# Reshape df to the largest possible square with negative values removed. Drop the smallest values if need be. The order of the positive numbers in the result should remain the same as the original.
# 
# Input

# In[102]:


df = pd.DataFrame(np.random.randint(-20, 50, 100).reshape(10,-1))


# 56. How to swap two rows of a dataframe?
# 
# Swap rows 1 and 2 in df.
# 
# Input

# In[103]:


df = pd.DataFrame(np.arange(25).reshape(5, -1))


# 57. How to reverse the rows of a dataframe?
# 
# Reverse all the rows of dataframe df.
# 
# Input

# In[104]:


df = pd.DataFrame(np.arange(25).reshape(5, -1))


# 58. How to create one-hot encodings of a categorical variable (dummy variables)?
# 
# Get one-hot encodings for column 'a' in the dataframe df and append it as columns.
# 
# Input

# In[105]:


df = pd.DataFrame(np.arange(25).reshape(5,-1), columns=list('abcde'))


# Output
# 
#    0  5  10  15  20   b   c   d   e
# 0  1  0   0   0   0   1   2   3   4
# 1  0  1   0   0   0   6   7   8   9
# 2  0  0   1   0   0  11  12  13  14
# 3  0  0   0   1   0  16  17  18  19
# 4  0  0   0   0   1  21  22  23  24

# 59. Which column contains the highest number of row-wise maximum values?
# 
# Obtain the column name with the highest number of row-wise maximum’s in df.

# In[106]:


df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1))


# 60. How to create a new column that contains the row number of nearest column by euclidean distance?
# Create a new column such that, each row contains the row number of nearest row-record by euclidean distance.
# 
# Input

# In[107]:


df = pd.DataFrame(np.random.randint(1,100, 40).reshape(10, -1), columns=list('pqrs'), index=list('abcdefghij'))
df
#     p   q   r   s
# a  57  77  13  62
# b  68   5  92  24
# c  74  40  18  37
# d  80  17  39  60
# e  93  48  85  33
# f  69  55   8  11
# g  39  23  88  53
# h  63  28  25  61
# i  18   4  73   7
# j  79  12  45  34


# Desired Output
# ```
# df
# #    p   q   r   s nearest_row   dist
# # a  57  77  13  62           i  116.0
# # b  68   5  92  24           a  114.0
# # c  74  40  18  37           i   91.0
# # d  80  17  39  60           i   89.0
# # e  93  48  85  33           i   92.0
# # f  69  55   8  11           g  100.0
# # g  39  23  88  53           f  100.0
# # h  63  28  25  61           i   88.0
# # i  18   4  73   7           a  116.0
# # j  79  12  45  34           a   81.0
# ```

# 61. How to know the maximum possible correlation value of each column against other columns?
# 
# Compute maximum possible absolute correlation value of each column against other columns in df.
# 
# Input

# In[108]:


df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1), columns=list('pqrstuvwxy'), index=list('abcdefgh'))


# 62. How to create a column containing the minimum by maximum of each row?
# 
# Compute the minimum-by-maximum for every row of df.

# In[109]:


df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))


# 63. How to create a column that contains the penultimate value in each row?
# 
# Create a new column 'penultimate' which has the second largest value of each row of df.
# 
# Input

# In[110]:


df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))


# 64. How to normalize all columns in a dataframe?
# 
# Normalize all columns of df by subtracting the column mean and divide by standard deviation.
# Range all columns of df such that the minimum value in each column is 0 and max is 1.
# Don’t use external packages like sklearn.
# 
# Input

# In[111]:


df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))


# 65. How to compute the correlation of each row with the suceeding row?
# 
# Compute the correlation of each row of df with its succeeding row.
# 
# Input

# In[112]:


df = pd.DataFrame(np.random.randint(1,100, 80).reshape(8, -1))


# 66. How to replace both the diagonals of dataframe with 0?
# 
# Replace both values in both diagonals of df with 0.
# 
# Input

# In[113]:


df = pd.DataFrame(np.random.randint(1,100, 100).reshape(10, -1))
df
#     0   1   2   3   4   5   6   7   8   9
# 0  11  46  26  44  11  62  18  70  68  26
# 1  87  71  52  50  81  43  83  39   3  59
# 2  47  76  93  77  73   2   2  16  14  26
# 3  64  18  74  22  16  37  60   8  66  39
# 4  10  18  39  98  25   8  32   6   3  29
# 5  29  91  27  86  23  84  28  31  97  10
# 6  37  71  70  65   4  72  82  89  12  97
# 7  65  22  97  75  17  10  43  78  12  77
# 8  47  57  96  55  17  83  61  85  26  86
# 9  76  80  28  45  77  12  67  80   7  63


# Desired output
# ```
# #     0   1   2   3   4   5   6   7   8   9
# # 0   0  46  26  44  11  62  18  70  68   0
# # 1  87   0  52  50  81  43  83  39   0  59
# # 2  47  76   0  77  73   2   2   0  14  26
# # 3  64  18  74   0  16  37   0   8  66  39
# # 4  10  18  39  98   0   0  32   6   3  29
# # 5  29  91  27  86   0   0  28  31  97  10
# # 6  37  71  70   0   4  72   0  89  12  97
# # 7  65  22   0  75  17  10  43   0  12  77
# # 8  47   0  96  55  17  83  61  85   0  86
# # 9   0  80  28  45  77  12  67  80   7   0
# ```

# 67. How to get the particular group of a groupby dataframe by key?
# 
# This is a question related to understanding of grouped dataframe. From df_grouped, get the group belonging to 'apple' as a dataframe.
# 
# Input

# In[114]:


df = pd.DataFrame({'col1': ['apple', 'banana', 'orange'] * 3,
                   'col2': np.random.rand(9),
                   'col3': np.random.randint(0, 15, 9)})

df_grouped = df.groupby(['col1'])


# 68. How to get the n’th largest value of a column when grouped by another column?
# 
# In df, find the second largest value of 'taste' for 'banana'
# 
# Input

# 

# In[115]:


df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})
               


# 69. How to compute grouped mean on pandas dataframe and keep the grouped column as another column (not index)?
# 
# In df, Compute the mean price of every fruit, while keeping the fruit as another column instead of an index.
# 
# Input

# In[117]:


df = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                   'rating': np.random.rand(9),
                   'price': np.random.randint(0, 15, 9)})
               


# 70. How to join two dataframes by 2 columns so they have only the common rows?
# 
# Join dataframes df1 and df2 by ‘fruit-pazham’ and ‘weight-kilo’.
# 
# Input

# In[118]:


df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})


# 71. How to remove rows from a dataframe that are present in another dataframe?
# 
# From df1, remove the rows that are present in df2. All three columns must be the same.
# 
# Input

# In[119]:


df1 = pd.DataFrame({'fruit': ['apple', 'banana', 'orange'] * 3,
                    'weight': ['high', 'medium', 'low'] * 3,
                    'price': np.random.randint(0, 15, 9)})

df2 = pd.DataFrame({'pazham': ['apple', 'orange', 'pine'] * 2,
                    'kilo': ['high', 'low'] * 3,
                    'price': np.random.randint(0, 15, 6)})


# 72. How to get the positions where values of two columns match?
# 

# 73. How to create lags and leads of a column in a dataframe?
# 
# Create two new columns in df, one of which is a lag1 (shift column a down by 1 row) of column ‘a’ and the other is a lead1 (shift column b up by 1 row).

# In[120]:


df = pd.DataFrame(np.random.randint(1, 100, 20).reshape(-1, 4), columns = list('abcd'))
df


# Desired Output
# 
# a   b   c   d  a_lag1  b_lead1
# 0  66  34  76  47     NaN     86.0
# 1  20  86  10  81    66.0     73.0
# 2  75  73  51  28    20.0      1.0
# 3   1   1   9  83    75.0     47.0
# 4  30  47  67   4     1.0      NaN

# 74. How to get the frequency of unique values in the entire dataframe?
# 
# Get the frequency of unique values in the entire dataframe df.
# 
# Input

# In[121]:


df = pd.DataFrame(np.random.randint(1, 10, 20).reshape(-1, 4), columns = list('abcd'))


# 75. How to split a text column into two separate columns?
# 
# Split the string column in df to form a dataframe with 3 columns as shown.
# 
# Input

# In[122]:


df = pd.DataFrame(["STD, City    State",
"33, Kolkata    West Bengal",
"44, Chennai    Tamil Nadu",
"40, Hyderabad    Telengana",
"80, Bangalore    Karnataka"], columns=['row'])

print(df)


# Desired Output
# ```
# 0 STD        City        State
# 1  33     Kolkata  West Bengal
# 2  44     Chennai   Tamil Nadu
# 3  40   Hyderabad    Telengana
# 4  80   Bangalore    Karnataka
# ```
