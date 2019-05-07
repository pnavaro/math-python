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
word = "bonjour"

# %% {"slideshow": {"slide_type": "fragment"}}
word

# %% {"slideshow": {"slide_type": "fragment"}}
word.capitalize()

# %% {"slideshow": {"slide_type": "fragment"}}
word.upper()

# %% {"slideshow": {"slide_type": "slide"}}
help(word.replace)

# %% {"slideshow": {"slide_type": "fragment"}}
word.replace('o','O',1)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Strings and `print` Function
# Strings can be enclosed in single quotes ('...') or double quotes ("...") with the same result. \ can be used to escape quotes:
#
#

# %% {"slideshow": {"slide_type": "fragment"}}
print('spam eggs')          # single quotes
print('doesn\'t')           # use \' to escape the single quote...
print("doesn't")            # ...or use double quotes instead
print('"Yes," he said.')    #
print("\"Yes,\" he said.")
print('"Isn\'t," she said.')

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# `print` function translates C special characters

# %% {"slideshow": {"slide_type": "fragment"}}
s = '\tFirst line.\nSecond line.'  # \n means newline \t inserts tab
print(s)  # with print(), \n produces a new line
print(r'\tFirst line.\nSecond line.')  # note the r before the quote

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # String literals with multiple lines

# %% {"slideshow": {"slide_type": "fragment"}}
print("""
Usage: thingy [OPTIONS]
     -h                        Display this usage message
     -H hostname               Hostname to connect to
""") 

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# \ character removes the initial newline.
#
# Strings can be concatenated (glued together) with the + operator, and repeated with *

# %% {"slideshow": {"slide_type": "fragment"}}
# 3 times 'un', followed by 'ium'
print(3 * 'un' + 'ium')

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Two or more string literals next to each other are automatically concatenated.

# %% {"slideshow": {"slide_type": "fragment"}}
text = ('Put several strings within parentheses '
         'to have them joined together.')
print(text)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Strings can be indexed, with the first character having index 0. There is no separate character type; a character is simply a string of size one

# %% {"slideshow": {"slide_type": "fragment"}}
word = 'Python'
print(word[0]) # character in position 0
print(word[5]) # character in position 5

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# Indices may also be negative numbers, to start counting from the right

# %% {"slideshow": {"slide_type": "fragment"}}
print(word[-1])  # last character
print(word[-2])  # second-last character

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Slicing Strings
# - Omitted first index defaults to zero, 
# - Omitted second index defaults to the size of the string being sliced.
# - Step can be set with the third index
#
#

# %% {"slideshow": {"slide_type": "fragment"}}
print(word[:2])  # character from the beginning to position 2 (excluded)
print(word[4:])  # characters from position 4 (included) to the end
print(word[-2:]) # characters from the second-last (included) to the end
print(word[::-1]) # This is the reversed string!

# %% {"slideshow": {"slide_type": "fragment"}}
word[::2]

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# Python strings cannot be changed — they are immutable.
# If you need a different string, you should create a new or use Lists.
#
#

# %% {"slideshow": {"slide_type": "fragment"}}
import traceback
try:
    word[0] = 'J'
except: 
    traceback.print_exc()

# %% {"slideshow": {"slide_type": "slide"}}
## Some string methods
print(word.startswith('P'))

# %% {"slideshow": {"slide_type": "fragment"}}
print(*(m for m in dir(word) if not m.startswith('_')) )

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# - Ask user to input a string.
# - Print out the string length.
# - Check if the last character is equal to the first character.
# - Check if this string contains only letters.
# - Check if this string is lower case.
# - Check if this string is a palindrome. A palindrome is a word, phrase, number, or other sequence of characters which reads the same backward as forward.

# %% {"slideshow": {"slide_type": "fragment"}}
# %load ../solutions/strings.py
