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

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Python Lists and tuples
#
# - List is the most versatile Python data type to group values with others
# - Can be written as a list of comma-separated values (items) between square brackets. 
# - Tuples are written between parenthesis. They are read-only lists.
# - Lists can contain items of different types.
# - Like strings, lists can be indexed and sliced.
# - Lists also support operations like concatenation.
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Indexing

# %% {"slideshow": {"slide_type": "fragment"}}
squares = [1, 4, 9, 16, 25]
print(squares)

# %% {"slideshow": {"slide_type": "fragment"}}
print(squares[0])  # indexing returns the item

# %% {"slideshow": {"slide_type": "fragment"}}
print(squares[-1])

# %% {"slideshow": {"slide_type": "fragment"}}
print(squares[-3:]) # slicing returns a new list

# %% {"slideshow": {"slide_type": "fragment"}}
squares += [36, 49, 64, 81, 100]
print(squares)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Unlike strings, which are immutable, lists are a mutable type.

# %% {"slideshow": {"slide_type": "fragment"}}
cubes = [1, 8, 27, 65, 125]  # something's wrong here  
cubes[3] = 64  # replace the wrong value, the cube of 4 is 64, not 65!
print(cubes)

# %% {"slideshow": {"slide_type": "fragment"}}
cubes.append(216)  # add the cube of 6
print(cubes)

# %% {"slideshow": {"slide_type": "fragment"}}
cubes.remove(1)
print(cubes)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Assignment 
#
# - You can change the size of the list or clear it entirely.
# - The built-in function len() returns list size.
# - It is possible to create lists containing other lists.

# %% {"slideshow": {"slide_type": "fragment"}}
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E'] # replace some values
print(letters)

# %% {"slideshow": {"slide_type": "fragment"}}
letters[2:5] = [] # now remove them
print(letters)

# %% {"slideshow": {"slide_type": "slide"}}
a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]

# %% {"slideshow": {"slide_type": "fragment"}}
x

# %% {"slideshow": {"slide_type": "fragment"}}
x[0]

# %% {"slideshow": {"slide_type": "fragment"}}
x[0][1], len(x)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Assignment, Copy and Reference

# %% {"slideshow": {"slide_type": "fragment"}}
a = [0, 1, 2, 3, 4]
b = a
print("b = ",b)

# %% {"slideshow": {"slide_type": "fragment"}}
b[1]= 20        # Change one value in b
print("a = ",a) # Y

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# **b is a reference to a, they occupy same space memory**

# %% {"slideshow": {"slide_type": "fragment"}}
b = a[:] # assign a slice of a and you create a new list
b[2]=10
print("b = ",b)
print("a = ",a)   

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Some useful List Methods

# %% {"slideshow": {"slide_type": "fragment"}}
a = list("python-2018")
a

# %% {"slideshow": {"slide_type": "fragment"}}
a.sort()
a

# %% {"slideshow": {"slide_type": "fragment"}}
a.reverse()
a

# %% {"slideshow": {"slide_type": "fragment"}}
a.pop() #pop the last item and remove it from the list
a

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Dictionary
#
# They are indexed by keys, which are often strings.

# %% {"slideshow": {"slide_type": "fragment"}}
person = dict(name="John Smith", email="john.doe@domain.fr")
person['size'] = 1.80
person['weight'] = 70

# %% {"slideshow": {"slide_type": "fragment"}}
person

# %% {"slideshow": {"slide_type": "fragment"}}
print(person.keys())

# %% {"slideshow": {"slide_type": "fragment"}}
print(person.items())

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# - Split the string "python LILLE 2018" into the list ["python","LILLE", 2018]
# - Insert "april" and value 10 before 2018 in the result list.
# - Capitalize the first item to "Python"
# - Create a dictionary with following keys (meeting, month, day, year)
# - Print out the items.
# - Append the key "place" to this dictionary and set the value to "LILLE".
# ```python
# ['python', 'LILLE', '2018']
# ['python', 'LILLE', 'april', 10, '2018']
# ['Python', 'LILLE', 'april', 10, '2018']
# {'course': 'Python','month': 'april','day': 10,'year': '2018','place': 'LILLE'}
#  ```
