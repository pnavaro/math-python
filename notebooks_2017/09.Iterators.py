#!/usr/bin/env python
# coding: utf-8

# # Iterators
# Most container objects can be looped over using a for statement:

# In[1]:


for element in [1, 2, 3]:
    print(element, end=' ')


# In[2]:


for element in (1, 2, 3):
    print(element, end=' ')


# In[3]:


for key in {'one': 1, 'two': 2}:
    print(key, end=' ')


# In[4]:


for char in "123":
    print(char, end=' ')


# In[5]:


for line in open("../binder/environment.yml"):
    print(line.strip(), end=',')


# - The `for` statement calls `iter()` on the container object. 
# - The function returns an iterator object that defines the method `__next__()`
# - To add iterator behavior to your classes: 
#     - Define an `__iter__()` method which returns an object with a `__next__()`.
#     - If the class defines `__next__()`, then `__iter__()` can just return self.
#     - The **StopIteration** exception indicates the end of the loop.

# In[6]:


s = 'abc'
it = iter(s)
it


# In[7]:


next(it), next(it), next(it)


# In[8]:


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


# In[9]:


rev = Reverse('spam')
for char in rev:
    print(char, end='')


# In[10]:


def reverse(data): # Python 3.6
    yield from data[::-1]
    
for char in reverse('bulgroz'):
     print(char, end='')


# # Generators
# - Generators are a simple and powerful tool for creating iterators.
# - Write regular functions but use the yield statement when you want to return data.
# - the `__iter__()` and `__next__()` methods are created automatically.
# 

# In[11]:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# In[12]:


for char in reverse('bulgroz'):
     print(char, end='')


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

# # Generator Expressions
# 
# - Use a syntax similar to list comprehensions but with parentheses instead of brackets.
# - Tend to be more memory friendly than equivalent list comprehensions.

# In[13]:


sum(i*i for i in range(10))                 # sum of squares


# In[14]:


get_ipython().run_line_magic('load_ext', 'memory_profiler')


# In[15]:


get_ipython().run_line_magic('memit', 'doubles = [2 * n for n in range(10000)]')


# In[16]:


get_ipython().run_line_magic('memit', 'doubles = (2 * n for n in range(10000))')


# In[17]:


# list comprehension
doubles = [2 * n for n in range(10)]
for x in doubles:
    print(x, end=' ')


# In[18]:


# generator expression
doubles = (2 * n for n in range(10))
for x in doubles:
    print(x, end=' ')


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
