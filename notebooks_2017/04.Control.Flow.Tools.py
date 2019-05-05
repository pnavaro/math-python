#!/usr/bin/env python
# coding: utf-8

# # Control Flow Tools

# ## While loop
# 
# - Don't forget the ':' character.
# - The body of the loop is indented

# In[1]:


# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while b < 1000:
    a, b = b, a+b
    print(round(b/a,3), end=",")


# # `if` Statements
# 
# ```python
# True, False, and, or, not, ==, is, !=, is not, >, >=, <, <=
# ```
# 
# 

# In[2]:


x = 42
if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


# switch or case statements don't exist in Python.

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

# # Loop over an iterable object
# 
# We use for statement for looping over an iterable object. If we use it with a string, it loops over its characters.
# 

# In[3]:


for c in "python":
    print(c)


# In[4]:


for word in "Python Lille april 10th 2018".split(" "):
    print(word, len(word))   


# ### Exercise: Anagram
# An anagram is word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
# 
# Write a code that print True if s1 is an anagram of s2. 
# To do it, remove every character present in both strings. Check 
# you obtain two empty strings.
# 
# Hint: `s = s.replace(c,"",1)` removes the character `c` in string `s` one time.
# 
# ```python
# s1 = "pascal obispo"
# s2 = "pablo picasso"
# ..
# True
# ```

# # Loop with range function
# 
# - It generates arithmetic progressions
# - It is possible to let the range start at another number, or to specify a different increment.
# - Since Python 3, the object returned by `range()` doesn’t return a list to save memory space. `xrange` no longer exists.
# - Use function list() to creates it.

# In[6]:


list(range(5))


# In[7]:


list(range(2, 5))


# In[8]:


list(range(-1, -5, -1))


# In[9]:


for i in range(5):
    print(i, end=' ')


# ### Exercise Exponential
# 
# - Write some code to compute the exponential mathematical constant $e \simeq 2.718281828459045$ using the taylor series developed at 0 and without any import of external modules:
# 
# $$ e \simeq \sum_{n=0}^{50} \frac{1}{n!} $$

# # `break` Statement.

# In[12]:


for n in range(2, 10):     # n = 2,3,4,5,6,7,8,9
    for x in range(2, n):  # x = 2, ..., n-1
        if n % x == 0:     # Return the division remain (mod)
            print(n, " = ", x, "*", n//x)
            break
        else:
            print("%d is a prime number" % n)
            break


# #  `iter` Function

# In[13]:


course = """ Python april 10,11,12 2018 LILLE """.split()
print(course)


# In[14]:


iterator = iter(course)
print(iterator.__next__())


# In[15]:


print(iterator.__next__())


# # Defining Function: `def` statement

# In[17]:


def is_palindromic(s):
    "Return True if the input sequence is a palindrome"
    return s == s[::-1]


is_palindromic("kayak")


# - Body of the function start must be indented
# - Functions without a return statement do return a value called `None`.
# 

# In[18]:


def fib(n):
    """Print a Fibonacci series up to n."""
    a, b = 0, 1
    while a < n:
         print(a, end=' ')  # the end optional argument is \n by default
         a, b = b, a+b
    print("\n") # new line
     
result = fib(2000)
print(result) # is None


# # Documentation string
# - It’s good practice to include docstrings in code that you write, so make a habit of it.

# In[19]:


def my_function( foo):
     """Do nothing, but document it.

     No, really, it doesn't do anything.
     """
     pass

print(my_function.__doc__)


# In[20]:


help(my_function)


# # Default Argument Values

# In[21]:


def f(a,b=5):
    return a+b

print(f(1))
print(f(b="a",a="bc"))


# **Important warning**: The default value is evaluated only once. 

# In[22]:


def f(a, L=[]):
    L.append(a)
    return L

print(f(1))


# In[23]:


print(f(2)) # L = [1]


# In[24]:


print(f(3)) # L = [1,2]


# # Function Annotations
# 
# Completely optional metadata information about the types used by user-defined functions.
# These type annotations conforming to [PEP 484](https://www.python.org/dev/peps/pep-0484/) could be statically used by [MyPy](http://mypy-lang.org).

# In[25]:


def f(ham: str, eggs: str = 'eggs') -> str:
     print("Annotations:", f.__annotations__)
     print("Arguments:", ham, eggs)
     return ham + ' and ' + eggs

f('spam')
help(f)
print(f.__doc__)


# # Arbitrary Argument Lists
# 
# Arguments can be wrapped up in a tuple or a list with form *args

# In[26]:


def f(*args, sep=" "):
    print (args)
    return sep.join(args)

print(f("big","data"))


# - Normally, these variadic arguments will be last in the list of formal parameters. 
# - Any formal parameters which occur after the *args parameter are ‘keyword-only’ arguments.

# # Keyword Arguments Dictionary
# 
# A final formal parameter of the form **name receives a dictionary.

# In[27]:


def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    print("-- I'm sorry, we're all out of", kind)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for key, value in keywords.items():
        print(key, ":", value)


# \*name must occur before \*\*name

# In[28]:


cheeseshop("Limburger", "It's very runny, sir.",
           "It's really very, VERY runny, sir.",
           shopkeeper="Michael Palin",
           client="John Cleese",
           sketch="Cheese Shop Sketch")


# # Lambda Expressions
# 
# Lambda functions can be used wherever function objects are required.

# In[29]:


f = lambda x : 2 * x + 2
f(3)


# In[30]:


taxicab_distance = lambda x_a,y_a,x_b,y_b: abs(x_b-x_a)+abs(y_b-y_a)
print(taxicab_distance(3,4,7,2))


# lambda functions can reference variables from the containing scope:
# 
# 

# In[31]:


def make_incrementor(n):
    return lambda x: x + n

f = make_incrementor(42)
f(0),f(1)


# # Unpacking Argument Lists
# Arguments are already in a list or tuple. They can be unpacked for a function call. 
# For instance, the built-in range() function is called with the *-operator to unpack the arguments out of a list:

# In[32]:


def chessboard_distance(x_a, y_a, x_b, y_b):
    """
    Compute the rectilinear distance between 
    point (x_a,y_a) and (x_b, y_b)
    """
    return max(abs(x_b-x_a),abs(y_b-y_a))

coordinates = [3,4,7,2] 
chessboard_distance(*coordinates)


# In the same fashion, dictionaries can deliver keyword arguments with the **-operator:

# In[33]:


def parrot(voltage, state='a stiff', action='voom'):
     print("-- This parrot wouldn't", action, end=' ')
     print("if you put", voltage, "volts through it.", end=' ')
     print("E's", state, "!")

d = {"voltage": "four million", "state": "bleedin' demised", "action": "VOOM"}
parrot(**d)


# ### Exercise: Time converter
# Write 3 functions to manipulate hours and minutes : 
# - Function minutes return minutes from (hours, minutes). 
# - Function hours the inverse function that return (hours, minutes) from minutes. 
# - Function add_time to add (hh1,mm1) and (hh2, mm2) two couples (hours, minutes). It takes 2
# tuples of length 2 as input arguments and return the tuple (hh,mm). 
# 
# ```python
# print(minutes(6,15)) # 375 
# print(minutes(7,46)) # 466 
# print(add_time((6,15),(7,46)) # (14,01)
# ```

# # Functions Scope
# 
# - All variable assignments in a function store the value in the local symbol table.
# - Global variables cannot be directly assigned a value within a function (unless named in a global statement).
# - The value of the function can be assigned to another name which can then also be used as a function.

# In[34]:


pi = 1.
def deg2rad(theta):
    pi = 3.14
    return theta * pi / 180.

print(deg2rad(45))
print(pi)


# In[35]:


def rad2deg(theta):
    return theta*180./pi

print(rad2deg(0.785))
pi = 3.14
print(rad2deg(0.785))


# In[36]:


def deg2rad(theta):
    global pi
    pi = 3.14
    return theta * pi / 180

pi = 1
print(deg2rad(45))


# In[37]:


print(pi)


# # `enumerate` Function

# In[38]:


primes =  [1,2,3,5,7,11,13]
for idx, ele in enumerate (primes):
    print(idx, " --- ", ele) 


# ### Exercise: Caesar cipher
# 
# In cryptography, a Caesar cipher, is one of the simplest and most widely known encryption techniques. It is a type of substitution cipher in which each letter in the plaintext is replaced by a letter some fixed number of positions down the alphabet. For example, with a left shift of 3, D would be replaced by A, E would become B, and so on. 
# 
# - Create a function `cipher` that take the plain text and the key value as arguments and return the encrypted text.
# - Create a funtion `plain` that take the crypted text and the key value as arguments that return the deciphered text.
# 

# # `zip` Builtin Function
# 
# Loop over sequences simultaneously.

# In[39]:


L1 = [1, 2, 3]
L2 = [4, 5, 6]

for (x, y) in zip(L1, L2):
    print (x, y, '--', x + y)


# ### Exercise
# 
# Code a new version of your cypher function to crypt also upper case character. 
# Use `zip` to loop over upper and lower case alphabets.
# 

# # List comprehension
# 
# - Set or change values inside a list
# - Create list from function

# In[43]:


lsingle = [1, 3, 9, 4]
ldouble = []
for k in lsingle:
    ldouble.append(2*k)
ldouble


# In[44]:


ldouble = [k*2 for k in lsingle]


# In[45]:


[n*n for n in range(1,10)]


# In[46]:


[n*n for n in range(1,10) if n&1]


# In[47]:


[n+1 if n&1 else n//2 for n in range(1,10) ]


# ### Exercise
# 
# Code a new version of cypher function using list comprehension. 
# 
# Hints: 
# - `s = ''.join(L)` convert the characters list `L` into a string `s`.
# - `L.index(c)` return the index position of `c` in list `L` 
# - `"c".islower()` and `"C".isupper()` return `True`

# # `map` built-in function
# 
# Apply a function over a sequence.
# 

# In[48]:


res = map(hex,range(16))
print(res)


# Since Python 3.x, `map` process return an iterator. Save memory, and should make things go faster.
# Display result by using unpacking operator.

# In[49]:


print(*res)


# # `map` with user-defined function

# In[50]:


def add(x,y):
    return x+y

L1 = [1, 2, 3]
L2 = [4, 5, 6]
print(*map(add,L1,L2))


# ### `map` is often faster than `for` loop

# In[51]:


M = range(10000)
f = lambda x: x**2
get_ipython().run_line_magic('timeit', 'lmap = map(f,M)')


# In[52]:


M = range(10000)
f = lambda x: x**2
get_ipython().run_line_magic('timeit', 'lfor = (f(m) for m in M)')


# ## filter
# creates a iterator of elements for which a function returns `True`. 

# In[53]:


number_list = range(-5, 5)
odd_numbers = filter(lambda x: x & 1 , number_list)
print(*odd_numbers)


# ### As `map`, `filter` is often faster than `for` loop

# In[54]:


M = range(1000)
f = lambda x: x % 3 == 0
get_ipython().run_line_magic('timeit', 'lmap = filter(f,M)')


# In[55]:


M = range(1000)
get_ipython().run_line_magic('timeit', 'lfor = (m for m in M if m % 3 == 0)')


# ### Exercise:
# 
# Code a new version of your cypher function using map. 
# 
# Hints: 
# - Applied function must have only one argument, create a function called `shift` with the key value and use map.

# # Recursive Call

# In[56]:


def gcd(x, y): 
    """ returns the greatest common divisor."""
    if x == 0: 
        return y
    else : 
        return gcd(y % x, x)

gcd(12,16)


# ### Exercise: factorial
# 
# - Write the function `factorial` with a recursive call
# 
# NB: Recursion is not recommended by [Guido](http://neopythonic.blogspot.co.uk/2009/04/tail-recursion-elimination.html).

# ### Exercise: Minimum number of rooms required for lectures.
# 
# Given an array of time intervals (start, end) for classroom lectures (possibly overlapping), find the minimum number of rooms required.
# 
# For example, given Input: 
# ```python
# lectures = ["9:00-10:30", "9:30-11:30","11:00-12:00","14:00-18:00", "15:00-16:00", "15:30-17:30", "16:00-18:00"]
# ```
# should output 3.

# ### Exercise: [non-palindromic skinny numbers](https://oeis.org/A035123)
# 
# non-palindromic squares remaining square when written backwards
# 
# $$
# \begin{array}{lclclcl}
# 10^2  &=& 100   &\qquad& 01^2  &=& 001 \\
# 13^2  &=& 169   &\qquad& 31^2  &=& 961 \\
# 102^2 &=& 10404 &\qquad& 201^2 &=& 40401
# \end{array}
# $$
# 

# ### Exercise: Polynomial derivative
# - A Polynomial is represented by a Python list of its coefficients.
#     [1,5,-4] => $1+5x-4x^2$
# - Write the function diff(P,n) that return the nth derivative Q
# - Don't use any external package 😉
# ```
# diff([3,2,1,5,7],2) = [2, 30, 84]
# diff([-6,5,-3,-4,3,-4],3) = [-24, 72, -240]
# ```

# ### Exercise: Narcissistic number
# 
# A  number is narcissistic if the sum of its own digits each raised to the power of the number of digits. 
# 
# Example : $4150 = 4^5 + 1^5 + 5^5 + 0^5$ or $153 = 1^3 + 5^3 + 3^3$
# 
# Find narcissitic numbers with 3 digits
# 
# 
# 

# ### Exercise: Happy number
# 
# - Given a number $n = n_0$, define a sequence $n_1, n_2,\ldots$ where 
#     $n_{{i+1}}$ is the sum of the squares of the digits of $n_{i}$. 
#     Then $n$ is happy if and only if there exists i such that $n_{i}=1$.
# 
# For example, 19 is happy, as the associated sequence is:
# $$
# \begin{array}{cccccl}
# 1^2 &+& 9^2 & &     &=& 82 \\
# 8^2 &+& 2^2 & &     &=& 68 \\
# 6^2 &+& 8^2 & &     &=& 100 \\
# 1^2 &+& 0^2 &+& 0^2 &=& 1
# \end{array}
# $$
# - Write a function `ishappy(n)` that returns True if `n` is happy.
# - Write a function `happy(n)` that returns a list with all happy numbers < $n$.
# 
# ```python
# happy(100) = [1, 7, 10, 13, 19, 23, 28, 31, 32, 44, 49, 68, 70, 79, 82, 86, 91, 94, 97]
# ```
# 
# 

# ### Exercise: longuest increasing subsequence
# 
# Given N elements, write a program that prints the length of the longuest increasing subsequence whose adjacent element difference is one.
# 
# Examples:
# ```
# a = [3, 10, 3, 11, 4, 5, 6, 7, 8, 12]
# Output : 6
# Explanation: 3, 4, 5, 6, 7, 8 is the longest increasing subsequence whose adjacent element differs by one.
# ```
# ```
# Input : a = [6, 7, 8, 3, 4, 5, 9, 10]
# Output : 5
# Explanation: 6, 7, 8, 9, 10 is the longest increasing subsequence
# ```
