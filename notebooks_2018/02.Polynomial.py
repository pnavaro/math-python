#!/usr/bin/env python
# coding: utf-8

# # Recursive Call

# In[1]:


def factorial(n):
    " Compute factorial with recursive call "
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial(4)


# In[2]:


def gcd(x, y): 
    """ returns the greatest common divisor."""
    if x == 0: 
        return y
    else: 
        return gcd(y % x, x)

gcd(12,16)


# ### Exercise: Polynomial derivative
# - A Polynomial is represented by a Python list of its coefficients.
#     [1,5,-4] => $1+5x-4x^2$
# - Write the function diff(P,n) that return the nth derivative Q
# ```
# diff([3,2,1,5,7],2) = [2, 30, 84]
# diff([-6,5,-3,-4,3,-4],3) = [-24, 72, -240]
# ```

# In[3]:


def diff(P, n):
    for d in range(n):
        Q = P.copy()
        if (len(Q) > 1):
            P = [ (e+1)*c for e,c in enumerate(Q[1:])]
        else:
            return [0]
    return P



diff([1, 2, 3], 2)


# In[4]:


# %load ../notebooks_2017/solutions/control_flow_tools/polynomial_diff.py
def diff(p, n):
    """ Return the nth derivative of polynom P """
    if n == 0:
        return p
    else:
        return diff([i * p[i] for i in range(1, len(p))], n - 1)


print(diff([3, 2, 1, 5, 7], 2))
print(diff([-6, 5, -3, -4, 3, -4], 3))


# In[5]:


s = 3.14
type(s)


# In[ ]:





# # Classes
# - Classes provide a means of bundling data and functionality together.
# - Creating a new class creates a **new type** of object.
# - Assigned variables are new **instances** of that type.
# - Each class instance can have **attributes** attached to it.
# - Class instances can also have **methods** for modifying its state.
# - Python classes provide the class **inheritance** mechanism.
# 

# # Use class to store data
# 
# - A empty class can be used to bundle together a few named data items. 

# In[6]:


class Polynomial:
    pass

p = Polynomial()  # Create an empty Polynomial record

p.degree = 2
p.coeffs = [1,-2,3]


# In[7]:


p.__dict__


# # namedtuple

# In[8]:


from collections import namedtuple

Polynomial = namedtuple('Polynomial', 'degree, coeffs')


# In[9]:


p = Polynomial( 2, [1, -2, 3])
p


# In[10]:


# Like tuples, namedtuples are immutable:

p.degree = 3


# In[18]:


class Polynomial:

    "A simple example class representing a Polynomial"
    
    day = "Monday"

    def __init__(self, coeffs):  # constructor
        self.coeffs = coeffs
        
    def degree(self):           
        return len(self.coeffs)-1
    
    def diff(self, n):
        """ Return the nth derivative """
        coeffs = self.coeffs[:]
        for k in range(n):
            coeffs = [i * coeffs[i] for i in range(1, len(coeffs))]
        self.coeffs = coeffs[:]
    
    def __repr__(self):
        return "+".join([str(c)+"x^"+str(e) for e,c in enumerate(self.coeffs)])
    
    def __call__(self, x):
        return sum([ c*x**(e) for e,c in enumerate(self.coeffs)])

p = Polynomial([1, -2, 3, 7, 11, 6, 4])
p.degree(), p.coeffs

print(p)
print(p.diff(2))
#p(2)
#p.day = "Tuesday"
#p.day
print(p)


# ### Exercise
# 
# Add the `diff` function inside the `Polynomial` class.
# 
# ```python
# >>> p = Polynomial([1, -2, 3])
# >>> p.diff(2)
# 6
# ```

# # Convert method to attribute
# 
# Use the `property` decorator 

# In[20]:


class Polynomial:

    "A simple example class representing a Polynomial"

    def __init__(self, coeffs):  # constructor
        self.coeffs = coeffs

    @property
    def degree(self):  # method
        return len(self.coeffs)-1


# In[21]:


p = Polynomial([1, -2, 3])

p.degree


# In[22]:


p


# # The new Python 3.7 DataClass

# In[23]:


from dataclasses import dataclass
from typing import List

@dataclass
class Polynomial:

    coeffs: List

    @property
    def degree(self):
        return len(self.coeffs)-1


# In[25]:


q = Polynomial([-1, -4, 2, 3])
q.coeffs


# In[26]:


print(q)


# # Method Overriding
# - Every Python classes has a `__repr__()` method used when you call `print()` function.

# In[38]:


x = 10
y = 2

print(f" {x:+05d} + {y:5.2e} = {x+y:5.2f} ")


# In[55]:


class Polynomial:
    """Simple example class with method overriding """

    def __init__(self, coeffs):
        self.coeffs = coeffs

    def __repr__(self):
        output = ""
        for e,c in enumerate(self.coeffs):
            if e > 0:
                output += f" {c:+d}x^{e} "
            else:
                output += f" {c:+d} "
            
        return output

    @property
    def degree(self):
        return len(self.coeffs)-1


# In[56]:


q = Polynomial([-3, -2, -1, 1])
print(q)


# ### Exercise
# 
# Change the `__repr__` method to improve the print the Polynomial
# 
# ```python
# >>> q = Polynomial([1,2,3,4,5])
# >>> print(q)
# +1 +2x^1 +3x^2 +4x^3 +5x^4
# ```

# # Inheritance

# In[66]:


from datetime import datetime

class Person():  # Parent class is defined here

    def __init__(self, name, birthdate):
        self.name = name
        b = list(map(int,birthdate.split('/')))
        self.birthdate  = datetime(*b[::-1])
        
    @property
    def age( self ):
        _age = datetime.now() - self.birthdate
        return abs(_age)

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age})"

    

pierre = Person('Navaro', '04/02/1972')
print(pierre)
pierre.age


# In[67]:


class Agent(Person):
    
    def __init__(self, name, birthdate, phone):
        
        super().__init__(name, birthdate)
        self.phone = phone
        
Marie = Agent("Verger", "04/04/1978", 4308)


# In[68]:


Marie.age
print(Marie)


# ### Exercise: Rectangle and Square
# - Create two classes to represent a Square and a Rectangle.
# - Add a method to compute Area
# - Override the print function to draw them using ascii art.
# ```py
# >>> print(Rectangle(4,10))
# ##########
# ##########
# ##########
# ##########
# >>> print(Square(4))
# ####
# ####
# ####
# ####
# ```
# 

# In[73]:


class Rectangle():  # Parent class is defined here

    def __init__(self, width, height):
        assert int(width) == width
        assert int(height) == height
        self.width = width
        self.height = height
        
    @property
    def area( self ):
        return self.width * self.height

    def __repr__(self):
        output = ""
        for i in range(self.height):
            for j in range(self.width):
                output += "#"
            output += "\n"
            
        return output

class Square(Rectangle):
    
    def __init__(self, edge):
        super().__init__(edge, edge)
        
        

r = Rectangle(10, 4)
s = Square(5)
s


# # Private Variables and Methods

# In[74]:


class DemoClass:
    " Demo class for name mangling "

    def public_method(self):
        return 'public!'

    def __private_method(self):  # Note the use of leading underscores
        return 'private!'


object3 = DemoClass()


# In[75]:


object3.public_method()


# In[78]:


object3.__private_method()


# In[79]:


dir(object3)


# In[28]:


[ s for s in dir(object3) if "method" in s]


# In[80]:


object3._DemoClass__private_method()


# In[30]:


object3.public_method


# # Use `class` as a Function.

# In[81]:


class Polynomial:
    
   " Class representing a polynom P(x) -> c_0+c_1*x+c_2*x^2+..."
    
   def __init__(self, coeffs):
      self.coeffs = coeffs
        
   def __call__(self, x):
      return sum([coef*x**exp for exp,coef in enumerate(self.coeffs)])

p = Polynomial([2,4,-1])
p(2) 


# ### Exercise: Polynomial
# 
# - Improve the class above called Polynomial by creating a method `diff(n)` to compute the nth derivative.
# - Override the `__repr__()` method to output a pretty printing.
# 
# Hint: `f"{coeff:+d}"` forces to print sign before the value of an integer.

# # Operators Overriding 

# ## Rational example

# In[12]:


class Rational:
    " Class representing a rational number"

    def __init__(self, n, d):
        assert isinstance(n, int) and isinstance(d, int)

        def gcd(x, y):
            if x == 0:
                return y
            elif x < 0:
                return gcd(-x, y)
            elif y < 0:
                return -gcd(x, -y)
            else:
                return gcd(y % x, x)

        g = gcd(n, d)
        self.n, self.d = n//g, d//g

    def __add__(self, other):
        return Rational(self.n * other.d + other.n * self.d,
                        self.d * other.d)

    def __sub__(self, other):
        return Rational(self.n * other.d - other.n * self.d,
                        self.d * other.d)

    def __mul__(self, other):
        return Rational(self.n * other.n, self.d * other.d)

    def __truediv__(self, other):
        return Rational(self.n * other.d, self.d * other.n)

    def __repr__(self):
        return f"{self.n:d}/{self.d:d}"


# In[13]:


r1 = Rational(2,3)
r2 = Rational(3,4)
r1+r2, r1-r2, r1*r2, r1/r2


# ### Exercise 
# Improve the class Polynomial by implementing operations:
# - Overrides '==' operator (__eq__)
# - Overrides '+' operator (__add__)
# - Overrides '-' operator (__neg__)
# - Overrides '*' operator (__mul__)

# In[101]:


from operator import add
from itertools import zip_longest

class Polynomial:
    
    " Class representing a polynom P(x) -> c_0+c_1*x+c_2*x^2+..."
     
    def __init__(self, coeffs):
       self.coeffs = coeffs
    
    @property
    def degree(self):
        return len(self.coeffs)-1
         
    def __add__(self, other):
        return Polynomial([c + q for c, q in zip_longest(other.coeffs, self.coeffs, fillvalue=0)])
        

        
    def __repr__(self):
        output = ""
        for e,c in enumerate(self.coeffs):
            if e > 0:
                output += f" {c:+d}x^{e} "
            else:
                output += f" {c:+d} "
            
        return output
    

    
p1 = Polynomial([2,3,1,3])
p2 = Polynomial([3,4])
p1+p2


# In[99]:


from itertools import zip_longest

l1 = [ 1, 2, 3, 4]
l2 = [ 2, 1, 5, 6, 7, 8]

for i1, i2 in zip_longest(l1, l2, fillvalue=0):
    print(i1, '--', i2)
    
zip_longest


# # Iterators
# Most container objects can be looped over using a for statement:

# In[15]:


for element in [1, 2, 3]:
    print(element, end=' ')


# In[102]:


for element in (1, 2, 3):
    print(element, end=' ')


# In[103]:


for key in {'one': 1, 'two': 2}:
    print(key, end=' ')


# In[104]:


for key, value in {'one': 1, 'two': 2}.items():
    print(key, value)


# In[105]:


for char in "123":
    print(char, end=' ')


# In[106]:


for line in open("../binder/environment.yml"):
    print(line.strip(), end=',')


# - The `for` statement calls `iter()` on the container object. 
# - The function returns an iterator object that defines the method `__next__()`
# - To add iterator behavior to your classes: 
#     - Define an `__iter__()` method which returns an object with a `__next__()`.
#     - If the class defines `__next__()`, then `__iter__()` can just return self.
#     - The **StopIteration** exception indicates the end of the loop.

# In[108]:


s = 'abcdefgh'
it = iter(s)
it


# In[112]:


next(it), next(it), next(it), 


# In[113]:


it


# In[114]:


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


# In[115]:


rev = Reverse('spam')
for char in rev:
    print(char, end='')


# # Generators
# - Generators are a simple and powerful tool for creating iterators.
# - Write regular functions but use the yield statement when you want to return data.
# - the `__iter__()` and `__next__()` methods are created automatically.
# 

# In[118]:


def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# In[119]:


for char in reverse('bulgroz'):
     print(char, end='')


# In[120]:


def reverse(data): # Python 3.6
    yield from data[::-1]
    
for char in reverse('bulgroz'):
     print(char, end='')


# # Generator Expressions
# 
# - Use a syntax similar to list comprehensions but with parentheses instead of brackets.
# - Tend to be more memory friendly than equivalent list comprehensions.

# In[129]:


data = [i for i in range(10)]

iterateur_on_data = ( i**2 for i in data)

for x in iterateur_on_data:
    print(x)


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
