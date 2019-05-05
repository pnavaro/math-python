#!/usr/bin/env python
# coding: utf-8

# # Dask Features
# 
# - process data that doesn't fit into memory by breaking it into blocks and specifying task chains
# - parallelize execution of tasks across cores and even nodes of a cluster
# - move computation to the data rather than the other way around, to minimize communication overheads
# 
# 

# In[1]:


import sys
import dask
import dask.multiprocessing


# In[2]:


from time import sleep

def slowinc(x, delay=1):
    sleep(delay)
    return x + 1

def slowadd(x, y, delay=1):
    sleep(delay)
    return x + y


# In[3]:


get_ipython().run_cell_magic('time', '', 'x = slowinc(1)\ny = slowinc(2)\nz = slowadd(x, y)')


# # Parallelize with dask.delayed
# 
# - Functions wrapped by `dask.delayed` don't run immediately, but instead put those functions and arguments into a task graph. 
# - The result is computed separately by calling the `.compute()` method.

# In[4]:


from dask import delayed


# In[5]:


x = delayed(slowinc)(1)
y = delayed(slowinc)(2)
z = delayed(slowadd)(x, y)


# In[6]:


get_ipython().run_cell_magic('time', '', 'z.compute()')


# # Dask graph
# 
# - Contains description of the calculations necessary to produce the result. 
# - The z object is a lazy Delayed object. This object holds everything we need to compute the final result. We can compute the result with .compute() as above or we can visualize the task graph for this value with .visualize().

# In[7]:


z.visualize()


# # Parallelize a loop
# 

# In[8]:


data = [1, 2, 3, 4, 5, 6, 7, 8]


# In[9]:


get_ipython().run_cell_magic('time', '', '\nresults = []\nfor x in data:\n    y = slowinc(x)\n    results.append(y)\n    \ntotal = sum(results)')


# ### Exercise 5.1
# 
# - Parallelize this by appending the delayed `slowinc` calls to the list `results`.
# - Display the graph of `total` computation
# - Compute time elapsed for the computation.

# In[10]:


results = []
for x in data:
    y = delayed(slowinc)(x)
    results.append(y)
    
total = (delayed)(sum)(results)


# In[11]:


total.visualize()


# In[12]:


get_ipython().run_cell_magic('time', '', 'total.compute()')


# # Control flow
# -  Delay only some functions, running a few of them immediately. This is helpful when those functions are fast and help us to determine what other slower functions we should call. 
# - In the example below we iterate through a list of inputs. If that input is even then we want to call `half`. If the input is odd then we want to call `odd_process`. This iseven decision to call `half` or `odd_process` has to be made immediately (not lazily) in order for our graph-building Python code to proceed.
# 

# In[13]:


from random import randint

def half(x):
    sleep(1)
    return x // 2

def odd_process(x):
    sleep(1)
    return 3*x+1

def is_even(x):
    return not x % 2

data = [randint(0,100) for i in range(8)]
data


# In[14]:


get_ipython().run_cell_magic('time', '', 'results = []\nfor x in data:\n    if is_even(x):\n        y = half(x)\n    else:\n        y = odd_process(x)\n    results.append(y)\n    \ntotal = sum(results)\nprint(total)')


# ### Exercise 5.2
# - Parallelize the sequential code above using dask.delayed
# - You will need to delay some functions, but not all
# - Visualize and check the computed result
# 

# ## Parallel Collections: Dask bag
# 
# Systems like Spark and Dask include "big data" collections with a small set of high-level primitives like map, filter, groupby, and join. With these common patterns we can often handle computations that are more complex than map, but are still structured.
# In this section we repeat the submit example using the PySpark and the Dask.Bag APIs, which both provide parallel operations on linear collections of arbitrary objects.
# 

# ## Spark/Dask.bag methods
# We can construct most of the above computation with the following Spark/Dask.bag methods:
# - *collection.map(function)*: apply function to each element in collection
# - *collection.product(collection)*: Create new collection with every pair of inputs
# - *collection.filter(predicate)*: Keep only elements of colleciton that match the predicate function
# - *collection.max()*: Compute maximum element
# We use these briefly in isolated exercises and then combine them to rewrite the previous computation from the submit section.

# In[15]:


import dask.bag as db

seq = list(range(8))

b = db.from_sequence(seq)
b


# In[16]:


b.compute() 


# ## map

# In[17]:


get_ipython().run_cell_magic('time', '', 'res = map(slowinc, seq) # apply slow inc on each element\nprint(*res)')


# In[18]:


get_ipython().run_line_magic('time', 'b.map(slowinc).compute()')


# In[19]:


b.filter(lambda x: x % 2 == 0).compute()


# In[20]:


# Cartesian product of each pair of elements in two sequences (or the same sequence in this case)

b.product(b).compute()


# In[21]:


# Chain operations to construct more complex computations

(b.map(lambda x: x ** 2)
  .product(b)
  .filter(lambda tup: tup[0] % 2 == 0)
  .compute())


# ### Exercise 5.3
# - Parallelize the hdf5 conversion from json files
# - Create a function `convert_to_hdf`
# - Use dask.compute function on delayed calls of the funtion created list
# - Is it really  faster as expected ?

# In[22]:


import os  # library to get directory and file paths
import tarfile # this module makes possible to read and write tar archives

def extract_daily_stock():
    minutedir = os.path.join('../data', 'minute')
    if not os.path.exists(minutedir):
       print("Extracting daily stock data")
       tar_path = os.path.join('../data', 'daily_stock.tgz')
       with tarfile.open(tar_path, mode='r:gz') as minute:
          minute.extractall('../data/')
            
extract_daily_stock() #


# In[23]:


get_ipython().run_cell_magic('time', '', 'import os, sys\nfrom glob import glob\nimport pandas as pd\nimport json\n\n\nhere = os.getcwd() # get the current directory\n\n\nstocks = [\'hal\', \'hp\', \'hpq\', \'ibm\', \'jbl\', \'jpm\', \'luv\', \'pcg\',\'usb\']\n\n\ndef convert_to_json(d):\n    """ Convert all csv files of directory d into json format """\n    filenames = sorted(glob(os.path.join(d, \'*\')))[-365:]\n    outfn = d.replace(\'minute\', \'json\') + \'.json\'\n    if os.path.exists(outfn):\n        return\n    with open(outfn, \'w\') as f:\n        for fn in filenames:\n            df = pd.read_csv(fn)\n            for rec in df.to_dict(orient=\'records\'):\n                json.dump(rec, f)\n                f.write(\'\\n\')\n    print("Finished JSON: %s" % d.split(os.path.sep)[-1])\n\n\njs = os.path.join(here, \'../data\', \'json\')\nif not os.path.exists(js):\n    os.mkdir(js)\n\nfor d in sorted(glob(os.path.join(here, \'../data\', \'minute\', \'*\'))):\n    convert_to_json(d)')


# In[24]:


import os, glob
filenames = sorted(glob.glob(os.path.join('../data', 'json', '*.json')))
filenames


# In[25]:


get_ipython().run_cell_magic('time', '', '\nimport json # or ujson\nfor fn in filenames:\n    with open(fn) as f:\n        data = [json.loads(line) for line in f]\n        \n    df = pd.DataFrame(data)\n    \n    out_filename = fn[:-5] + \'.h5\'\n    df.to_hdf(out_filename, \'/data\')\n    print("Finished : %s" % out_filename.split(os.path.sep)[-1])')


# In[26]:


from glob import glob
import os

filenames = sorted(glob(os.path.join('..', 'data', 'json', '*.h5')))  # ../data/json/*.json


# In[27]:


get_ipython().run_cell_magic('time', '', "series = {}\nfor fn in filenames:   # Simple map over filenames\n    series[fn] = pd.read_hdf(fn)['close']\n\nresults = {}\n\nfor a in filenames:    # Doubly nested loop over the same collection\n    for b in filenames:  \n        if a != b:     # Filter out bad elements\n            results[a, b] = series[a].corr(series[b])  # Apply function\n\n((a, b), corr) = max(results.items(), key=lambda kv: kv[1])  # Reduction\n\nprint(corr)")


# We use matplotlib to visually inspect the highly correlated timeseries

# In[28]:


get_ipython().run_line_magic('matplotlib', 'inline')
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 4))
plt.plot(series[a]/series[a].max())
plt.plot(series[b]/series[b].max())
plt.xticks(visible=False);


# In[29]:


get_ipython().run_cell_magic('time', '', "### Parallel Code\n\nimport dask.bag as db\n\nb = db.from_sequence(filenames)\nseries = b.map(lambda fn: pd.read_hdf(fn)['close'])\n\ncorr = (series.product(series)\n              .filter(lambda ab: not (ab[0] == ab[1]).all())\n              .map(lambda ab: ab[0].corr(ab[1])).max())\n\nresult = corr.compute()")


# In[30]:


result


# # References
# * [Dask website](https://dask.pydata.org/)
# 
