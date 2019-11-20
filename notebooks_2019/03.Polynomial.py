# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.3
#   kernelspec:
#     display_name: Python 3.7
#     language: python
#     name: python3
# ---

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Recursive Call

# +
def factorial(n):
    " Compute factorial with recursive call "
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)
    
factorial(4)


# + {"slideshow": {"slide_type": "fragment"}}
def gcd(x, y): 
    """ returns the greatest common divisor."""
    if x == 0: 
        return y
    else: 
        return gcd(y % x, x)

gcd(12,16)


# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Exercise: Polynomial derivative
# - A Polynomial is represented by a Python list of its coefficients.
#     [1,5,-4] => $1+5x-4x^2$
# - Write the function diff(P,n) that return the nth derivative Q
# ```
# diff([3,2,1,5,7],2) = [2, 30, 84]
# diff([-6,5,-3,-4,3,-4],3) = [-24, 72, -240]
# ```

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Classes
# - Classes provide a means of bundling data and functionality together.
# - Creating a new class creates a **new type** of object.
# - Assigned variables are new **instances** of that type.
# - Each class instance can have **attributes** attached to it.
# - Class instances can also have **methods** for modifying its state.
# - Python classes provide the class **inheritance** mechanism.
#

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Use class to store data
#
# - A empty class can be used to bundle together a few named data items. 

# + {"slideshow": {"slide_type": "fragment"}}
class Polynomial:
    pass

p = Polynomial()  # Create an empty Polynomial record

p.degree = 2
p.coeffs = [1,-2,3]

# + {"slideshow": {"slide_type": "fragment"}}
p.__dict__

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # namedtuple

# + {"slideshow": {"slide_type": "fragment"}}
from collections import namedtuple

Polynomial = namedtuple('Polynomial', 'degree, coeffs')

# + {"slideshow": {"slide_type": "fragment"}}
p = Polynomial( 2, [1, -2, 3])
p

# + {"slideshow": {"slide_type": "fragment"}}
# Like tuples, namedtuples are immutable:

p.degree = 3


# + {"slideshow": {"slide_type": "slide"}}
class Polynomial:

    "A simple example class representing a Polynomial"
    
    def __init__(self, coeffs):  # constructor
        self.coeffs = coeffs
        
    def degree(self):           
        return len(self.coeffs)-1


p = Polynomial([1, -2, 3, 7, 11, 6, 4])
p.degree(), p.coeffs

# -

# ### Exercise
#
# Add the `diff` function inside the `Polynomial` class.
#
# ```python
# >>> p = Polynomial([1, -2, 3])
# >>> p.diff(2)
# 6
# ```

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Convert method to attribute
#
# Use the `property` decorator 

# + {"slideshow": {"slide_type": "fragment"}}
class Polynomial:

    "A simple example class representing a Polynomial"

    def __init__(self, coeffs):  # constructor
        self.coeffs = coeffs

    @property
    def degree(self):  # method
        return len(self.coeffs)-1


# + {"slideshow": {"slide_type": "fragment"}}
p = Polynomial([1, -2, 3])

p.degree

# + {"slideshow": {"slide_type": "fragment"}}
p

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # The new Python 3.7 DataClass

# + {"slideshow": {"slide_type": "fragment"}}
from dataclasses import dataclass
from typing import List

@dataclass
class Polynomial:

    coeffs: List

    @property
    def degree(self):
        return len(self.coeffs)-1


# + {"slideshow": {"slide_type": "fragment"}}
q = Polynomial([-1, -4, 2, 3])
q.coeffs
# -

print(q)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Method Overriding
# - Every Python classes has a `__repr__()` method used when you call `print()` function.

# +
x = 10
y = 2

print(f" {x:+05d} + {y:5.2e} = {x+y:5.2f} ")


# + {"slideshow": {"slide_type": "fragment"}}
class Polynomial:
    """Simple example class with method overriding """

    def __init__(self, coeffs):
        self.coeffs = coeffs
        
    def __repr__(self):
        return "+".join([ "("+str(c)+")" for c in self.coeffs])

    @property
    def degree(self):
        return len(self.coeffs)-1


# -

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

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Use `class` as a Function.

# +
class F:
    " Create a function f(x) = a * x + b "
    def __init__(self, a, b):
        self.a = a
        self.b = b
    def __call__(self, x):
        return self.a * x + self.b
    
a, b = 2, 1
f = F(a, b)
f(3) # computes a * 3 + b

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# ### Exercise
#
# Add the method `__call__`to the class `Polynomial`

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Inheritance

# + {"slideshow": {"slide_type": "fragment"}}
from datetime import datetime

class Person():  # Parent class is defined here

    def __init__(self, name, birthdate):
        self.name = name
        b = list(map(int,birthdate.split('/')))
        self.birthdate  = datetime(*b[::-1])
        
    @property
    def age( self ):
        return datetime.now() - self.birthdate

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age})"

    

pierre = Person('Navaro', '04/02/1972')
print(pierre)
pierre.age


# +
class Employee(Person):
    
    def __init__(self, name, birthdate, phone):
        
        super().__init__(name, birthdate)
        self.phone = phone
        
Pierre = Employee("Navaro", "04/02/1972", 4308)
# -

Pierre.age
print(Pierre)


# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
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

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Private Variables and Methods

# + {"slideshow": {"slide_type": "fragment"}}
class DemoClass:
    " Demo class for name mangling "

    def public_method(self):
        return 'public!'

    def __private_method(self):  # Note the use of leading underscores
        return 'private!'


object3 = DemoClass()

# + {"slideshow": {"slide_type": "slide"}}
object3.public_method()

# + {"slideshow": {"slide_type": "fragment"}}
object3.__private_method()
# -

dir(object3)

# + {"slideshow": {"slide_type": "fragment"}}
[ s for s in dir(object3) if "method" in s]

# + {"slideshow": {"slide_type": "fragment"}}
object3._DemoClass__private_method()
# -

object3.public_method


# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Operators Overriding 

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Rational example

# + {"slideshow": {"slide_type": "fragment"}}
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


# + {"slideshow": {"slide_type": "slide"}}
r1 = Rational(2,3)
r2 = Rational(3,4)
r1+r2, r1-r2, r1*r2, r1/r2

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ### Exercise 
# Improve the class Polynomial by implementing operations:
# - Overrides '==' operator (__eq__)
# - Overrides '+' operator (__add__)
# - Overrides '-' operator (__neg__)
# - Overrides '*' operator (__mul__)

# +
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


# +
from itertools import zip_longest

l1 = [ 1, 2, 3, 4]
l2 = [ 2, 1, 5, 6, 7, 8]

for i1, i2 in zip_longest(l1, l2, fillvalue=0):
    print(i1, '--', i2)
    
zip_longest

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Iterators
# Most container objects can be looped over using a for statement:

# + {"slideshow": {"slide_type": "slide"}}
for element in [1, 2, 3]:
    print(element, end=' ')

# + {"slideshow": {"slide_type": "slide"}}
for element in (1, 2, 3):
    print(element, end=' ')

# + {"slideshow": {"slide_type": "slide"}}
for key in {'one': 1, 'two': 2}:
    print(key, end=' ')
# -

for key, value in {'one': 1, 'two': 2}.items():
    print(key, value)

# + {"slideshow": {"slide_type": "slide"}}
for char in "123":
    print(char, end=' ')

# + {"slideshow": {"slide_type": "slide"}}
for line in open("../binder/environment.yml"):
    print(line.strip(), end=',')

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# - The `for` statement calls `iter()` on the container object. 
# - The function returns an iterator object that defines the method `__next__()`
# - To add iterator behavior to your classes: 
#     - Define an `__iter__()` method which returns an object with a `__next__()`.
#     - If the class defines `__next__()`, then `__iter__()` can just return self.
#     - The **StopIteration** exception indicates the end of the loop.

# + {"slideshow": {"slide_type": "fragment"}}
s = 'abcdefgh'
it = iter(s)
it

# + {"slideshow": {"slide_type": "fragment"}}
next(it), next(it), next(it), 
# -

it


# + {"slideshow": {"slide_type": "slide"}}
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


# + {"slideshow": {"slide_type": "fragment"}}
rev = Reverse('spam')
for char in rev:
    print(char, end='')


# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Generators
# - Generators are a simple and powerful tool for creating iterators.
# - Write regular functions but use the yield statement when you want to return data.
# - the `__iter__()` and `__next__()` methods are created automatically.
#

# + {"slideshow": {"slide_type": "fragment"}}
def reverse(data):
    for index in range(len(data)-1, -1, -1):
        yield data[index]


# + {"slideshow": {"slide_type": "fragment"}}
for char in reverse('bulgroz'):
     print(char, end='')


# + {"slideshow": {"slide_type": "slide"}}
def reverse(data): # Python 3.6
    yield from data[::-1]
    
for char in reverse('bulgroz'):
     print(char, end='')

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Generator Expressions
#
# - Use a syntax similar to list comprehensions but with parentheses instead of brackets.
# - Tend to be more memory friendly than equivalent list comprehensions.

# +
data = [i for i in range(10)]

iterateur_on_data = ( i**2 for i in data)

for x in iterateur_on_data:
    print(x)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
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
# -


