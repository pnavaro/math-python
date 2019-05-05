#!/usr/bin/env python
# coding: utf-8

# # Python Lists and tuples
# 
# - List is the most versatile Python data type to group values with others
# - Can be written as a list of comma-separated values (items) between square brackets. 
# - Tuples are written between parenthesis. They are read-only lists.
# - Lists can contain items of different types.
# - Like strings, lists can be indexed and sliced.
# - Lists also support operations like concatenation.
# 

# # Indexing

# In[1]:


squares = [1, 4, 9, 16, 25]
print(squares)


# In[2]:


print(squares[0])  # indexing returns the item


# In[3]:


print(squares[-1])


# In[4]:


print(squares[-3:]) # slicing returns a new list


# In[5]:


squares += [36, 49, 64, 81, 100]
print(squares)


# ### Unlike strings, which are immutable, lists are a mutable type.

# In[6]:


cubes = [1, 8, 27, 65, 125]  # something's wrong here  
cubes[3] = 64  # replace the wrong value, the cube of 4 is 64, not 65!
print(cubes)


# In[7]:


cubes.append(216)  # add the cube of 6
print(cubes)


# In[8]:


cubes.remove(1)
print(cubes)


# # Assignment 
# 
# - You can change the size of the list or clear it entirely.
# - The built-in function len() returns list size.
# - It is possible to create lists containing other lists.

# In[9]:


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
letters[2:5] = ['C', 'D', 'E'] # replace some values
print(letters)


# In[10]:


letters[2:5] = [] # now remove them
print(letters)


# In[11]:


a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]


# In[12]:


x


# In[13]:


x[0]


# In[14]:


x[0][1], len(x)


# # Assignment, Copy and Reference

# In[15]:


a = [0, 1, 2, 3, 4]
b = a
print("b = ",b)


# In[16]:


b[1]= 20        # Change one value in b
print("a = ",a) # Y


# **b is a reference to a, they occupy same space memory**

# In[17]:


b = a[:] # assign a slice of a and you create a new list
b[2]=10
print("b = ",b)
print("a = ",a)   


# # Some useful List Methods

# In[18]:


a = list("python-2018")
a


# In[19]:


a.sort()
a


# In[20]:


a.reverse()
a


# In[21]:


a.pop() #pop the last item and remove it from the list
a


# # Dictionary
# 
# They are indexed by keys, which are often strings.

# In[22]:


person = dict(name="John Smith", email="john.doe@domain.fr")
person['size'] = 1.80
person['weight'] = 70


# In[23]:


person


# In[24]:


print(person.keys())


# In[25]:


print(person.items())


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
