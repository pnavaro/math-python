# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     cell_metadata_json: true
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.5'
#       jupytext_version: 1.3.2
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# + {"slideshow": {"slide_type": "slide"}}
# %matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (10,6)

# + [markdown] {"slideshow": {"slide_type": "fragment"}}
# - The first line is specific to jupyter notebook, figures are displayed under cell
# - numpy module is always imported like this, every numpy command begin by np.
# - pyplot is a matplotlib subpackage similar to the matlab interface
# - We set the size of all figures to 10cm x 6cm

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # What provide Numpy to Python ?
#
# - `ndarray` multi-dimensional array object
# - derived objects such as masked arrays and matrices
# - `ufunc` fast array mathematical operations.
# - Offers some Matlab-ish capabilities within Python
# - Initially developed by [Travis Oliphant](https://www.continuum.io/people/travis-oliphant).
# - Numpy 1.0 released October, 2006.
# - The [SciPy.org website](https://docs.scipy.org/doc/numpy) is very helpful.
# - NumPy fully supports an object-oriented approach.
# -

# # Routines for fast operations on arrays.
#
#     - shape manipulation
#     - sorting
#     - I/O
#     - FFT
#     - basic linear algebra
#     - basic statistical operations
#     - random simulation
#     - statistics
#     - and much more...

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Getting Started with NumPy
#
# - It is handy to import everything from NumPy into a Python console:
# ```python
# from numpy import *
# ```
# - But it is easier to read and debug if you use explicit imports.
# ```python
# import numpy as np
# import scipy as sp
# import matplotlib.pyplot as plt
# ```

# + {"slideshow": {"slide_type": "fragment"}}
import numpy as np
print(np.__version__)

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Why Arrays ?

# + [markdown] {"slideshow": {"slide_type": "fragment"}}
# - Python lists are slow to process and use a lot of memory.
# - For tables, matrices, or volumetric data, you need lists of lists of lists... which becomes messy to program.

# + {"slideshow": {"slide_type": "fragment"}}
from random import random
from operator import truediv

# + {"slideshow": {"slide_type": "fragment"}}
l1 = [random() for i in range(1000)]
l2 = [random() for i in range(1000)]
# %timeit s = sum(map(truediv,l1,l2))

# + {"slideshow": {"slide_type": "fragment"}}
a1 = np.array(l1)
a2 = np.array(l2)
# %timeit s = np.sum(a1/a2)

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Numpy Arrays: The `ndarray` class.
#
# - There are important differences between NumPy arrays and Python lists:
#     - NumPy arrays have a fixed size at creation.
#     - NumPy arrays elements are all required to be of the same data type.
#     - NumPy arrays operations are performed in compiled code for performance.
# - Most of today's scientific/mathematical Python-based software use NumPy arrays.
# - NumPy gives us the code simplicity of Python, but the operation is speedily executed by pre-compiled C code.

# + {"slideshow": {"slide_type": "fragment"}}
a = np.array([0,1,2,3])  #  list
b = np.array((4,5,6,7))  #  tuple
c = np.matrix('8 9 0 1') #  string (matlab syntax)

# + {"slideshow": {"slide_type": "fragment"}}
print(a,b,c)

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Element wise operations are the “default mode” 
#
# - arrays shape must match

# + {"slideshow": {"slide_type": "fragment"}}
a*b, a+b

# + {"slideshow": {"slide_type": "fragment"}}
5*a, 5+a

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# #  NumPy Arrays Properties

# + {"slideshow": {"slide_type": "fragment"}}
a = np.array([1,2,3,4,5]) # Simple array creation

# + {"slideshow": {"slide_type": "fragment"}}
type(a) # Checking the type

# + {"slideshow": {"slide_type": "fragment"}}
a.dtype # Print numeric type of elements

# + {"slideshow": {"slide_type": "slide"}}
a.shape # returns a tuple listing the length along each dimension

# + {"slideshow": {"slide_type": "fragment"}}
np.size(a), a.size # returns the entire number of elements.

# + {"slideshow": {"slide_type": "fragment"}}
a.ndim  # Number of dimensions

# + [markdown] {"slideshow": {"slide_type": "fragment"}}
# - ** Always use `shape` or `size` for numpy arrays instead of `len` **
# - `len` gives same information only for 1d array.

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Functions to allocate arrays

# + {"slideshow": {"slide_type": "fragment"}}
x = np.zeros((4),dtype=('i4,f4,a10'))
x

# + [markdown] {"slideshow": {"slide_type": "fragment"}}
# `empty, empty_like, ones, ones_like, zeros, zeros_like, full, full_like`

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# #  Setting Array Elements Values

# + {"slideshow": {"slide_type": "fragment"}}
a = np.array([1,2,3,4,5])
print(a.dtype)

# + {"slideshow": {"slide_type": "fragment"}}
a[0] = 10 # Change first item value
a, a.dtype

# + {"slideshow": {"slide_type": "fragment"}}
a.fill(0) # slighty faster than a[:] = 0
a

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Setting Array Elements Types

# + {"slideshow": {"slide_type": "fragment"}}
b = np.array([1,2,3,4,5.0]) # Last item is a float
b, b.dtype

# + {"slideshow": {"slide_type": "fragment"}}
a.fill(3.0)  # assigning a float into a int array 
a[1] = 1.5   # truncates the decimal part
print(a.dtype, a)

# + {"slideshow": {"slide_type": "fragment"}}
a.astype('float64') # returns a new array containing doubles

# + {"slideshow": {"slide_type": "fragment"}}
np.asfarray([1,2,3,4]) # Return an array converted to a float type

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Slicing x[lower:upper:step]
# - Extracts a portion of a sequence by specifying a lower and upper bound.
# - The lower-bound element is included, but the upper-bound element is **not** included.
# - The default step value is 1 and can be negative.

# + {"slideshow": {"slide_type": "fragment"}}
a = np.array([10,11,12,13,14])

# + {"slideshow": {"slide_type": "fragment"}}
a[:2], a[-5:-3], a[0:2], a[-2:] # negative indices work

# + {"slideshow": {"slide_type": "fragment"}}
a[::2], a[::-1]

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise: 
# - Compute derivative of $f(x) = \sin(x)$ with finite difference method.
# $$
#     \left(\frac{\partial f}{\partial x} \right)_{i+1/2} \sim \frac{f(x_{i+1})-f(x_i)}{dx}
# $$
# derivatives values are centered in-between sample points.
#
# - Compute integral using trapezoidal rule with $f(x) = e^{-x^2}$
#
# $$
# \int_{-6}^{6} f(x)\,dx = \frac{dx}{2} \sum_{k=1}^{n-1} \left(f(x)+f(x+dx) \right)
# $$
#
#

# + {"slideshow": {"slide_type": "slide"}}
# %matplotlib inline
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [12.,8.] # Increase plot size

# + {"slideshow": {"slide_type": "fragment"}}
x, dx = np.linspace(0,4*np.pi,100, retstep=True)
y = np.sin(x)
plt.plot(x, y);

# + {"slideshow": {"slide_type": "slide"}}

plt.plot(x, np.cos(x),'b')
plt.title(r"$\rm{Derivative\ of}\ \sin(x)$");

# + {"slideshow": {"slide_type": "slide"}}
# Compute integral of x numerically
avg_height = 0.5*(y[1:]+y[:-1])
int_sin = np.cumsum(dx*avg_height)
plt.plot(x[1:], int_sin, 'ro', x, np.cos(0)-np.cos(x));

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Multidimensional array

# + {"slideshow": {"slide_type": "fragment"}}
a = np.arange(4*3).reshape(4,3) # NumPy array
l = [[0,1,2],[3,4,5],[6,7,8],[9,10,11]] # Python List

# + {"slideshow": {"slide_type": "fragment"}}
print(a)
print(l)

# + {"slideshow": {"slide_type": "slide"}}
l[-1][-1] # Access to last item

# + {"slideshow": {"slide_type": "fragment"}}
print(a[-1,-1])  # Indexing syntax is different with NumPy array
print(a[0,0])    # returns the first item
print(a[1,:])    # returns the second line

# + {"slideshow": {"slide_type": "fragment"}}
print(a[1]) # second line with 2d array
print(a[:,-1])  # last column

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise: Create the following arrays
# ```python
# [100 101 102 103 104 105 106 107 108 109]
# ```
# Hint: np.arange
# ```python
# [-2. -1.8 -1.6 -1.4 -1.2 -1. -0.8 -0.6 -0.4 -0.2 0. 
# 0.2 0.4 0.6 0.8 1. 1.2 1.4 1.6 1.8]
# ```
# Hint: np.linspace
# ```python
# [[ 0.001	0.00129155 0.0016681 0.00215443 0.00278256 
#      0.003593810.00464159 0.00599484 0.00774264 0.01]
# ```
# Hint: np.logspace
# ```python
# [[ 0. 0. -1. -1. -1.] 
#  [ 0. 0.  0. -1. -1.] 
#  [ 0. 0.  0.  0. -1.]
#  [ 0. 0.  0.  0.  0.]
#  [ 0. 0.  0.  0.  0.] 
#  [ 0. 0.  0.  0.  0.] 
#  [ 0. 0.  0.  0.  0.]]
# ```
# Hint: np.tri, np.zeros, np.transpose
#
# ```python
# [[ 0.  1.  2.  3. 4.] 
#  [-1.  0.  1.  2. 3.] 
#  [-1. -1.  0.  1. 2.] 
#  [-1. -1. -1.  0. 1.] 
#  [-1. -1. -1. -1. 0.]]
# ```
# Hint: np.ones, np.diag
#

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise 
# - We compute numerically the Laplace Equation Solution using Finite Difference Method
# - Replace the computation of the discrete form of Laplace equation with numpy arrays
# $$
# T_{i,j} = \frac{1}{4} ( T_{i+1,j} + T_{i-1,j} + T_{i,j+1} + T_{i,j-1})
# $$
# - The function numpy.allclose can help you to compute the residual.

# + {"slideshow": {"slide_type": "slide"}}
# %%time
# Boundary conditions
Tnorth, Tsouth, Twest, Teast = 100, 20, 50, 50

# Set meshgrid
n, l = 64, 1.0
X, Y = np.meshgrid(np.linspace(0,l,n), np.linspace(0,l,n))
T = np.zeros((n,n))

# Set Boundary condition
T[n-1:, :] = Tnorth
T[:1, :]   = Tsouth
T[:, n-1:] = Teast
T[:, :1]   = Twest

residual = 1.0   
istep = 0
while residual > 1e-5 :
    istep += 1
    print ((istep, residual), end="\r")
    residual = 0.0   
    for i in range(1, n-1):
        for j in range(1, n-1):
            T_old = T[i,j]
            T[i, j] = 0.25 * (T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1])
            if T[i,j]>0:
                residual=max(residual,abs((T_old-T[i,j])/T[i,j]))


print()
print("iterations = ",istep)
plt.title("Temperature")
plt.contourf(X, Y, T)
plt.colorbar()

# +
import numpy as np
import itertools
import matplotlib.pyplot as plt

# Boundary conditions
Tnorth, Tsouth, Twest, Teast = 100, 20, 50, 50

# Set meshgrid
n, l = 64, 1.0
X, Y = np.meshgrid(np.linspace(0,l,n), np.linspace(0,l,n))
T = np.zeros((n,n))

# Set Boundary condition
T[n-1:, :] = Tnorth
T[:1, :] = Tsouth
T[:, n-1:] = Teast
T[:, :1] = Twest

for istep in itertools.count():
    T_old = T[1:-1,1:-1]
    T_new = (T[1:-1,2:]+T[2:,1:-1]+T[1:-1,:-2]+T[:-2,1:-1])*0.25
    if np.allclose(T_new, T_old, rtol=1e-5): break
    T[1:-1,1:-1] = T_new

print()
print("iterations = ",istep)
plt.title("Temperature")
plt.contourf(X, Y, T)
plt.colorbar()


# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Arrays to ASCII files
#

# + {"slideshow": {"slide_type": "fragment"}}
x = y = z = np.arange(0.0,5.0,1.0)

# + {"slideshow": {"slide_type": "fragment"}}
np.savetxt('test.out', (x,y,z), delimiter=',')   # X is an array
# %cat test.out

# + {"slideshow": {"slide_type": "slide"}}
np.savetxt('test.out', (x,y,z), fmt='%1.4e')   # use exponential notation
# %cat test.out

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Arrays from ASCII files

# + {"slideshow": {"slide_type": "fragment"}}
np.loadtxt('test.out')

# + [markdown] {"slideshow": {"slide_type": "fragment"}}
# - [save](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.save.html#numpy.save): Save an array to a binary file in NumPy .npy format
# - [savez](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savez.html#numpy.savez) : Save several arrays into an uncompressed .npz archive
# - [savez_compressed](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed): Save several arrays into a compressed .npz archive
# - [load](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.load.html#numpy.load): Load arrays or pickled objects from .npy, .npz or pickled files.

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ## H5py
#
# Pythonic interface to the HDF5 binary data format. [h5py user manual](http://docs.h5py.org)

# + {"slideshow": {"slide_type": "fragment"}}
import h5py as h5

with h5.File('test.h5','w') as f:
    f['x'] = x
    f['y'] = y
    f['z'] = z

# + {"slideshow": {"slide_type": "fragment"}}
with h5.File('test.h5','r') as f:
    for field in f.keys():
        print(field+':',f.get(field))


# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Slices Are References
# - Slices are references to memory in the original array.
# - Changing values in a slice also changes the original array.
#

# + {"slideshow": {"slide_type": "fragment"}}
a = np.arange(10)
b = a[3:6]
b  # `b` is a view of array `a` and `a` is called base of `b`

# + {"slideshow": {"slide_type": "fragment"}}
b[0] = -1
a  # you change a view the base is changed.

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# - Numpy does copy only if it is necessary to save memory.

# + {"slideshow": {"slide_type": "fragment"}}
c = a[7:8].copy() # Explicit copy of the array slice
c[0] = -1 
a

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Fancy Indexing

# + {"slideshow": {"slide_type": "fragment"}}
a = np.random.randint(20, size=(4, 5))
a

# + {"slideshow": {"slide_type": "fragment"}}
np.random.shuffle(a.flat) # shuffle modify only the first axis
a

# + {"slideshow": {"slide_type": "slide"}}
locations = a % 3 == 0 # locations can be used as a mask
a[locations] = 0 #set to 0 only the values that are divisible by 3
a

# + {"slideshow": {"slide_type": "fragment"}}
a += a == 0
a

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ### `numpy.take`

# + {"slideshow": {"slide_type": "fragment"}}
a = np.fromfunction(lambda i, j: (i+1)*10+j+1, (4, 5), dtype=int)
a

# + {"slideshow": {"slide_type": "fragment"}}
a[1:3,2:5] # intersection line 1:2 and 2:5

# + {"slideshow": {"slide_type": "fragment"}}
np.take(a,[[6,7],[10,11]])  # Use flatten array indices

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Changing array shape

# + {"slideshow": {"slide_type": "fragment"}}
grid = np.indices((3,5)) # Return an array representing the indices of a grid.
grid[0]

# + {"slideshow": {"slide_type": "fragment"}}
grid[1]

# + {"slideshow": {"slide_type": "slide"}}
grid.flat[:] # Return a view 

# + {"slideshow": {"slide_type": "fragment"}}
grid.flatten() # Return a copy
# -

grid.flatten

# + {"slideshow": {"slide_type": "fragment"}}
np.ravel(grid, order='C') # A copy is made only if needed.

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Sorting

# + {"slideshow": {"slide_type": "fragment"}}
a=np.array([5,3,6,1,6,7,9,0,8])
np.sort(a) #. Return a view

# + {"slideshow": {"slide_type": "fragment"}}
a

# + {"slideshow": {"slide_type": "fragment"}}
a.sort() # Change the array inplace
a

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Transpose-like operations

# + {"slideshow": {"slide_type": "fragment"}}
a = np.array([5,3,6,1,6,7,9,0,8])
b = a
b.shape = (3,3) # b is a reference so a will be changed

# + {"slideshow": {"slide_type": "fragment"}}
a

# + {"slideshow": {"slide_type": "fragment"}}
c = a.T # Return a view so a is not changed
np.may_share_memory(a,c)

# + {"slideshow": {"slide_type": "fragment"}}
c[0,0] = -1 # c is stored in same memory so change c you change a
a

# + {"slideshow": {"slide_type": "slide"}}
c  # is a transposed view of a

# + {"slideshow": {"slide_type": "fragment"}}
b  # b is a reference to a

# + {"slideshow": {"slide_type": "fragment"}}
c.base  # When the array is not a view `base` return None

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Methods Attached to NumPy Arrays

# + {"slideshow": {"slide_type": "fragment"}}
a = np.arange(20).reshape(4,5)
np.random.shuffle(a.flat)
a

# + {"slideshow": {"slide_type": "fragment"}}
a = (a - a.mean())/ a.std() # Standardize the matrix
print(a)

# + {"slideshow": {"slide_type": "slide"}}
np.set_printoptions(precision=4)
print(a)

# + {"slideshow": {"slide_type": "fragment"}}
a.argmax() # max position in the memory contiguous array

# + {"slideshow": {"slide_type": "fragment"}}
np.unravel_index(a.argmax(),a.shape) # get position in the matrix

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Array Operations over a given axis

# + {"slideshow": {"slide_type": "fragment"}}
a = np.arange(20).reshape(5,4)
#np.random.shuffle(a.flat)
a

# + {"slideshow": {"slide_type": "fragment"}}
a.sum(axis=0) # sum of each column
# -

a == 10

# + {"slideshow": {"slide_type": "fragment"}}
np.apply_along_axis(sum, axis=0, arr=a)

# + {"slideshow": {"slide_type": "fragment"}}
np.apply_along_axis(sorted, axis=0, arr=a)

# + [markdown] {"slideshow": {"slide_type": "fragment"}}
# You can replace the `sorted` builtin fonction by a user defined function.

# + {"slideshow": {"slide_type": "slide"}}
np.eye(4)

# + {"slideshow": {"slide_type": "fragment"}}
a = np.diag(range(4))
a
# -

# # Compute distances

# + {"slideshow": {"slide_type": "slide"}}
rng = np.random.RandomState(1111)
X = rng.rand(10,2)
plt.scatter(X[:,0], X[:,1])
for (i,x) in enumerate(X):
    plt.text(x[0], x[1]+0.02, str(i))

# + {"slideshow": {"slide_type": "slide"}}
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
differences

# + {"slideshow": {"slide_type": "slide"}}
# square the coordinate differences
sq_differences = differences ** 2
sq_differences

# + {"slideshow": {"slide_type": "slide"}}
# sum the coordinate differences to get the squared distance
dist_sq = sq_differences.sum(-1)
dist_sq
# -

nearest = np.argsort(dist_sq, axis=1)
print(nearest)

# + {"slideshow": {"slide_type": "slide"}}
K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
print(nearest_partition)

# + {"slideshow": {"slide_type": "slide"}}
# %matplotlib inline
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], s=100)

# draw lines from each point to its two nearest neighbors
K = 5

i=3
for j in nearest_partition[i, :K+1]:
    # plot a line from X[i] to X[j]
    # use some zip magic to make it happen:
    
    plt.plot(*zip(X[j], X[i]), color='black')

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Views and Memory Management
# - If it exists one view of a NumPy array, it can be destroyed.
#

# + {"slideshow": {"slide_type": "fragment"}}
big = np.arange(1000000)
small = big[:5]
del big
small.base

# + [markdown] {"slideshow": {"slide_type": "fragment"}}
# - Array called `big` is still allocated.
# - Sometimes it is better to create a copy.

# + {"slideshow": {"slide_type": "fragment"}}
big = np.arange(1000000)
small = big[:5].copy()
del big
print(small.base)

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Change memory alignement

# + {"slideshow": {"slide_type": "fragment"}}
del(a)
a = np.random.randint(20, size=(5,4))
a

# + {"slideshow": {"slide_type": "fragment"}}
print(a.flags)

# + {"slideshow": {"slide_type": "fragment"}}
b = np.asfarray(a) # makes a copy
b.flags
# -

c = np.ravel(a)
c.flags

c.base

# + {"slideshow": {"slide_type": "fragment"}}
c.base is a

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Broadcasting rules
#
# Broadcasting rules allow you to make an outer product between two vectors: the first method involves array tiling, the second one involves broadcasting. The last method is significantly faster.
#

# + {"slideshow": {"slide_type": "fragment"}}
n = 1000
a = np.arange(n)
ac = a[:, np.newaxis]   # column matrix
ar = a[np.newaxis, :]   # row matrix

# + {"slideshow": {"slide_type": "fragment"}}
# %timeit np.tile(a, (n,1)).T * np.tile(a, (n,1))

# + {"slideshow": {"slide_type": "fragment"}}
# %timeit ac * ar

# + {"slideshow": {"slide_type": "fragment"}}
np.all(np.tile(a, (n,1)).T * np.tile(a, (n,1)) == ac * ar)

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ## StructuredArray using a compound data type specification

# + {"slideshow": {"slide_type": "fragment"}}
data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)

# + {"slideshow": {"slide_type": "fragment"}}
data['name'] = ['Pierre', 'Paul', 'Jacques', 'Francois']
data['age'] = [45, 10, 71, 39]
data['weight'] = [95.0, 75.0, 88.0, 71.0]
print(data)

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# ## RecordArray

# + {"slideshow": {"slide_type": "fragment"}}
data_rec = data.view(np.recarray)
data_rec.age

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # NumPy Array Programming
# - Array operations are fast, Python loops are slow. 
# - Top priority: **avoid loops**
# - It’s better to do the work three times witharray operations than once with a loop.
# - This does require a change of habits.
# - This does require some experience.
# - NumPy’s array operations are designed to make this possible.

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # initialize a random normal vector with 100 values

# + {"slideshow": {"slide_type": "fragment"}}
n = 100
mu, sigma = 0, 1.0
X = np.random.normal(mu, sigma, n)
X

# + {"slideshow": {"slide_type": "slide"}}
rng = np.random.RandomState(42)
X = rng.normal(mu, sigma, 100)
X

# + {"slideshow": {"slide_type": "fragment"}}
b = np.array([1.0, 2.0]) # numpy array from python list
y = np.random.normal(size=n) +  b[0] + b[1] * X # always element by element operations

# + {"slideshow": {"slide_type": "fragment"}}
x = np.linspace(-3,3,100) # create a numpy array lineary spaced from -3 to 3 with 100 points
plt.scatter(X, y, c='r')
plt.plot(x, b[0]+b[1]*x, 'b')

# + {"slideshow": {"slide_type": "slide"}}
import seaborn as sns
sns.set(style='whitegrid')

sns.regplot(X, y);

# + {"slideshow": {"slide_type": "slide"}}
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

model = linear_model.LinearRegression()

X = X[:,np.newaxis] # scikit-learn is waiting for a Matrix

model.fit(X, y)
print('Coefficient: \n', model.coef_)
model.intercept_
# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Linear regression with the classic formula
#
# $$
# w = (X^tX)^{-1} X^tY
# $$

# + {"slideshow": {"slide_type": "fragment"}}
if ~np.all( X[:,0] == 1.0):
    X = np.insert(X, 0, 1, axis=1) # insert a first column of ones 

X[:10] # first ten lines

# + {"slideshow": {"slide_type": "fragment"}}
X_sq_reg_inv = np.linalg.inv(X.T @ X) # inv(X'X)
w = X_sq_reg_inv.dot(X.T).dot(y)  
# w = (X_sq_reg_inv @ X.T) @ y  
# w = np.dot(np.dot(X_sq_reg_inv, X.T), y)

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # Calculate weights by least squares  (using Moore-Penrose pseudoinverse)
#
#

# + {"slideshow": {"slide_type": "fragment"}}
U, S, V = np.linalg.svd(X.T.dot(X))
X_sq_reg_inv = V.T.dot(np.diag(1/S)).dot(U.T)
w = X_sq_reg_inv.dot(X.T).dot(y)
w

# + {"slideshow": {"slide_type": "fragment"}}
w = np.linalg.pinv(X).dot(y)
w

# + [markdown] {"slideshow": {"slide_type": "slide"}}
# # References
# - [NumPy reference](http://docs.scipy.org/doc/numpy/reference/)
# - [Getting the Best Performance out of NumPy](http://ipython-books.github.io/featured-01/)
# - [Numpy by Konrad Hinsen](http://calcul.math.cnrs.fr/Documents/Ecoles/2013/python/NumPy%20avance.pdf)
# - [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
