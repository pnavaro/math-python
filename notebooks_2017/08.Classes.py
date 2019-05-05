#!/usr/bin/env python
# coding: utf-8

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
# - You can easily save this class containing your data in JSON file.

# In[1]:


import json
class Animal:
    pass

dog = Animal()  # Create an empty animal record

# Fill the fields of the record
dog.name = 'Medor'
dog.weight = 18
dog.age = 4


# In[2]:


dog.__dict__


# # namedtuple

# In[3]:


from collections import namedtuple

Animal = namedtuple('Animal', 'name, weight, age')


# In[4]:


dog = Animal('Dog', 18.0, 4)
dog


# In[5]:


# Like tuples, namedtuples are immutable:
import traceback
try:
    dog.weight = 14.5
except:
    traceback.print_exc()
        


# In[6]:


class Animal:

    "A simple example class Animal with its name, weight and age"

    def __init__(self, name, weight, age):  # constructor
        self.name = name
        self.weight = weight
        self.age = age

    def birthyear(self):  # method
        import datetime
        now = datetime.datetime.now()
        return now.year - self.age


# In[7]:


dog = Animal('Dog', 18, 4) # Instance
print(f' {dog.name}: {dog.weight} Kg, {dog.age} years')
dog.birthyear()


# In[8]:


dog.age = 7
dog.birthyear()


# - `dog` is an *instance* of Animal Class.
# - `dog.birthdate()` is a *method* of `Animal` instance `dog`.
# - `name` and `weight` are attributes of `Animal` instance `dog`.

# # Convert method to attribute
# 
# Use the `property` decorator 

# In[9]:


class Animal:

    "A simple example class Animal with its name, weight and age"

    def __init__(self, name, weight, age):  # constructor
        self.name = name
        self.weight = weight
        self.age = age

    @property
    def birthyear(self):  # method
        import datetime
        now = datetime.datetime.now()
        return now.year - self.age


# In[10]:


dog = Animal('Dog', 18, 4)
dog.birthyear  # birthyear can now be used as an attribute


# In[11]:


dog


# # The new Python 3.7 DataClass

# In[12]:


from dataclasses import dataclass

@dataclass
class Animal:

    name: str
    weight: float
    age: int

    @property
    def birthyear(self) -> int:
        import datetime
        now = datetime.datetime.now()
        return now.year - self.age


# In[13]:


dog = Animal('Dog', 18.0, 4)
dog


# # Method Overriding
# - Every Python classes has a `__repr__()` method used when you call `print()` function.

# In[14]:


class Animal:
    """Simple example class with method overriding """

    def __init__(self, name, weight, age):
        self.name = name
        self.weight = weight
        self.age = age

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.weight}, {self.age})"

    @property
    def birthyear(self):
        import datetime
        now = datetime.datetime.now()
        return now.year - self.age


# In[15]:


dog = Animal('Dog', 18.0, 4)
print(dog)
dog.birthyear


# # Inheritance

# In[16]:


class Dog(Animal):  # Parent class is defined here

    " Derived from MyClass with k attribute "

    def __init__(self, name, weight, age, breed):
        super().__init__(name, weight, age)  # Call method in the parent class
        self.breed = breed

    def __repr__(self):
        return f"{self.__class__.__name__}({self.name}, {self.weight}, {self.age}, {self.breed})"


beagle = Dog('Jack', 9.0, 1, 'Beagle')
print(beagle)
beagle.birthyear


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

# ### Exercise: Grocery list item
# 
# Let's create a class representing a grocery list. First we need a class to represent an item of this grocery list:
# - The `GroceryItem` class has seven attributes:
#     - `name` (string)
#     - `price` (double)
#     - `category` (string)
#     - `vat_percentage` (double)
#     - `quantity` (integer)
#     - `ingredients` (list of strings)
# 
# - The item class has two methods
#     - `get_total_vat` returns the VAT value.
#     - `get_total_price` returns the total price.
# 
# Implement the `GroceryItem` class and override the `__repr__()` method by returning the item name and its quantity.

# ```python
# beef = GroceryItem("Beef", 12.3, "Meat", 10, 2, ["Beef"])
# print(beef)
# print(f"Total price : {beef.get_total_price():.2f} \u20ac ")
# print(f"Total VAT   : {beef.get_total_vat():.2f} \u20ac ")
# ```
# ```pybt
# Beef x 2
# Total cut   : 0.0 € 
# Total price : 27.060000000000002 € 
# Total VAT   : 2.46 € 
# ```

# ### Exercice: Grocery list
# 
# Now implement the GroceryList containing GroceryItem defined above.
# In this class, add these functions:
# 
# - `items_with_meat()` return a list of items of 'Meat' category.
# - `prices_with_vat()` return a dict with item names as keys and prices as values.
# - `ingredients_list()` return a set of all ingredients contained in items.
# - `total_invoice()` return the total price of the shopping list.
# - `total_for(category)` return the total price for a category
# - `price_by_category()` return a dict with category as key and the price as value.
# - `total_vat()` return the total VAT amount.
# - `top_ingredients(n)` ranks the `n` most frequently founded ingredients
# - `all_item_names()` return a list of item names

# ```python
# print(f"Articles with meat are : {shopping_list.items_with_meat()}")
# print(f"Full prices are : {shopping_list.prices_with_vat()}")
# print(f"Ingredients : {shopping_list.ingredients_list()}")
# print(f"Total  : {shopping_list.total_invoice()}")
# print(f"Total for meat category : {shopping_list.total_for('Meat')}")
# print(f"Prices by category : {shopping_list.price_by_category()}")
# print(f"VAT amount : {shopping_list.total_vat()}")
# print(f"First three ingedients : {shopping_list.top_ingredients(3)}")
# print(f"All articles names : {shopping_list.all_item_names()}")
# ```
# ```pytb
# Articles with meat are : [Beef x 2, Pork x 1]
# Full prices are : {'Beef': 27.06, 'Pork': 8.34, 'Tomato Sauce': 6.60, 'Beans': 17.32, 'Tuna': 7.19}
# Ingredients : {'Tomato', 'Preservatives', 'Fish', 'Sugar', 'Water', 'Beef', 'Salt', 'Beans', 'Oil', 'Pork'}
# Total  : 66.53
# Total for meat category : 35.40
# Prices by category : {'Meat': 35.40, 'Can': 31.125000000000004}
# VAT amount : 6.59
# First three ingedients : ['Water', 'Salt', 'Beef']
# All articles names : ['Beef', 'Pork', 'Tomato Sauce', 'Beans', 'Tuna']
# ```

# # Private Variables and Methods

# In[25]:


class DemoClass:
    " Demo class for name mangling "

    def public_method(self):
        return 'public!'

    def __private_method(self):  # Note the use of leading underscores
        return 'private!'


object3 = DemoClass()


# In[26]:


object3.public_method()


# In[27]:


try:
    object3.__private_method()
except:
    traceback.print_exc()


# In[28]:


[ s for s in dir(object3) if "method" in s]


# In[29]:


object3._DemoClass__private_method()


# In[30]:


object3.public_method


# # Use `class` as a Function.

# In[31]:


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

# In[58]:


class MyComplex:
    " Simple class representing a complex"
    width = 7
    precision = 3

    def __init__(self, real=0, imag=0):
        self.real = real
        self.imag = imag

    def __repr__(self): 
        return (f"({self.real:{self.width}.{self.precision}f}"
                f"{self.imag:+{self.width}.{self.precision}f}j)")

    def __eq__(self, other):  # override '=='
        return (self.real == other.real) and (self.imag == other.imag)

    def __add__(self, other):  # override '+'
        return MyComplex(self.real+other.real, self.imag+other.imag)

    def __sub__(self, other):  # override '-'
        return MyComplex(self.real-other.real, self.imag-other.imag)

    def __mul__(self, other):  # override '*'
        if isinstance(other, MyComplex):
            return MyComplex(self.real * other.real - self.imag * other.imag,
                             self.real * other.imag + self.imag * other.real)

        else:
            return MyComplex(other*self.real, other*self.imag)


# In[59]:


u = MyComplex(0, 1)
v = MyComplex(1, 0)
print('u=', u, "; v=", v)


# In[60]:


u+v, u-v, u*v, u==v


# We can change the *class* attribute precision.

# In[61]:


MyComplex.precision=2
print(u.precision)
print(u)


# In[62]:


v.precision


# We can change the *instance* attribute precision.

# In[63]:


u.precision=1
print(u)


# In[64]:


print(v)


# In[65]:


MyComplex.precision=5
u # set attribute keeps its value


# In[66]:


v # unset attribute is set to the new value


# ## Rational example

# In[67]:


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
        self.numer, self.denom = n//g, d//g

    def __add__(self, other):
        return Rational(self.numer * other.denom + other.numer * self.denom,
                        self.denom * other.denom)

    def __sub__(self, other):
        return Rational(self.numer * other.denom - other.numer * self.denom,
                        self.denom * other.denom)

    def __mul__(self, other):
        return Rational(self.numer * other.numer, self.denom * other.denom)

    def __truediv__(self, other):
        return Rational(self.numer * other.denom, self.denom * other.numer)

    def __repr__(self):
        return f"{self.numer:d}/{self.denom:d}"


# In[68]:


r1 = Rational(2,3)
r2 = Rational(3,4)
r1+r2, r1-r2, r1*r2, r1/r2


# ### Exercise 
# Improve the class Polynomial by implementing operations:
# - Overrides '==' operator (__eq__)
# - Overrides '+' operator (__add__)
# - Overrides '-' operator (__neg__)
# - Overrides '*' operator (__mul__)
