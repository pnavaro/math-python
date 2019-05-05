#!/usr/bin/env python
# coding: utf-8

# # Errors and Exceptions
# 
# There are two distinguishable kinds of errors: *syntax errors* and *exceptions*.
# - Syntax errors, also known as parsing errors, are the most common.
# - Exceptions are errors caused by statement or expression syntactically corrects.
# - Exceptions are not unconditionally fatal.
# 
# [Exceptions in Python documentation](https://docs.python.org/3/library/exceptions.html)

# In[1]:


10 * (1/0)


# In[2]:


4 + spam*3


# In[3]:


'2' + 2


# # Handling Exceptions
# 
# - In example below, the user can interrupt the program with `Control-C` or the `stop` button in Jupyter Notebook.
# - Note that a user-generated interruption is signalled by raising the **KeyboardInterrupt** exception.
# 

# In[7]:


while True:
   try:
     x = int(input("Please enter a number: "))
     print(f' x = {x}')
     break
   except ValueError:
     print("Oops!  That was no valid number.  Try again...")


# - A try statement may have more than one except clause
# - The optional `else` clause must follow all except clauses.

# In[8]:


import sys

def process_file(file):
    try:
        i = int(open(file).readline().strip()) # Read the first line of f and convert to int
        print(i)
        assert i < 0 # check if i is negative
    except OSError as err:
        print(f"OS error: {err}")
    except ValueError:
        print("Could not convert data to an integer.")
    except:
        print("Unexpected error:", sys.exc_info()[0])

# Create the file workfile.txt
with open('workfile.txt','w') as f:
    f.write("foo")
    f.write("bar")


# In[9]:


process_file('workfile.txt') # catch exception return by int() call


# In[10]:


# Change permission of the file, workfile.txt cannot be read
get_ipython().system('chmod u-r workfile.txt')


# In[11]:


process_file('workfile.txt') # catch exception return by open() call


# In[12]:


# Let's delete the file workfile.txt
get_ipython().system('rm -f workfile.txt')


# In[13]:


process_file('workfile.txt') # catch another exception return by open() call


# In[14]:


# Insert the value 1 at the top of workfile.txt
get_ipython().system('echo "1" > workfile.txt')
get_ipython().run_line_magic('cat', 'workfile.txt')


# In[15]:


process_file('workfile.txt') # catch excepion return by assert()


# # Raising Exceptions
# 
# The raise statement allows the programmer to force a specified exception to occur.
# 

# In[16]:


raise NameError('HiThere')


# # Defining Clean-up Actions
# 
# - The try statement has an optional clause which is intended to define clean-up actions that must be executed under all circumstances.
# 
# - A finally clause is always executed before leaving the try statement

# In[17]:


try:
     raise KeyboardInterrupt
finally:
     print('Goodbye, world!')


# ### Exercise
# 
# - Write a function `check_date` that takes a string "DD/MM/YYYY" as argument and
# returns `True` if the date is valid.
# - Use it with a `try ... except` statement to help the user to enter a valid date.
# - raise ValueError "Not a valid date"
# - Hints: 
#   * Use string method `split`
#   * Year y is a leap year if y%400==0 or (y%4==0 and y%100!=0)
# 

# ### Wordcount Exercise
# - Improve the function `reduce` to read the results of `words` by using the `KeyError` exception to fill in the dictionary.
#  
