#!/usr/bin/env python
# coding: utf-8

# # Input and Output
# - str() function return human-readable representations of values.
# - repr() generate representations which can be read by the interpreter.
# - For objects which don’t have a particular representation for human consumption, str() will return the same value as repr().

# In[1]:


s = 'Hello, world.'
str(s)


# In[2]:


l = list(range(4))
str(l)


# In[3]:


repr(s)


# In[4]:


repr(l)


# In[5]:


x = 10 * 3.25
y = 200 * 200
s = 'The value of x is ' + str(x) + ', and y is ' + repr(y) + '...'
print(s)


# repr() of a string adds string quotes and backslashes:

# In[6]:


hello = 'hello, world\n'
hellos = repr(hello)
hellos


# The argument to repr() may be any Python object:

# In[7]:


repr((x, y, ('spam', 'eggs')))


# In[8]:


n = 7
for x in range(1, n):
    for i in range(n):
        print(repr(x**i).rjust(i+2), end=' ') # rjust or center can be used
    print()


# In[9]:


for x in range(1, n):
    for i in range(n):
        print("%07d" % x**i, end=' ')  # old C format
    print()


# # Usage of the `str.format()` method 

# In[10]:


print('We are at the {} in {}!'.format('osur', 'Rennes'))


# In[11]:


print('From {0} to  {1}'.format('November 17', 'November 24'))


# In[12]:


print('It takes place at {place}'.format(place='Milon room'))


# In[13]:


import math
print('The value of PI is approximately {:.7g}.'.format(math.pi))


# ## Formatted string literals (Python 3.6)

# In[14]:


print(f'The value of PI is approximately {math.pi:.4f}.')


# In[15]:


name = "Fred"
print(f"He said his name is {name}.")
print(f"He said his name is {name!r}.")


# In[16]:


f"He said his name is {repr(name)}."  # repr() is equivalent to !r


# In[17]:


width, precision = 10, 4
value = 12.34567
print(f"result: {value:{width}.{precision}f}")  # nested fields


# In[18]:


from datetime import *
today = datetime(year=2017, month=1, day=27)
print(f"{today:%B %d, %Y}")  # using date format specifier


# # Exercise
# Create a list containing the values of [binomial coefficients](https://en.wikipedia.org/wiki/Binomial_coefficient) and reproduce the [Pascal's triangle](https://en.wikipedia.org/wiki/Pascal%27s_triangle)
# <pre>
#                  1  
#                1   1  
#              1   2   1  
#            1   3   3   1  
#          1   4   6   4   1  
#        1   5  10  10   5   1  
#      1   6  15  20  15   6   1  
#    1   7  21  35  35  21   7   1  
# </pre>
# 

# # Reading and Writing Files
# 
# `open()` returns a file object, and is most commonly used with file name and accessing mode argument.
# 

# In[19]:


f = open('workfile.txt', 'w')
f.write("1. This is a txt file.\n")
f.write("2. \\n is used to begin a new line")
f.close()
get_ipython().system('cat workfile.txt')


# `mode` can be :
# - 'r' when the file will only be read, 
# - 'w' for only writing (an existing file with the same name will be erased)
# - 'a' opens the file for appending; any data written to the file is automatically added to the end. 
# - 'r+' opens the file for both reading and writing. 
# - The mode argument is optional; 'r' will be assumed if it’s omitted.
# - Normally, files are opened in text mode.
# - 'b' appended to the mode opens the file in binary mode.

# In[20]:


with open('workfile.txt') as f:
    read_text = f.read()
f.closed


# In[21]:


read_text


# In[22]:


lines= []
with open('workfile.txt') as f:
    lines.append(f.readline())
    lines.append(f.readline())
    lines.append(f.readline())
    
lines


# - `f.readline()` returns an empty string when the end of the file has been reached.
# - `f.readlines()` or `list(f)` read all the lines of a file in a list.
# 
# For reading lines from a file, you can loop over the file object. This is memory efficient, fast, and leads to simple code:

# In[23]:


with open('workfile.txt') as f:
    for line in f:
        print(line, end='')


# ### Exercise: Wordcount Example
# 
# [WordCount](https://hadoop.apache.org/docs/current/hadoop-mapreduce-client/hadoop-mapreduce-client-core/MapReduceTutorial.html#Example:_WordCount_v1.0) is a simple application that counts the number of occurrences of each word in a given input set.
# 
# - Use lorem module to write a text in the file "sample.txt"
# - Write a function `words` with file name as input that returns a sorted list of words present in the file.
# - Write the function `reduce` to read the results of words and sum the occurrences of each word to a final count, and then output the results as a dictionary
# `{word1:occurences1, word2:occurences2}`.
# - You can check the results using piped shell commands:
# ```sh
# cat sample.txt | fmt -1 | tr [:upper:] [:lower:] | tr -d '.' | sort | uniq -c 
# ```

# In[27]:


from lorem import text

text()


# In[28]:


def words( file ):
    """ Parse a file and returns a sorted list of words """
    pass

words('sample.txt')
#[('adipisci', 1),
# ('adipisci', 1),
# ('adipisci', 1),
# ('aliquam', 1),
# ('aliquam', 1),


# In[29]:


d = {}
d['word1'] = 3
d['word2'] = 2
d


# In[21]:


def reduce ( words ):
    """ Count the number of occurences of a word in list
    and return a dictionary """
    pass

reduce(words('sample.txt'))
#{'neque': 80),
# 'ut': 80,
# 'est': 76,
# 'amet': 74,
# 'magnam': 74,
# 'adipisci': 73,


# # Saving structured data with json
# 
# - JSON (JavaScript Object Notation) is a popular data interchange format.
# - JSON format is commonly used by modern applications to allow for data exchange. 
# - JSON can be used to communicate with applications written in other languages.

# In[28]:


import json
json.dumps([1, 'simple', 'list'])


# In[29]:


x = dict(name="Pierre Navaro", organization="CNRS", position="IR")
with open('workfile.json','w') as f:
    json.dump(x, f)


# In[30]:


with open('workfile.json','r') as f:
    x = json.load(f)
x


# In[31]:


get_ipython().run_line_magic('cat', 'workfile.json')


# Use `ujson` for big data structures
# https://pypi.python.org/pypi/ujson
# 
