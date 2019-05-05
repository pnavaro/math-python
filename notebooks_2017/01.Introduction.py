#!/usr/bin/env python
# coding: utf-8

# ![jkvdp_tweet](../images/jkvdp_tweet.png)

# # History
# 
# - Project initiated by Guido Von Rossum in 1990
# - Interpreted language written in C.
# - Widely used in all domains (Web, Data Science, Scientific Computation).
# - This is a high level language with a simple syntax. 
# - Python types are numerously and powerful.
# - Bind Python with other languages is easy.
# - You can perform a lot of operations with very few lines.
# - Available on all platforms Unix, Windows, Mac OS X...
# - Very few limits.
# - Many libraries offer Python bindings.
# 
# 

# # Python 2 and 3 version
# - Python 3.x isn't a simple improvement or extension of Python 2.x.
# - All libraries exist in version 3  but both versions coexist.
# - Every example are written in Python 3.x, it is the default version.
# - Changes in official documentation: [https://docs.python.org/3/whatsnew/3.0.html]
# - `print` is now a function `print()` with `sep` argument.
# - Some function return "views" instead of "lists".
# - In version 3 division operator isn't pure (7/2 = 3.5).
# - `range` function doesn't return list anymore. Use `list(range(n))`.
# 
# ## Porting your code 
# - http://www.diveintopython3.net/porting-code-to-python-3-with-2to3.html
# - [Python-Future](http://python-future.org/quickstart.html) offers Python 2 compatibility.
# - [Migrating to Python 3 with pleasure](https://github.com/arogozhnikov/python3_with_pleasure?utm_campaign=Data%2BElixir&utm_medium=email&utm_source=Data_Elixir_165)

# # Python distributions
# 
#  Python packages are available with all linux distributions but you can get standalone bundles:
# - [Enthought Python Distribution](http://www.enthought.com/products/epd.php)
# - [Astropy](http://www.astropy.org)
# - [SAGEMATH](http://sagemath.org/)
# - [Anaconda](https://www.continuum.io/downloads)
# - [Pyzo](http://www.pyzo.org)
# 

# # Performances
#  Python is not fast... but:
# - Sometimes it is. 
# - Most of operations are optimized.
# - Package like numpy can reduce the CPU time.
# - With Python you can save time to achieve your project.
# 
# Some advices:
# - Write your program with Python language. 
# - If it is fast enough, be happy.
# - After profiling, optimize costly parts of your code.
# - If you're still not satisfied, try [Julia](https://www.julialang.org).
# 
# "Premature optimization is the root of all evil" (Donald Knuth 1974)
# 

# # Jupyter Notebook
# 
# 
# To open the notebook
# ```
# jupyter notebook
# ```
# You should see the notebook open in your browser. If not, go to http://localhost:8888/tree
# 
# The Jupyter Notebook is an interactive environment for writing and running code. 
# The notebook is capable of running code in [a wide range of languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). 
# However, each notebook is associated with Python3 kernel.

# # Jupyter Lab
# - You can eventually switch to the web-based user interface JupyterLab. Go to   http://localhost:8888/lab
# - JupyterLab enables you to work with text editors, terminals, and custom components. 
# - JupyterLab looks like [RStudio Server](https://support.rstudio.com/hc/en-us/articles/234653607-Getting-Started-with-RStudio-Server).

# ## Code cells allow you to enter and run code
# 
# **Make a copy of this notebook by using the File menu.**
# 
# Run a code cell using `Shift-Enter` or pressing the <button class='btn btn-default btn-xs'><i class="icon-step-forward fa fa-step-forward"></i></button> button in the toolbar above:
# 
# There are two other keyboard shortcuts for running code:
# 
# * `Alt-Enter` runs the current cell and inserts a new one below.
# * `Ctrl-Enter` run the current cell and enters command mode.

# 
# 
# ## Managing the Kernel
# 
# Code is run in a separate process called the Kernel.  The Kernel can be interrupted or restarted.  Try running the following cell and then hit the <button class='btn btn-default btn-xs'><i class='icon-stop fa fa-stop'></i></button> button in the toolbar above.
# 
# The "Cell" menu has a number of menu items for running code in different ways. These includes:
# 
# * Run and Select Below
# * Run and Insert Below
# * Run All
# * Run All Above
# * Run All Below
# 
# 

# ## Restarting the kernels
# 
# The kernel maintains the state of a notebook's computations. You can reset this state by restarting the kernel. This is done by clicking on the <button class='btn btn-default btn-xs'><i class='fa fa-repeat icon-repeat'></i></button> in the toolbar above.
# 
# 
# Check the [documentation](https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html).

# # First program
# 
# - Print out the string "Hello world!" and its type.
# - Print out the value of `a` variable set to 6625 and its type.

# In[1]:


s = "Hello World!"
print(type(s),s)
a = 6625
print(type(a),a)
# a+s  # returns TypeError: unsupported operand type(s) for +: 'int' and 'str'


# ## Execute using python

# In[2]:


get_ipython().run_cell_magic('file', 'hello.py', '\ns = "Hello World!"\nprint(type(s),s)\na = 6625\nprint(type(a),a)')


# ```bash
# $ python3 hello.py
# <class 'str'> Hello World!
# <class 'int'> 6625
# ```

# ## Execute with ipython
# ```ipython
# $ ipython
# Python 3.6.3 | packaged by conda-forge | (default, Nov  4 2017, 10:13:32)
# Type 'copyright', 'credits' or 'license' for more information
# IPython 6.2.1 -- An enhanced Interactive Python. Type '?' for help.
# 
# In [1]: run hello.py
# <class 'str'> Hello World!
# <class 'int'> 6625
# ```

# # Python Types
# - Most of Python types are classes, typing is dynamic.
# - ; symbol can be used to split two Python commands on the same line.

# In[3]:


s = int(2010); print(type(s))
s = 3.14; print(type(s))
s = True; print(type(s))
s = None; print(type(s))
s = 1.0j; print(type(s))
s = type(type(s)); print(type(s))


# # Calculate with Python

# In[4]:


x = 45      # This is a comment!
x += 2        # equivalent to x = x + 2
print(x, x > 45)


# In[5]:


y = 2.5
print("x+y=",x+y, type(x+y))  # Add float to integer, result will be a float


# In[6]:


print(x*10/y)   # true division returns a float
print(x*10//3)  # floor division discards the fractional part


# In[7]:


print( x % 8) # the % operator returns the remainder of the division


# In[8]:


print( "x = %05d " % x) # You can use C format rules to improve print output


# # Multiple Assignment
# - Variables can simultaneously get new values. 
# - Expressions on the right-hand side are all evaluated first before assignments take place. 
# - The right-hand side expressions are evaluated from the left to the right.
# - Use it very carefully

# In[9]:


a = b = c = 1
print(a, b, c) 


# In[10]:


a, b, c = 1, 2, 3
print (a, b, c)


# In[11]:


a, c = c, a     # Nice way to permute values
print (a, b, c) 


# In[12]:


a < b < c, a > b > c


# # `input` Function

# In[13]:


# name = input("Please enter your name: ")
# name


# In[14]:


# x = int(input("Please enter an integer: "))
# x


# In[15]:


# l = list(input("Please enter 3 values "))
# l

