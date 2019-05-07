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
# # Iterators
# Most container objects can be looped over using a for statement:

# %% {"slideshow": {"slide_type": "slide"}}
for element in [1, 2, 3]:
    print(element, end=' ')

# %% {"slideshow": {"slide_type": "slide"}}
for element in (1, 2, 3):
    print(element, end=' ')

# %% {"slideshow": {"slide_type": "slide"}}
for key in {'one': 1, 'two': 2}:
    print(key, end=' ')

# %% {"slideshow": {"slide_type": "slide"}}
for char in "123":
    print(char, end=' ')

# %% {"slideshow": {"slide_type": "slide"}}
for line in open("../binder/environment.yml"):
    print(line.strip(), end=',')

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# - The `for` statement calls `iter()` on the container object. 
# - The function returns an iterator object that defines the method `__next__()`
# - To add iterator behavior to your classes: 
#     - Define an `__iter__()` method which returns an object with a `__next__()`.
#     - If the class defines `__next__()`, then `__iter__()` can just return self.
#     - The **StopIteration** exception indicates the end of the loop.

# %% {"slideshow": {"slide_type": "fragment"}}
s = 'abc'
it = iter(s)
it

# %% {"slideshow": {"slide_type": "fragment"}}
next(it), next(it), next(it)


# %% {"slideshow": {"slide_type": "slide"}}
class Reverse:
    """Iterator for looping over a sequence backwards."""

    def __init__(self, data):
        self.data = data
        self.index = len(data)

    def __iter__(self):
        return self

    def __next__(self):
        if self.index == 0:
            raise StopIteration
        self.index = self.index - 1
        return self.data[self.index]


# %% {"slideshow": {"slide_type": "fragment"}}
rev = Reverse('spam')
for char in rev:
    print(char, end='')


# %% {"slideshow": {"slide_type": "slide"}}
def reverse(data): # Python 3.6
    yield from data[::-1]
    
for char in reverse('bulgroz'):
     print(char, end='')


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Generators
# - Generators are a simple and powerful tool for creating iterators.
# - Write regular functions but use the yield statement when you want to return data.
# - the `__iter__()` and `__next__()` methods are created automatically.
#

# %% {"slideshow": {"slide_type": "fragment"}}
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# %% {"slideshow": {"slide_type": "fragment"}}
for char in reverse('bulgroz'):
     print(char, end='')

# %% [markdown]
# ### Exercise 
#
# Generates a list of IP addresses based on IP range. 
#
# ```python
# ip_range = 
# for ip in ip_range("192.168.1.0", "192.168.1.10"):
#    print(ip)
#
# 192.168.1.0
# 192.168.1.1
# 192.168.1.2
# ...
# ```

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Generator Expressions
#
# - Use a syntax similar to list comprehensions but with parentheses instead of brackets.
# - Tend to be more memory friendly than equivalent list comprehensions.

# %% {"slideshow": {"slide_type": "fragment"}}
sum(i*i for i in range(10))                 # sum of squares

# %% {"slideshow": {"slide_type": "fragment"}}
%load_ext memory_profiler

# %% {"slideshow": {"slide_type": "fragment"}}
%memit doubles = [2 * n for n in range(10000)]

# %% {"slideshow": {"slide_type": "fragment"}}
%memit doubles = (2 * n for n in range(10000))

# %% {"slideshow": {"slide_type": "slide"}}
# list comprehension
doubles = [2 * n for n in range(10)]
for x in doubles:
    print(x, end=' ')

# %% {"slideshow": {"slide_type": "fragment"}}
# generator expression
doubles = (2 * n for n in range(10))
for x in doubles:
    print(x, end=' ')

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# The [Chebyshev polynomials](https://en.wikipedia.org/wiki/Chebyshev_polynomials) of the first kind are defined by the recurrence relation
#
# $$
# \begin{eqnarray}
# T_o(x) &=& 1 \\
# T_1(x) &=& x \\
# T_{n+1} &=& 2xT_n(x)-T_{n-1}(x)
# \end{eqnarray}
# $$
#
# - Create a class `Chebyshev` that generates the sequence of Chebyshev polynomials
