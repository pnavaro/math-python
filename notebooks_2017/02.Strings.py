#!/usr/bin/env python
# coding: utf-8

# In[1]:


word = "bonjour"


# In[2]:


word


# In[3]:


word.capitalize()


# In[4]:


word.upper()


# In[5]:


help(word.replace)


# In[6]:


word.replace('o','O',1)


# # Strings and `print` Function
# Strings can be enclosed in single quotes ('...') or double quotes ("...") with the same result. \ can be used to escape quotes:
# 
# 

# In[7]:


print('spam eggs')          # single quotes
print('doesn\'t')           # use \' to escape the single quote...
print("doesn't")            # ...or use double quotes instead
print('"Yes," he said.')    #
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')


# `print` function translates C special characters

# In[8]:


s = '\tFirst line.\nSecond line.'  # \n means newline \t inserts tab
print(s)  # with print(), \n produces a new line
print(r'\tFirst line.\nSecond line.')  # note the r before the quote


# # String literals with multiple lines

# In[9]:


print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") 


# \ character removes the initial newline.
# 
# Strings can be concatenated (glued together) with the + operator, and repeated with *

# In[10]:


# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')


# Two or more string literals next to each other are automatically concatenated.

# In[11]:


text = ('Put several strings within parentheses '
         'to have them joined together.')
print(text)


# Strings can be indexed, with the first character having index 0. There is no separate character type; a character is simply a string of size one

# In[12]:


word = 'Python'
print(word[0]) # character in position 0
print(word[5]) # character in position 5


# Indices may also be negative numbers, to start counting from the right

# In[13]:


print(word[-1])  # last character
print(word[-2])  # second-last character


# # Slicing Strings
# - Omitted first index defaults to zero, 
# - Omitted second index defaults to the size of the string being sliced.
# - Step can be set with the third index
# 
# 

# In[14]:


print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end
print(word[::-1]) # This is the reversed string!


# In[15]:


word[::2]


# Python strings cannot be changed — they are immutable.
# If you need a different string, you should create a new or use Lists.
# 
# 

# In[16]:


import traceback
try:
    word[0] = 'J'
except: 
    traceback.print_exc()


# In[17]:


## Some string methods
print(word.startswith('P'))


# In[18]:


print(*(m for m in dir(word) if not m.startswith('_')) )


# ### Exercise
# 
# - Ask user to input a string.
# - Print out the string length.
# - Check if the last character is equal to the first character.
# - Check if this string contains only letters.
# - Check if this string is lower case.
# - Check if this string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

# In[19]:


# %load ../solutions/strings.py

