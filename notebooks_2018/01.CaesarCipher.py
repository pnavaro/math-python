#!/usr/bin/env python
# coding: utf-8

# # Caesar cipher
# 
# In cryptography, a Caesar cipher, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
# 
# ## Objectives
# 
# - Create a function `cipher` that take a plain text and the key value as arguments and return the encrypted text.
# ```py
# cipher("abcd gef", 1) == "bcde hij"
# ```

# ## String methods
# 
# - the method `lower()` returns the lowered string contained in variable word
# - the method `isalpha()` returns true if string has at least 1 character and all characters are alphabetic 

# In[28]:


word = "Bonjour"
word.lower(),word.isalpha()


# In[29]:


str.lower(word), str.isalpha(word)


# ### Exercise 1
# 
# - Display all strings methods by typing `<TAB>` key after the dot of `word.`,
# - Select the `word.replace` method,
# - Display documentation by typing `<shift>+<TAB>` keys after `word.replace`,
# - replace all character `o` by `O` by using `word.replace` method.

# In[32]:


word   # . and <TAB>


# In[33]:


word.replace  # shift+<TAB> 


# In[34]:


word.replace("o","O")


# alphabet string is available from the standard library string:

# In[153]:


import string

alphabet = string.ascii_lowercase
print(alphabet)


# In[154]:


from string import ascii_uppercase as ALPHABET

print(ALPHABET)


# ## Loop over an iterable object
# 
# We use `for` statement for looping over an iterable object. If we use it with a string, it loops over its characters.
# 
# https://docs.python.org/3.7/tutorial/controlflow.html#for-statements

# ## `if` Statements
# 
# `if` .. `elif`..`else`
# ```python
# True, False, and, or, not, ==, is, !=, is not, >, >=, <, <=, in
# ```
# https://docs.python.org/3.7/tutorial/controlflow.html#if-statements

# We need a `int_to_char` function that returns letter at shifted position.

# In[397]:


def int_to_char(n):
    """ ---------------------
        First Python function
        ---------------------
        
        return the alphabet character at position n modulo 26
    """
    return alphabet[n%26]


# In[398]:


help(int_to_char)


# ### Exercise  2
# 
# Create a function `char_to_int(c)` that returns the position of c in alphabet
# 
# *Algorithm*
# - If this character is an alpha character.
# - Loop over alphabet `while`  until this character is equal to the matching character in alphabet. Increment a counter to compute its position.
# - A function that does not explictely return a value, returns `None` 
# 
# https://docs.python.org/3.7/tutorial/controlflow.html#defining-functions 

# In[336]:


# %load solutions/caesar/ex02.py


# # `enumerate` Function
# 
# https://docs.python.org/3.7/tutorial/introduction.html#strings

# In[172]:


for i, c in enumerate("abcd"):
    print(i, " : ", c) 


# ### Exercise 3
# 
# Rewrite the `char_to_int` with a for loop
# 
# *Algorithm*
# - If input character is an alpha character.
# - Loop over enumerate(alphabet)  until input character is equal to the matching character in alphabet. 
# - Return the index (loop is stopped by `break` or `return` inside a function).
# 
# 

# In[346]:


# %load solutions/caesar/ex03.py


# ### Exercise 4
# 
# The `char_to_int` function can be improved by using the `str.index` method. Rewrite the function.

# In[347]:


print(str.index.__doc__)


# In[348]:


# %load solutions/caesar/ex04.py
def char_to_int(c):
    if c.isalpha():
        return alphabet.index(c)

char_to_int("e"), char_to_int(" ")


# ## String concatenation
# 
# https://docs.python.org/3.7/tutorial/introduction.html#strings

# In[349]:


s = ""
s += "a"
s *= 4
s


# ### Exercise 5
# 
# Improve again functions `char_to_int` and `int_to_char` by using Python functions `chr` and
# `ord`.

# In[350]:


for x in 'abcd':
    print(ord(x), ' \t ',chr(ord(x)))


# In[353]:


# %load solutions/caesar/ex05.py


# ### Exercise 6
# 
# Write a first version of the cipher function using both functions implemented above.
# 
# *Algorithm*
# - Create an empty string `s`.
# - For every character in input text do:
#     - compute position in alphabet with `char_to_int`
#     - if c is a character append the shifted character to `s`.
#     - else append the unchanged c character.
# - Return the string s

# In[ ]:


# %load solutions/caesar/ex06.py


# ## Python list
# 
# The function above works but we need to create a new string to cipher the plain text.
# Since the string is not mutable, the cell code below will throw an error.
# 
# https://docs.python.org/3.6/tutorial/introduction.html#lists

# In[304]:


word = "bonjour"
word[0] = "B"


# Let's use a Python list to cipher the text. We will no longer use functions `char_to_int` and `int_to_char`.
# Strings can be cast to list with `list` function or `str.split` method. The function `str.join` convert a list of characters to a string.

# In[305]:


word = list(word)
word


# In[306]:


'i am a pythonista!'.split()


# In[307]:


"".join(word)


# Here a version of the cipher function using a `for` loop and `str.index` function.

# In[308]:


alphabet.index("c") # returns the position of first "c" in alphabet string.


# In[309]:


def cipher(text, key=0):
    "Encrypt the `text` using the Caesar cipher technique. "
    res = ""
    for c in text:
        if c.isalpha():
            i = alphabet.index(c)
            res += alphabet[(i+key)%26]
        else:
            res += c
    
    return res

cipher('s kw k zidryxscdk!', 42)


# ### Exercise 7 
# 
# Rewrite the `cipher` function using Python list.
# 
# *Algorithm*
# - remove the `res` string
# - convert the `text` string to a python list
# - change every item of this list by its shifted version.
# - return the string converted from list using `str.join`

# In[ ]:


# %load solutions/caesar/ex07.py


# ## List comprehension
# 
# - Set or change values inside a list
# - Create list from function
# 
# https://docs.python.org/3.7/tutorial/datastructures.html#list-comprehensions

# In[311]:


lsingle = [1, 3, 9, 4]  # Create double version of single list
ldouble = []
for k in lsingle:
    ldouble.append(2*k)
ldouble


# In[312]:


ldouble = [k*2 for k in lsingle] # comprehension version


# In[313]:


[n*n for n in range(1,10)] # square from 1 to 9


# In[314]:


[n*n for n in range(1,10) if n&1] # square only if item is odd


# In[315]:


[3*n+1 if n&1 else n//2 for n in range(1,10) ]


# ### Exercise 8
# 
# Code a new version of cypher function using list comprehension. 
# 

# In[358]:


# %load solutions/caesar/ex08.py


# ## `map` built-in function
# 
# Apply a function over a sequence.
# 

# In[359]:


res = map(chr,range(97,123))
print(res)


# Since Python 3.x, `map` process return an iterator. Save memory, and should make things go faster.
# Display result by using unpacking operator.

# In[360]:


print(*res)


# ## `map` with user-defined function

# In[361]:


def add(x,y):
    return x+y

L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(*map(add,L1,L2))


# ### `map` is often faster than `for` loop

# In[362]:


M = range(10000)
f = lambda x: x**2
get_ipython().run_line_magic('timeit', 'lmap = map(f,M)')


# In[363]:


M = range(10000)
f = lambda x: x**2
get_ipython().run_line_magic('timeit', 'lfor = (f(m) for m in M)')


# ### Exercise 9
# 
# Code a new version of your cypher function using map. 
# 
# *Algorithm*:
# - create a function called `shift` that return the shifted character with the key value inside the cipher function
# - Applied function shift, must have only one argument.
# - use map to apply this shift function.
# - return the ciphered text

# In[366]:


# %load solutions/caesar/ex09.py


# ##  `dict`
# 
# https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries

# In[367]:


d = { c:i for (i,c) in enumerate("abcd")}
d


# In[368]:


d['b']


# In[369]:


d.keys()


# In[370]:


d.items()


# In[371]:


def cipher(text, key=0):
    
    "Encrypt the `text` using the Caesar cipher technique."
    
    a = { c:alphabet[(i+key)%26] for (i,c) in enumerate(alphabet)}
    
    return "".join((a[c] if c.isalpha() else c for c in text ))

cipher('s kw k zidryxscdk!', 42)


# ## `str.maketrans` and `str.translate`
# 
# https://docs.python.org/3.6/library/stdtypes.html?highlight=maketrans#str.maketrans

# In[372]:


def cipher(text, key=0):
    "Encrypt the `text` using the Caesar cipher technique."
    
    a = { c:alphabet[(i+key)%26] for (i,c) in enumerate(alphabet)}
    
    table = str.maketrans(a)
    
    return text.translate(table)

cipher('s kw k zidryxscdk!', 42)


# ## Create a latin text with `lorem` package 

# In[373]:


import sys
get_ipython().system('{sys.executable} -m pip install lorem')

import lorem

text = lorem.sentence()

print(text)


# ## Open and write a the file sample.txt

# In[381]:


from lorem import text
with open("sample.txt","w") as f:
    f.write(text())


# ## Open and read the file sample.txt

# In[383]:


with open("sample.txt") as f:
    data = f.read()
print(data)


# ## Homework
# 
# Write the cipher function with file name as input and key value. This function will:
# - Open and read the file.
# - Cipher the plain text (be careful there are upper case character this time)
# - Open and write the crypted text in the same file.
# - Don't forget the key 😉

# In[ ]:


# %load solutions/caesar/homework.py


# In[385]:


get_ipython().run_line_magic('cat', 'sample.txt')


# In[386]:


cipher("sample.txt",-1)


# In[387]:


get_ipython().run_line_magic('cat', 'sample.txt')


# In[ ]:




