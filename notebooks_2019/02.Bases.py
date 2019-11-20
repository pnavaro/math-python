# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # First program
#
# - Print out the string "Hello world!" and its type.
# - Print out the value of `a` variable set to 6625 and its type.

# + {"slideshow": {"slide_type": "fragment"}}
s = "Hello World!"
print(type(s),s)

# + {"slideshow": {"slide_type": "fragment"}}
a = 6625
print(type(a),a)

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Python Types
# - Most of Python types are classes, typing is dynamic.
# - ; symbol can be used to split two Python commands on the same line.

# + {"slideshow": {"slide_type": "fragment"}}
s = int(2010); print(type(s))
s = 3.14; print(type(s))
s = True; print(type(s))
s = None; print(type(s))
s = 1.0j; print(type(s))
s = type(type(s)); print(type(s))

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Calculate with Python

# + {"slideshow": {"slide_type": "fragment"}}
x = 45      # This is a comment!
x += 2        # equivalent to x = x + 2
print(x, x > 45)

# + {"slideshow": {"slide_type": "fragment"}}
y = 2.5
print("x+y=",x+y, type(x+y))  # Add float to integer, result will be a float

# + {"slideshow": {"slide_type": "fragment"}}
print(x*10/y)   # true division returns a float
print(x*10//3)  # floor division discards the fractional part

# + {"slideshow": {"slide_type": "fragment"}}
print( x % 8) # the % operator returns the remainder of the division

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Multiple Assignment
# - Variables can simultaneously get new values. 
# - Expressions on the right-hand side are all evaluated first before assignments take place. 
# - The right-hand side expressions are evaluated from the left to the right.
# - Use it very carefully

# + {"slideshow": {"slide_type": "fragment"}}
a = b = c = 1
print(a, b, c) 

# + {"slideshow": {"slide_type": "fragment"}}
a, b, c = 1, 2, 3
print (a, b, c)

# + {"slideshow": {"slide_type": "fragment"}}
a, c = c, a     # Nice way to permute values
print (a, b, c) 

# + {"slideshow": {"slide_type": "fragment"}}
a < b < c, a > b > c
# -

# # Import a package

import lorem
lorem.sentence()

from lorem import sentence
sentence()

# # Manipulate strings

s = sentence()
s

s.lower()

s.replace(".","")

s.count("e")

s.index("o")

s[:5], s[-5:]

# ### Exercise
#
# - Use index method to get the first and the last word of the sentence.

# ### String concatenation and repeat

2 * s == s + s



# # Open and write to file

with open("sample.txt", "w") as f:
    f.write(lorem.paragraph())

%cat sample.txt

# # Open and read from file

with open("sample.txt") as f:
    data = f.read()
data

# # Python Lists and tuples
# - List is the most versatile Python data type to group values with others
# - Can be written as a list of comma-separated values (items) between square brackets.
# - Tuples are written between parenthesis. They are read-only lists.
# - Lists can contain items of different types.
# - Like strings, lists can be indexed and sliced.
# - Lists also support operations like concatenation.
#

# ### Create list of words from a text

words = data.split()
words[:5] # display 5 first words

# Methods available for a python list
#
# - `append` 
# - `clear` 
# - `copy` 
# - `count` 
# - `extend`
# - `index`
# - `insert`
# - `pop`
# - `remove`
# - `reverse`
# - `sort`
#
# To get the doc just type words.reverse (shift+TAB)

# # Loops and control flows
#
# ## While

a, b = 0, 1
while b < 1000:
    a, b = b, a+b
    print(round(b/a,3), end=",")

# ## For

words = sentence().split()
for word in words:
    print(word, len(word))

for i in range(5):
    print(i, words[i], len(words[i]))

for i,w in enumerate(words):
    print(i, w, len(w))

for i,w in enumerate(words[::-1]):
    print(i, w, len(w))

for i,w in enumerate(sorted(words)):
    print(i, w, len(w))

# # If else

for i in range(1,11):
    print(i, end=" is ")
    if i % 2 == 0:
        print("even")
    else:
        print("odd")

# ### Exercise [Collatz conjecture](https://en.wikipedia.org/wiki/Collatz_conjecture)
#
# Consider the following operation on an arbitrary positive integer:
#  - If the number is even, divide it by two.
#  - If the number is odd, triple it and add one.
#
# The conjecture is that no matter what initial value of this integer, the sequence will always reach 1.
#  - Test the Collatz conjecture for n = 100000.
#  - How many steps do you need to reach 1 ?
#  

# # `break` Statement.

for n in range(2, 10):     # n = 2,3,4,5,6,7,8,9
    for x in range(2, n):  # x = 2, ..., n-1
        if n % x == 0:     # Return the division remain (mod)
            print(n, " = ", x, "*", n//x)
            break
        else:
            print("%d is a prime number" % n)
            break


# # Defining Function

# - Body of the function start must be indented
# - Functions without a return statement do return a value called `None`.

# +
def is_prime(n):
    """
    Return True if the input int is a prime number
    """
    for x in range(2, n): 
        if n % x == 0:
            return False
        
    return True

for n in range(1,10):
    print(n, is_prime(n))
# -

help(is_prime)


# # Default Argument Values

def f(a,b=5):
    return a+b

print(f(1))
print(f(b="a",a="bc"))


# **Important warning**: The default value is evaluated only once. 

def f(a, L=[]):
    L.append(a)
    return L

print(f(1))

print(f(2)) # L = [1]

print(f(3)) # L = [1,2]


# # Arbitrary Argument Lists
#
# Arguments can be wrapped up in a tuple or a list with form *args

def f(*args, sep=" "):
    print(args)
    return sep.join(args)

print(f("big","data"))


# - Normally, these variadic arguments will be last in the list of formal parameters. 
# - Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments.

# # Keyword Arguments Dictionary
#
# A final formal parameter of the form **name receives a dictionary.

# +
def person(**kwargs):
    for key, value in kwargs.items():
        print(key, ":", value)
        
person( firstname="Pierre", lastname="Navaro", office=112)
# -

# \*args must occur before \*\*kwargs
#
# kwargs is a dictionary, we can do the same operation with

me = dict(firstname="Pierre", lastname="Navaro", office=112)
me

type(me)

me.keys()

me.items()

me["firstname"]

me["position"]="Engineer"

me

# # Lambda Expressions
#
# Lambda functions can be used wherever function objects are required.

f = lambda x : 2 * x + 2
f(3)


# lambda functions can reference variables from the containing scope:
#
# Create the polynomial function p(x) = ax^2 +bx + c

def make_polynom(a, b, c):
    return lambda x: a * x**2 + b * x + c 

p = make_polynom(a=1, b=2, c=3)
p(0),p(1)

# # Unpacking Argument Lists
# Arguments are already in a list or tuple. They can be unpacked for a function call. 
# For instance, the built-in range() function is called with the *-operator to unpack the arguments out of a list:

coeffs_list = [1, 2, 3]

p = make_polynom(*coeffs_list)
p(0),p(1)

coeffs_dict = dict(a=1, b=2, c=3)
coeffs

p = make_polynom(**coeffs_dict)
p(0),p(1)

# # Functions Scope
#
# - All variable assignments in a function store the value in the local symbol table.
# - Global variables cannot be directly assigned a value within a function (unless named in a global statement).
# - The value of the function can be assigned to another name which can then also be used as a function.

pi = 1.
def deg2rad(theta):
    pi = 3.14
    return theta * pi / 180.

print(deg2rad(45))
print(pi)


def rad2deg(theta):
    return theta*180./pi

print(rad2deg(0.785))
pi = 3.14
print(rad2deg(0.785))


def deg2rad(theta):
    global pi
    pi = 3.14
    return theta * pi / 180

pi = 1
print(deg2rad(45))

print(pi)

# # `zip` Builtin Function
#
# Loop over sequences simultaneously.

for (x, y) in zip(L1, L2):
    print (x, y, '--', x + y)

# If we want to add element by element two lists.

# +
p1 = [1,2,3]
p2 = [3,4,5]

p3 = [] # create an empty list
for c1,c2 in zip(p1,p2):
    p3.append(c1+c2)
    
p3
# -

# # List comprehension
#
# - Set or change values inside a list
# - Create list from function

p3 = [c1+c2 for c1,c2 in zip(p1,p2)]
p3

[n*n for n in range(1,10)] # list of squares

[n*n for n in range(1,10) if n % 2 != 0]

[n+1 if n&1 else n//2 for n in range(1,10) ]

# # `map` built-in function
#
# Apply a function over a sequence.
#

res = map(is_prime,range(16))
print(res)

# Since Python 3.x, `map` process return an iterator. Save memory, and should make things go faster.
# Display result by using unpacking operator.

print(*res)


# # `map` with user-defined function

def add(x,y):
    return x+y

L1, L2 = [1, 2, 3], [4, 5, 6]
res = map(add,L1,L2)
print(*res)

print(*res) # res is empty

# ### `map` is often faster than `for` loop

M = range(10000)
f = lambda x: x**2
%timeit lmap = map(f,M)

M = range(10000)
f = lambda x: x**2
%timeit lfor = (f(m) for m in M)

# # Parallel version of map

# +
from time import sleep

def slow_add( x ):
    sleep(1.0)
    return x+1

data = list(range(8))
data    
# -

%%time
res = map(slow_add, data)
print(*res)

# +
%%time

from concurrent.futures import ThreadPoolExecutor

with ThreadPoolExecutor(4) as pool:
    res = pool.map(slow_add, data)

print(*res)


# -

# # Recursive Call

def gcd(x, y): 
    """ returns the greatest common divisor."""
    if x == 0: 
        return y
    else : 
        return gcd(y % x, x)

gcd(12,16)

# ## Exercise: Polynomial
#
# - A Polynomial is represented by a Python list of its coefficients.
#     [1,5,-4] => $1+5x-4x^2$
#     
# ### Evaluation 
#
# - Write the function eval(P,x) that return the value of P(x)
#
# ```
# P = [3,2,1,5,7]
# eval([3,2,1,5,7],1) =  18
# ```

# ### Derivative
#
# - Write the function diff(P,n) that return the nth derivative Q
# ```
# diff([3,2,1,5,7],2) = [2, 30, 84]
# diff([-6,5,-3,-4,3,-4],3) = [-24, 72, -240]
# ```
#
# ### Addition
# - Write the function add(P,Q) that return the polynomial coefficients of P+Q
# - Your function must work when P and Q has different degrees
#
# ### Multiplication
# - Write the function mul(P,Q) that return the polynomial coefficients of P*Q

P = [ 1, 5, 6, 8]
Q = [ -2, 1, 3]
     

# +
from numpy import poly1d

p = poly1d(P[::-1])
q = poly1d(Q[::-1])
# -

p + q

p * q


