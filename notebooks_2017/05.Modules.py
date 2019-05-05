#!/usr/bin/env python
# coding: utf-8

# # Modules
# 
# If your Python program gets longer, you may want to split it into several files for easier maintenance. To support this, Python has a way to put definitions in a file and use them in a script or in an interactive instance of the interpreter. Such a file is called a module.

# Run the cell below to create a file named fibo.py with several functions inside:

# In[1]:


get_ipython().run_cell_magic('file', 'fibo.py', '""" Simple module with\n    two functions to compute Fibonacci series """\n\ndef fib1(n):\n   """ write Fibonacci series up to n """\n   a, b = 0, 1\n   while b < n:\n      print(b, end=\', \')\n      a, b = b, a+b\n\ndef fib2(n):   \n    """ return Fibonacci series up to n """\n    result = []\n    a, b = 0, 1\n    while b < n:\n        result.append(b)\n        a, b = b, a+b\n    return result\n\nif __name__ == "__main__":\n    import sys\n    fib1(int(sys.argv[1]))')


# You can use the function fib by importing fibo which is the name of the file without .py extension.

# In[6]:


import fibo
print(fibo.__name__)
print(fibo.__file__)
fibo.fib1(1000)


# In[8]:


help(fibo)


# # Executing modules as scripts
# 
# When you run a Python module with
# ```bash
# $ python fibo.py <arguments>
# ```
# the code in the module will be executed, just as if you imported it, but with the __name__ set to "__main__". The following code will be executed only in this case and not when it is imported.
# ```python
# if __name__ == "__main__":
#     import sys
#     fib(int(sys.argv[1]))
# ```
# In Jupyter notebook, you can run the fibo.py python script using magic command.

# In[9]:


get_ipython().run_line_magic('run', 'fibo.py 1000')


# The module is also imported.

# In[10]:


fib1(1000)


# ## Different ways to import a module
# ```python
# import fibo
# import fibo as f
# from fibo import fib1, fib2
# from fibo import *
# ```

# - Last command with '*' imports all names except those beginning with an underscore (_). In most cases, do not use this facility since it introduces an unknown set of names into the interpreter, possibly hiding some things you have already defined.

# - If a function with same name is present in different modules imported. Last module function imported replace the previous one.

# In[11]:


from numpy import sqrt
from scipy import sqrt
sqrt(-1)


# In[13]:


from scipy import sqrt
from numpy import sqrt
sqrt(-1)


# In[16]:


import numpy as np
import scipy as sp

print(np.sqrt(-1+0j), sp.sqrt(-1))


# - For efficiency reasons, each module is only imported once per interpreter session. Therefore, if you change your modules, you must restart the interpreter 
# – If you really want to test interactively after a long run, use :
# ```python
# import importlib
# importlib.reload(modulename)
# ```

# # The Module Search Path
# 
# When a module is imported, the interpreter searches for a file named module.py in a list of directories given by the variable sys.path.
# - Python programs can modify sys.path
# - export the PYTHONPATH environment variable to change it on your system.

# In[17]:


import sys
sys.path


# In[18]:


import collections
collections.__path__


# # Packages
# 
# - A package is a directory containing Python module files.
# - This directory always contains a file name \_\_init\_\_.py
# 
# <pre>
# marseille
# ├── __init__.py
# ├── calanques
# │   ├── __init__.py
# │   ├── morgiou.py
# │   ├── sorgiou.py
# │   └── sugiton.py
# └── cirm
#     ├── __init__.py
#     ├── annexe.py
#     ├── auditorium.py
#     └── bastide.py
# </pre>

# ## Relative imports
# 
# These imports use leading dots to indicate the current and parent packages involved in the relative import. In the sugiton module, you can use:
# ```python
# from . import morgiou # import module in the same directory
# from .. import cirm   # import module in parent directory
# from ..cirm import bastide # import module in another subdirectory of the parent directory
# ```

# ## Reminder
# 
# Don't forget that importing * is not recommended

# In[23]:


sum(range(5),-1)


# In[28]:


from numpy import *
sum(range(5),-1)


# In[29]:


del sum # delete imported sum function from numpy 
help(sum)


# In[30]:


import numpy as np
help(np.sum)

