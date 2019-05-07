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
#     display_name: Python3.7
#     language: python
#     name: python3
# ---

# %% [markdown]
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

# %% [markdown]
# ## String methods
#
# - the method `lower()` returns the lowered string contained in variable word
# - the method `isalpha()` returns true if string has at least 1 character and all characters are alphabetic 

# %%
word = "Bonjour"
word.lower(),word.isalpha()

# %%
str.lower(word), str.isalpha(word)

# %% [markdown]
# ### Exercise 1
#
# - Display all strings methods by typing `<TAB>` key after the dot of `word.`,
# - Select the `word.replace` method,
# - Display documentation by typing `<shift>+<TAB>` keys after `word.replace`,
# - replace all character `o` by `O` by using `word.replace` method.

# %%
word   # . and <TAB>

# %%
word.replace  # shift+<TAB> 

# %%
word.replace("o","O")

# %% [markdown]
# alphabet string is available from the standard library string:

# %%
import string

alphabet = string.ascii_lowercase
print(alphabet)

# %%
from string import ascii_uppercase as ALPHABET

print(ALPHABET)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Loop over an iterable object
#
# We use `for` statement for looping over an iterable object. If we use it with a string, it loops over its characters.
#
# https://docs.python.org/3.7/tutorial/controlflow.html#for-statements

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## `if` Statements
#
# `if` .. `elif`..`else`
# ```python
# True, False, and, or, not, ==, is, !=, is not, >, >=, <, <=, in
# ```
# https://docs.python.org/3.7/tutorial/controlflow.html#if-statements

# %% [markdown]
# We need a `int_to_char` function that returns letter at shifted position.

# %%
def int_to_char(n):
    """ ---------------------
        First Python function
        ---------------------
        
        return the alphabet character at position n modulo 26
    """
    return alphabet[n%26]


# %% {"slideshow": {"slide_type": "slide"}}
help(int_to_char)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
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

# %% {"slideshow": {"slide_type": "slide"}}
# %load solutions/caesar/ex02.py

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# # `enumerate` Function
#
# https://docs.python.org/3.7/tutorial/introduction.html#strings

# %% {"slideshow": {"slide_type": "fragment"}}
for i, c in enumerate("abcd"):
    print(i, " : ", c) 

# %% [markdown]
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

# %%
# %load solutions/caesar/ex03.py

# %% [markdown]
# ### Exercise 4
#
# The `char_to_int` function can be improved by using the `str.index` method. Rewrite the function.

# %%
print(str.index.__doc__)


# %%
# %load solutions/caesar/ex04.py
def char_to_int(c):
    if c.isalpha():
        return alphabet.index(c)

char_to_int("e"), char_to_int(" ")

# %% [markdown]
# ## String concatenation
#
# https://docs.python.org/3.7/tutorial/introduction.html#strings

# %%
s = ""
s += "a"
s *= 4
s

# %% [markdown]
# ### Exercise 5
#
# Improve again functions `char_to_int` and `int_to_char` by using Python functions `chr` and
# `ord`.

# %%
for x in 'abcd':
    print(ord(x), ' \t ',chr(ord(x)))

# %%
# %load solutions/caesar/ex05.py

# %% [markdown]
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

# %%
# %load solutions/caesar/ex06.py

# %% [markdown]
# ## Python list
#
# The function above works but we need to create a new string to cipher the plain text.
# Since the string is not mutable, the cell code below will throw an error.
#
# https://docs.python.org/3.6/tutorial/introduction.html#lists

# %%
word = "bonjour"
word[0] = "B"

# %% [markdown]
# Let's use a Python list to cipher the text. We will no longer use functions `char_to_int` and `int_to_char`.
# Strings can be cast to list with `list` function or `str.split` method. The function `str.join` convert a list of characters to a string.

# %%
word = list(word)
word

# %%
'i am a pythonista!'.split()

# %%
"".join(word)

# %% [markdown]
# Here a version of the cipher function using a `for` loop and `str.index` function.

# %%
alphabet.index("c") # returns the position of first "c" in alphabet string.


# %%
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

# %% [markdown]
# ### Exercise 7 
#
# Rewrite the `cipher` function using Python list.
#
# *Algorithm*
# - remove the `res` string
# - convert the `text` string to a python list
# - change every item of this list by its shifted version.
# - return the string converted from list using `str.join`

# %%
# %load solutions/caesar/ex07.py

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## List comprehension
#
# - Set or change values inside a list
# - Create list from function
#
# https://docs.python.org/3.7/tutorial/datastructures.html#list-comprehensions

# %% {"slideshow": {"slide_type": "fragment"}}
lsingle = [1, 3, 9, 4]  # Create double version of single list
ldouble = []
for k in lsingle:
    ldouble.append(2*k)
ldouble

# %% {"slideshow": {"slide_type": "fragment"}}
ldouble = [k*2 for k in lsingle] # comprehension version

# %% {"slideshow": {"slide_type": "slide"}}
[n*n for n in range(1,10)] # square from 1 to 9

# %% {"slideshow": {"slide_type": "fragment"}}
[n*n for n in range(1,10) if n&1] # square only if item is odd

# %% {"slideshow": {"slide_type": "fragment"}}
[3*n+1 if n&1 else n//2 for n in range(1,10) ]

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 8
#
# Code a new version of cypher function using list comprehension. 
#

# %%
# %load solutions/caesar/ex08.py

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## `map` built-in function
#
# Apply a function over a sequence.
#

# %% {"slideshow": {"slide_type": "fragment"}}
res = map(chr,range(97,123))
print(res)

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# Since Python 3.x, `map` process return an iterator. Save memory, and should make things go faster.
# Display result by using unpacking operator.

# %% {"slideshow": {"slide_type": "fragment"}}
print(*res)


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## `map` with user-defined function

# %% {"slideshow": {"slide_type": "fragment"}}
def add(x,y):
    return x+y

L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(*map(add,L1,L2))

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### `map` is often faster than `for` loop

# %% {"slideshow": {"slide_type": "fragment"}}
M = range(10000)
f = lambda x: x**2
%timeit lmap = map(f,M)

# %% {"slideshow": {"slide_type": "fragment"}}
M = range(10000)
f = lambda x: x**2
%timeit lfor = (f(m) for m in M)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 9
#
# Code a new version of your cypher function using map. 
#
# *Algorithm*:
# - create a function called `shift` that return the shifted character with the key value inside the cipher function
# - Applied function shift, must have only one argument.
# - use map to apply this shift function.
# - return the ciphered text

# %%
# %load solutions/caesar/ex09.py

# %% [markdown]
# ##  `dict`
#
# https://docs.python.org/3.6/tutorial/datastructures.html#dictionaries

# %%
d = { c:i for (i,c) in enumerate("abcd")}
d

# %%
d['b']

# %%
d.keys()

# %%
d.items()


# %%
def cipher(text, key=0):
    
    "Encrypt the `text` using the Caesar cipher technique."
    
    a = { c:alphabet[(i+key)%26] for (i,c) in enumerate(alphabet)}
    
    return "".join((a[c] if c.isalpha() else c for c in text ))

cipher('s kw k zidryxscdk!', 42)


# %% [markdown]
# ## `str.maketrans` and `str.translate`
#
# https://docs.python.org/3.6/library/stdtypes.html?highlight=maketrans#str.maketrans

# %%
def cipher(text, key=0):
    "Encrypt the `text` using the Caesar cipher technique."
    
    a = { c:alphabet[(i+key)%26] for (i,c) in enumerate(alphabet)}
    
    table = str.maketrans(a)
    
    return text.translate(table)

cipher('s kw k zidryxscdk!', 42)

# %% [markdown]
# ## Create a latin text with `lorem` package 

# %% {"slideshow": {"slide_type": "slide"}}
import sys
!{sys.executable} -m pip install lorem

import lorem

text = lorem.sentence()

print(text)

# %% [markdown]
# ## Open and write a the file sample.txt

# %%
from lorem import text
with open("sample.txt","w") as f:
    f.write(text())

# %% [markdown]
# ## Open and read the file sample.txt

# %%
with open("sample.txt") as f:
    data = f.read()
print(data)

# %% [markdown]
# ## Homework
#
# Write the cipher function with file name as input and key value. This function will:
# - Open and read the file.
# - Cipher the plain text (be careful there are upper case character this time)
# - Open and write the crypted text in the same file.
# - Don't forget the key 😉

# %%
# %load solutions/caesar/homework.py

# %%
%cat sample.txt

# %%
cipher("sample.txt",-1)

# %%
%cat sample.txt

# %%
