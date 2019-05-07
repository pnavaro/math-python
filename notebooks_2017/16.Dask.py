# ---
# jupyter:
#   jupytext:
#     comment_magics: false
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.2'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python (math-python)
#     language: python
#     name: math-python
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Dask Features
#
# - process data that doesn't fit into memory by breaking it into blocks and specifying task chains
# - parallelize execution of tasks across cores and even nodes of a cluster
# - move computation to the data rather than the other way around, to minimize communication overheads
#
#

# %% {"slideshow": {"slide_type": "slide"}}
import sys
import dask
import dask.multiprocessing

# %% {"slideshow": {"slide_type": "slide"}}
from time import sleep

def slowinc(x, delay=1):
    sleep(delay)
    return x + 1

def slowadd(x, y, delay=1):
    sleep(delay)
    return x + y


# %% {"slideshow": {"slide_type": "fragment"}}
%%time
x = slowinc(1)
y = slowinc(2)
z = slowadd(x, y)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Parallelize with dask.delayed
#
# - Functions wrapped by `dask.delayed` don't run immediately, but instead put those functions and arguments into a task graph. 
# - The result is computed separately by calling the `.compute()` method.

# %% {"slideshow": {"slide_type": "fragment"}}
from dask import delayed

# %% {"slideshow": {"slide_type": "fragment"}}
x = delayed(slowinc)(1)
y = delayed(slowinc)(2)
z = delayed(slowadd)(x, y)

# %% {"slideshow": {"slide_type": "fragment"}}
%%time
z.compute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Dask graph
#
# - Contains description of the calculations necessary to produce the result. 
# - The z object is a lazy Delayed object. This object holds everything we need to compute the final result. We can compute the result with .compute() as above or we can visualize the task graph for this value with .visualize().

# %% {"slideshow": {"slide_type": "fragment"}}
z.visualize()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Parallelize a loop
#

# %% {"slideshow": {"slide_type": "fragment"}}
data = [1, 2, 3, 4, 5, 6, 7, 8]

# %% {"slideshow": {"slide_type": "fragment"}}
%%time

results = []
for x in data:
    y = slowinc(x)
    results.append(y)
    
total = sum(results)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 5.1
#
# - Parallelize this by appending the delayed `slowinc` calls to the list `results`.
# - Display the graph of `total` computation
# - Compute time elapsed for the computation.

# %% {"slideshow": {"slide_type": "fragment"}}
results = []
for x in data:
    y = delayed(slowinc)(x)
    results.append(y)
    
total = (delayed)(sum)(results)

# %% {"slideshow": {"slide_type": "slide"}}
total.visualize()

# %% {"slideshow": {"slide_type": "slide"}}
%%time
total.compute()

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Control flow
# -  Delay only some functions, running a few of them immediately. This is helpful when those functions are fast and help us to determine what other slower functions we should call. 
# - In the example below we iterate through a list of inputs. If that input is even then we want to call `half`. If the input is odd then we want to call `odd_process`. This iseven decision to call `half` or `odd_process` has to be made immediately (not lazily) in order for our graph-building Python code to proceed.
#

# %% {"slideshow": {"slide_type": "fragment"}}
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

# %% {"slideshow": {"slide_type": "fragment"}}
%%time
results = []
for x in data:
    if is_even(x):
        y = half(x)
    else:
        y = odd_process(x)
    results.append(y)
    
total = sum(results)
print(total)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 5.2
# - Parallelize the sequential code above using dask.delayed
# - You will need to delay some functions, but not all
# - Visualize and check the computed result
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Parallel Collections: Dask bag
#
# Systems like Spark and Dask include "big data" collections with a small set of high-level primitives like map, filter, groupby, and join. With these common patterns we can often handle computations that are more complex than map, but are still structured.
# In this section we repeat the submit example using the PySpark and the Dask.Bag APIs, which both provide parallel operations on linear collections of arbitrary objects.
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Spark/Dask.bag methods
# We can construct most of the above computation with the following Spark/Dask.bag methods:
# - *collection.map(function)*: apply function to each element in collection
# - *collection.product(collection)*: Create new collection with every pair of inputs
# - *collection.filter(predicate)*: Keep only elements of colleciton that match the predicate function
# - *collection.max()*: Compute maximum element
# We use these briefly in isolated exercises and then combine them to rewrite the previous computation from the submit section.

# %% {"slideshow": {"slide_type": "slide"}}
import dask.bag as db

seq = list(range(8))

b = db.from_sequence(seq)
b

# %% {"slideshow": {"slide_type": "fragment"}}
b.compute() 

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## map

# %% {"slideshow": {"slide_type": "fragment"}}
%%time 
res = map(slowinc, seq) # apply slow inc on each element
print(*res)

# %% {"slideshow": {"slide_type": "fragment"}}
%time b.map(slowinc).compute()

# %% {"slideshow": {"slide_type": "fragment"}}
b.filter(lambda x: x % 2 == 0).compute()

# %% {"slideshow": {"slide_type": "slide"}}
# Cartesian product of each pair of elements in two sequences (or the same sequence in this case)

b.product(b).compute()

# %% {"slideshow": {"slide_type": "slide"}}
# Chain operations to construct more complex computations

(b.map(lambda x: x ** 2)
  .product(b)
  .filter(lambda tup: tup[0] % 2 == 0)
  .compute())


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 5.3
# - Parallelize the hdf5 conversion from json files
# - Create a function `convert_to_hdf`
# - Use dask.compute function on delayed calls of the funtion created list
# - Is it really  faster as expected ?

# %% {"slideshow": {"slide_type": "slide"}}
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

# %% {"slideshow": {"slide_type": "slide"}}
%%time
import os, sys
from glob import glob
import pandas as pd
import json


here = os.getcwd() # get the current directory


stocks = ['hal', 'hp', 'hpq', 'ibm', 'jbl', 'jpm', 'luv', 'pcg','usb']


def convert_to_json(d):
    """ Convert all csv files of directory d into json format """
    filenames = sorted(glob(os.path.join(d, '*')))[-365:]
    outfn = d.replace('minute', 'json') + '.json'
    if os.path.exists(outfn):
        return
    with open(outfn, 'w') as f:
        for fn in filenames:
            df = pd.read_csv(fn)
            for rec in df.to_dict(orient='records'):
                json.dump(rec, f)
                f.write('\n')
    print("Finished JSON: %s" % d.split(os.path.sep)[-1])


js = os.path.join(here, '../data', 'json')
if not os.path.exists(js):
    os.mkdir(js)

for d in sorted(glob(os.path.join(here, '../data', 'minute', '*'))):
    convert_to_json(d)

# %% {"slideshow": {"slide_type": "slide"}}
import os, glob
filenames = sorted(glob.glob(os.path.join('../data', 'json', '*.json')))
filenames

# %% {"slideshow": {"slide_type": "slide"}}
%%time

import json # or ujson
for fn in filenames:
    with open(fn) as f:
        data = [json.loads(line) for line in f]
        
    df = pd.DataFrame(data)
    
    out_filename = fn[:-5] + '.h5'
    df.to_hdf(out_filename, '/data')
    print("Finished : %s" % out_filename.split(os.path.sep)[-1])

# %% {"slideshow": {"slide_type": "slide"}}
from glob import glob
import os

filenames = sorted(glob(os.path.join('..', 'data', 'json', '*.h5')))  # ../data/json/*.json

# %% {"slideshow": {"slide_type": "slide"}}
%%time
series = {}
for fn in filenames:   # Simple map over filenames
    series[fn] = pd.read_hdf(fn)['close']

results = {}

for a in filenames:    # Doubly nested loop over the same collection
    for b in filenames:  
        if a != b:     # Filter out bad elements
            results[a, b] = series[a].corr(series[b])  # Apply function

((a, b), corr) = max(results.items(), key=lambda kv: kv[1])  # Reduction

print(corr)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# We use matplotlib to visually inspect the highly correlated timeseries

# %% {"slideshow": {"slide_type": "fragment"}}
%matplotlib inline
from matplotlib import pyplot as plt
plt.figure(figsize=(10, 4))
plt.plot(series[a]/series[a].max())
plt.plot(series[b]/series[b].max())
plt.xticks(visible=False);

# %% {"slideshow": {"slide_type": "slide"}}
%%time
### Parallel Code

import dask.bag as db

b = db.from_sequence(filenames)
series = b.map(lambda fn: pd.read_hdf(fn)['close'])

corr = (series.product(series)
              .filter(lambda ab: not (ab[0] == ab[1]).all())
              .map(lambda ab: ab[0].corr(ab[1])).max())

result = corr.compute()

# %% {"slideshow": {"slide_type": "fragment"}}
result

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # References
# * [Dask website](https://dask.pydata.org/)
#
