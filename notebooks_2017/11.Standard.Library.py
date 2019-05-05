#!/usr/bin/env python
# coding: utf-8

# # Standard Library
# 
# ## Operating System Interface
# 

# In[2]:


import os
os.getcwd()      # Return the current working directory


# In[3]:


get_ipython().run_line_magic('env', "CC='/usr/local/bin/gcc-8'")
os.environ['CC']='/usr/local/bin/gcc-8' # Change the default C compiler to gcc-7
os.system('mkdir today') # Run the command mkdir in the system shell


# In[4]:


os.chdir('today')   # Change current working directory
os.system('touch data.db') # Create the empty file data.db


# In[5]:


import shutil
shutil.copyfile('data.db', 'archive.db')
if os.path.exists('backup.db'):  # If file backup.db exists
    os.remove('backup.db')       # Remove it
shutil.move('archive.db', 'backup.db',)
shutil.os.chdir('..')


# ## File Wildcards
# 
# The glob module provides a function for making file lists from directory wildcard searches:

# In[6]:


import glob
glob.glob('*.py')


# In[7]:


def recursive_replace( root, pattern, replace ) :
    """
    Function to replace a string inside a directory
    root : directory
    pattern : searched string
    replace "pattern" by "replace"
    """
    for directory, subdirs, filenames in os.walk( root ):
      for filename in filenames:
        path = os.path.join( directory, filename )
        text = open( path ).read()
        if pattern in text:
          print('occurence in :' + filename)
          open(path,'w').write( text.replace( pattern, replace ) )


# # Command Line Arguments
# 
# These arguments are stored in the sys module’s argv attribute as a list.

# In[1]:


get_ipython().run_cell_magic('file', 'demo.py', 'import sys\nprint(sys.argv)')


# In[2]:


get_ipython().run_line_magic('run', 'demo.py one two three')


# # Random

# In[10]:


import random
random.choice(['apple', 'pear', 'banana'])


# In[11]:


random.sample(range(100), 10)   # sampling without replacement


# In[12]:


random.random()    # random float


# In[13]:


random.randrange(6)    # random integer chosen from range(6)


# # Statistics

# In[14]:


import statistics
data = [2.75, 1.75, 1.25, 0.25, 0.5, 1.25, 3.5]
statistics.mean(data)


# In[15]:


statistics.median(data)


# In[16]:


statistics.variance(data)


# # Performance Measurement
# 

# In[17]:


from timeit import Timer
Timer('t=a; a=b; b=t', 'a=1; b=2').timeit()


# In[18]:


Timer('a,b = b,a', 'a=1; b=2').timeit()


# In[19]:


get_ipython().run_cell_magic('timeit', 'a=1; b=2', 'a,b = b,a')


# The [profile](https://docs.python.org/3/library/profile.html#module-profile) and [pstats](https://docs.python.org/3/library/profile.html#module-pstats) modules provide tools for identifying time critical sections in larger blocks of code.

# # Quality Control
# 
# One approach for developing high quality software is to write tests for each function.
# 
# - The doctest module provides a tool for scanning a module and validating tests embedded in a program’s docstrings. 
# - This improves the documentation by providing the user with an example and it allows the doctest module to make sure the code remains true to the documentation:

# In[20]:


def average(values):
    """Computes the arithmetic mean of a list of numbers.

    >>> print(average([20, 30, 70]))
    40.0
    """
    return sum(values) / len(values)

import doctest
doctest.testmod()   # automatically validate the embedded tests


# ## Python’s standard library is very extensive
# - Containers and iterators: `collections`, `itertools`
# - Internet access: `urllib, email, mailbox, cgi, ftplib`
# - Dates and Times: `datetime, calendar, `
# - Data Compression: `zlib, gzip, bz2, lzma, zipfile, tarfile`
# - File formats: `csv, configparser, netrc, xdrlib, plistlib` 
# - Cryptographic Services: `hashlib, hmac, secrets`
# - Structure Markup Processing Tools: `html, xml`
# 
# Check the [The Python Standard Library](https://docs.python.org/3/library/index.html)
