#!/usr/bin/env python
# coding: utf-8

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

# In[1]:


import numpy as np
print(np.__version__)


# # Why Arrays ?

# - Python lists are slow to process and use a lot of memory.
# - For tables, matrices, or volumetric data, you need lists of lists of lists... which becomes messy to program.

# In[2]:


from random import random
from operator import truediv


# In[3]:


l1 = [random() for i in range(1000)]
l2 = [random() for i in range(1000)]
get_ipython().run_line_magic('timeit', 's = sum(map(truediv,l1,l2))')


# In[4]:


a1 = np.array(l1)
a2 = np.array(l2)
get_ipython().run_line_magic('timeit', 's = np.sum(a1/a2)')


# # Numpy Arrays: The `ndarray` class.
# 
# - There are important differences between NumPy arrays and Python lists:
#     - NumPy arrays have a fixed size at creation.
#     - NumPy arrays elements are all required to be of the same data type.
#     - NumPy arrays operations are performed in compiled code for performance.
# - Most of today's scientific/mathematical Python-based software use NumPy arrays.
# - NumPy gives us the code simplicity of Python, but the operation is speedily executed by pre-compiled C code.

# In[5]:


a = np.array([0,1,2,3])  #  list
b = np.array((4,5,6,7))  #  tuple
c = np.matrix('8 9 0 1') #  string (matlab syntax)


# In[6]:


print(a,b,c)


# ## Element wise operations are the “default mode” 

# In[7]:


a*b,a+b


# In[8]:


5*a, 5+a


# In[9]:


a @ b, np.dot(a,b)  # Matrix multiplication


# #  NumPy Arrays Properties

# In[10]:


a = np.array([1,2,3,4,5]) # Simple array creation


# In[11]:


type(a) # Checking the type


# In[12]:


a.dtype # Print numeric type of elements


# In[13]:


a.itemsize # Print Bytes per element


# In[14]:


a.shape # returns a tuple listing the length along each dimension


# In[15]:


np.size(a), a.size # returns the entire number of elements.


# In[16]:


a.ndim  # Number of dimensions


# In[17]:


a.nbytes # Memory used


# - ** Always use `shape` or `size` for numpy arrays instead of `len` **
# - `len` gives same information only for 1d array.

# # Functions to allocate arrays

# In[18]:


x = np.zeros((2,),dtype=('i4,f4,a10'))
x


# `empty, empty_like, ones, ones_like, zeros, zeros_like, full, full_like`

# #  Setting Array Elements Values

# In[19]:


a = np.array([1,2,3,4,5])
print(a.dtype)


# In[20]:


a[0] = 10 # Change first item value
a, a.dtype


# In[21]:


a.fill(0) # slighty faster than a[:] = 0
a


# # Setting Array Elements Types

# In[22]:


b = np.array([1,2,3,4,5.0]) # Last item is a float
b, b.dtype


# In[23]:


a.fill(3.0)  # assigning a float into a int array 
a[1] = 1.5   # truncates the decimal part
print(a.dtype, a)


# In[24]:


a.astype('float64') # returns a new array containing doubles


# In[25]:


np.asfarray([1,2,3,4]) # Return an array converted to a float type


# # Slicing x[lower:upper:step]
# - Extracts a portion of a sequence by specifying a lower and upper bound.
# - The lower-bound element is included, but the upper-bound element is **not** included.
# - The default step value is 1 and can be negative.

# In[26]:


a = np.array([10,11,12,13,14])


# In[27]:


a[:2], a[-5:-3], a[0:2], a[-2:] # negative indices work


# In[28]:


a[::2], a[::-1]


# ### Exercise: 
# - Compute derivative of $f(x) = \sin(x)$ with finite difference method.
# $$
#     \frac{\partial f}{\partial x} \sim \frac{f(x+dx)-f(x)}{dx}
# $$
# 
# derivatives values are centered in-between sample points.

# In[29]:


x, dx = np.linspace(0,4*np.pi,100, retstep=True)
y = np.sin(x)


# In[30]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.rcParams['figure.figsize'] = [12.,8.] # Increase plot size
plt.plot(x, np.cos(x),'b')
plt.title(r"$\rm{Derivative\ of}\ \sin(x)$");


# In[31]:


# Compute integral of x numerically
avg_height = 0.5*(y[1:]+y[:-1])
int_sin = np.cumsum(dx*avg_height)
plt.plot(x[1:], int_sin, 'ro', x, np.cos(0)-np.cos(x));


# # Multidimensional array

# In[32]:


a = np.arange(4*3).reshape(4,3) # NumPy array
l = [[0,1,2],[3,4,5],[6,7,8],[9,10,11]] # Python List


# In[33]:


print(a)
print(l)


# In[34]:


l[-1][-1] # Access to last item


# In[35]:


print(a[-1,-1])  # Indexing syntax is different with NumPy array
print(a[0,0])    # returns the first item
print(a[1,:])    # returns the second line


# In[36]:


print(a[1]) # second line with 2d array
print(a[:,-1])  # last column


# ### Exercise 
# - We compute numerically the Laplace Equation Solution using Finite Difference Method
# - Replace the computation of the discrete form of Laplace equation with numpy arrays
# $$
# T_{i,j} = \frac{1}{4} ( T_{i+1,j} + T_{i-1,j} + T_{i,j+1} + T_{i,j-1})
# $$
# - The function numpy.allclose can help you to compute the residual.

# In[37]:


get_ipython().run_cell_magic('time', '', '# Boundary conditions\nTnorth, Tsouth, Twest, Teast = 100, 20, 50, 50\n\n# Set meshgrid\nn, l = 64, 1.0\nX, Y = np.meshgrid(np.linspace(0,l,n), np.linspace(0,l,n))\nT = np.zeros((n,n))\n\n# Set Boundary condition\nT[n-1:, :] = Tnorth\nT[:1, :]   = Tsouth\nT[:, n-1:] = Teast\nT[:, :1]   = Twest\n\nresidual = 1.0   \nistep = 0\nwhile residual > 1e-5 :\n    istep += 1\n    print ((istep, residual), end="\\r")\n    residual = 0.0   \n    for i in range(1, n-1):\n        for j in range(1, n-1):\n            T_old = T[i,j]\n            T[i, j] = 0.25 * (T[i+1,j] + T[i-1,j] + T[i,j+1] + T[i,j-1])\n            if T[i,j]>0:\n                residual=max(residual,abs((T_old-T[i,j])/T[i,j]))\n\n\nprint()\nprint("iterations = ",istep)\nplt.title("Temperature")\nplt.contourf(X, Y, T)\nplt.colorbar()')


# In[38]:


# %load solutions/numpy/laplace.py
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
plt.show()


# # Arrays to ASCII files
# 

# In[39]:


x = y = z = np.arange(0.0,5.0,1.0)


# In[40]:


np.savetxt('test.out', (x,y,z), delimiter=',')   # X is an array
get_ipython().run_line_magic('cat', 'test.out')


# In[41]:


np.savetxt('test.out', (x,y,z), fmt='%1.4e')   # use exponential notation
get_ipython().run_line_magic('cat', 'test.out')


# # Arrays from ASCII files

# In[42]:


np.loadtxt('test.out')


# - [save](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.save.html#numpy.save): Save an array to a binary file in NumPy .npy format
# - [savez](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savez.html#numpy.savez) : Save several arrays into an uncompressed .npz archive
# - [savez_compressed](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.savez_compressed.html#numpy.savez_compressed): Save several arrays into a compressed .npz archive
# - [load](https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.load.html#numpy.load): Load arrays or pickled objects from .npy, .npz or pickled files.

# ## H5py
# 
# Pythonic interface to the HDF5 binary data format. [h5py user manual](http://docs.h5py.org)

# In[43]:


import h5py as h5

with h5.File('test.h5','w') as f:
    f['x'] = x
    f['y'] = y
    f['z'] = z


# In[44]:


with h5.File('test.h5','r') as f:
    for field in f.keys():
        print(field+':',f[field].value)
       


# In[45]:


f = h5.File('test.h5','r')
f['y'].value


# # Slices Are References
# - Slices are references to memory in the original array.
# - Changing values in a slice also changes the original array.
# 

# In[46]:


a = np.arange(10)
b = a[3:6]
b  # `b` is a view of array `a` and `a` is called base of `b`


# In[47]:


b[0] = -1
a  # you change a view the base is changed.


# - Numpy does copy only if it is necessary to save memory.

# In[48]:


c = a[7:8].copy() # Explicit copy of the array slice
c[0] = -1 
a


# # Fancy Indexing

# In[49]:


a = np.random.randint(20, size=(4, 5))
a


# In[50]:


np.random.shuffle(a.flat) # shuffle modify only the first axis
a


# In[51]:


locations = a % 3 == 0 # locations can be used as a mask
a[locations] = 0 #set to 0 only the values that are divisible by 3
a


# In[52]:


a += a == 0
a


# ### `numpy.take`

# In[53]:


a = np.fromfunction(lambda i, j: (i+1)*10+j+1, (4, 5), dtype=int)
a


# In[54]:


a[1:3,2:5] # intersection line 1:2 and 2:5


# In[55]:


np.take(a,[[6,7],[10,11]])  # Use flatten array indices


# # Changing array shape

# In[56]:


grid = np.indices((3,5)) # Return an array representing the indices of a grid.
grid[0]


# In[57]:


grid[1]


# In[58]:


grid.flat[:] # Return a view 


# In[59]:


grid.flatten() # Return a copy


# In[60]:


grid.flatten


# In[61]:


np.ravel(grid, order='C') # A copy is made only if needed.


# # Sorting

# In[62]:


a=np.array([5,3,6,1,6,7,9,0,8])
np.sort(a) #. Return a view


# In[63]:


a


# In[64]:


a.sort() # Change the array inplace
a


# # Transpose-like operations

# In[65]:


a = np.array([5,3,6,1,6,7,9,0,8])
b = a
b.shape = (3,3) # b is a reference so a will be changed


# In[66]:


a


# In[67]:


c = a.T # Return a view so a is not changed
np.may_share_memory(a,c)


# In[68]:


c[0,0] = -1 # c is stored in same memory so change c you change a
a


# In[69]:


c  # is a transposed view of a


# In[70]:


b  # b is a reference to a


# In[71]:


c.base  # When the array is not a view `base` return None


# # Methods Attached to NumPy Arrays

# In[72]:


a = np.arange(20).reshape(4,5)
np.random.shuffle(a.flat)
a


# In[73]:


a = (a - a.mean())/ a.std() # Standardize the matrix
print(a)


# In[74]:


np.set_printoptions(precision=4)
print(a)


# In[75]:


a.argmax() # max position in the memory contiguous array


# In[76]:


np.unravel_index(a.argmax(),a.shape) # get position in the matrix


# # Array Operations over a given axis

# In[77]:


a = np.arange(20).reshape(5,4)
#np.random.shuffle(a.flat)
a


# In[78]:


a.sum(axis=0) # sum of each column


# In[79]:


a == 10


# In[80]:


np.apply_along_axis(sum, axis=0, arr=a)


# In[81]:


np.apply_along_axis(sorted, axis=0, arr=a)


# You can replace the `sorted` builtin fonction by a user defined function.

# In[82]:


np.empty(10)


# In[83]:


np.linspace(0,1,10)


# In[84]:


np.linspace(0,1,10,endpoint=False, retstep=True)


# In[85]:


np.arange(0,2.+0.4,0.4)


# In[86]:


np.eye(4)


# In[87]:


a = np.diag(range(4))
a


# In[88]:


a[:,:,np.newaxis]


# In[89]:


rand = np.random.RandomState(1111)
X = rand.rand(10,2)
differences = X[:, np.newaxis, :] - X[np.newaxis, :, :]
differences


# In[90]:


# square the coordinate differences
sq_differences = differences ** 2
sq_differences


# In[91]:


# sum the coordinate differences to get the squared distance
dist_sq = sq_differences.sum(-1)
dist_sq


# In[108]:


nearest = np.argsort(dist_sq, axis=1)
print(nearest)


# In[109]:


K = 2
nearest_partition = np.argpartition(dist_sq, K + 1, axis=1)
print(nearest_partition)


# In[110]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
plt.scatter(X[:, 0], X[:, 1], s=100)

# draw lines from each point to its two nearest neighbors
K = 2

for i in range(X.shape[0]):
    for j in nearest_partition[i, :K+1]:
        # plot a line from X[i] to X[j]
        # use some zip magic to make it happen:
        plt.plot(*zip(X[j], X[i]), color='black')


# ### Create the following arrays
# ```python
# [100 101 102 103 104 105 106 107 108 109]
# ```
# Hint: numpy.arange
# ```python
# [-2. -1.8 -1.6 -1.4 -1.2 -1. -0.8 -0.6 -0.4 -0.2 0. 
# 0.2 0.4 0.6 0.8 1. 1.2 1.4 1.6 1.8]
# ```
# Hint: numpy.linspace
# ```python
# [[ 0.001	0.00129155 0.0016681 0.00215443 0.00278256 
#      0.003593810.00464159 0.00599484 0.00774264 0.01]
# ```
# Hint: numpy.logspace
# ```python
# [[ 0. 0. -1. -1. -1.] 
#  [ 0. 0.  0. -1. -1.] 
#  [ 0. 0.  0.  0. -1.]
#  [ 0. 0.  0.  0.  0.]
#  [ 0. 0.  0.  0.  0.] 
#  [ 0. 0.  0.  0.  0.] 
#  [ 0. 0.  0.  0.  0.]]
# ```
# Hint: numpy.tri, numpy.zeros, numpy.transpose
# 
# ```python
# [[ 0.  1.  2.  3. 4.] 
#  [-1.  0.  1.  2. 3.] 
#  [-1. -1.  0.  1. 2.] 
#  [-1. -1. -1.  0. 1.] 
#  [-1. -1. -1. -1. 0.]]
# ```
# Hint: numpy.ones, numpy.diag
# 
# * Compute the integral numerically with Trapezoidal rule
# $$
# I = \int_{-\infty}^\infty e^{-v^2} dv
# $$
# with  $v \in [-10;10]$ and n=20.
# 
# 

# # Views and Memory Management
# - If it exists one view of a NumPy array, it can be destroyed.
# 

# In[111]:


big = np.arange(1000000)
small = big[:5]
del big
small.base


# - Array called `big` is still allocated.
# - Sometimes it is better to create a copy.

# In[112]:


big = np.arange(1000000)
small = big[:5].copy()
del big
print(small.base)


# ## Change memory alignement

# In[113]:


del(a)
a = np.arange(20).reshape(5,4)
print(a.flags)


# In[114]:


b = np.asfortranarray(a) # makes a copy
b.flags


# In[115]:


b.base is a


# You can also create a fortran array with array function.

# In[116]:


c = np.array([[1,2,3],[4,5,6]])
f = np.asfortranarray(c)


# In[117]:


print(f.ravel(order='K')) # Return a 1D array using memory order
print(c.ravel(order='K')) # Copy is made only if necessary


# # Broadcasting rules
# 
# Broadcasting rules allow you to make an outer product between two vectors: the first method involves array tiling, the second one involves broadcasting. The last method is significantly faster.
# 

# In[118]:


n = 1000
a = np.arange(n)
ac = a[:, np.newaxis]   # column matrix
ar = a[np.newaxis, :]   # row matrix


# In[119]:


get_ipython().run_line_magic('timeit', 'np.tile(a, (n,1)).T * np.tile(a, (n,1))')


# In[120]:


get_ipython().run_line_magic('timeit', 'ac * ar')


# In[121]:


np.all(np.tile(a, (n,1)).T * np.tile(a, (n,1)) == ac * ar)


# # Numpy Matrix
# 
# Specialized 2-D array that retains its 2-D nature through operations. It has certain special operators, such as $*$ (matrix multiplication) and $**$ (matrix power).

# In[122]:


m = np.matrix('1 2; 3 4') #Matlab syntax
m


# In[123]:


a = np.matrix([[1, 2],[ 3, 4]]) #Python syntax
a


# In[124]:


a = np.arange(1,4)
b = np.mat(a) # 2D view, no copy!
b, np.may_share_memory(a,b)


# In[125]:


a = np.matrix([[1, 2, 3],[ 3, 4, 5]])
a * b.T # Matrix vector product


# In[126]:


m * a # Matrix multiplication


# ## StructuredArray using a compound data type specification

# In[127]:


data = np.zeros(4, dtype={'names':('name', 'age', 'weight'),
                          'formats':('U10', 'i4', 'f8')})
print(data.dtype)


# In[128]:


data['name'] = ['Pierre', 'Paul', 'Jacques', 'Francois']
data['age'] = [45, 10, 71, 39]
data['weight'] = [95.0, 75.0, 88.0, 71.0]
print(data)


# ## RecordArray

# In[129]:


data_rec = data.view(np.recarray)
data_rec.age


# # NumPy Array Programming
# - Array operations are fast, Python loops are slow. 
# - Top priority: **avoid loops**
# - It’s better to do the work three times witharray operations than once with a loop.
# - This does require a change of habits.
# - This does require some experience.
# - NumPy’s array operations are designed to make this possible.

# # Fast Evaluation Of Array Expressions 
# 
# - The `numexpr` package supplies routines for the fast evaluation of array expressions elementwise by using a vector-based virtual machine.
# - Expressions are cached, so reuse is fast.
# 
# [Numexpr Users Guide](https://github.com/pydata/numexpr/wiki/Numexpr-Users-Guide)

# In[130]:


import numexpr as ne
import numpy as np
nrange = (2 ** np.arange(6, 24)).astype(int)

t_numpy = []
t_numexpr = []

for n in nrange:
    a = np.random.random(n)
    b = np.arange(n, dtype=np.double)
    c = np.random.random(n)
    
    c1 = ne.evaluate("a ** 2 + b ** 2 + 2 * a * b * c ", optimization='aggressive')

    t1 = get_ipython().run_line_magic('timeit', '-oq -n 10 a ** 2 + b ** 2 + 2 * a * b * c')
    t2 = get_ipython().run_line_magic('timeit', '-oq -n 10 ne.re_evaluate()')

    t_numpy.append(t1.best)
    t_numexpr.append(t2.best)

get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")
import matplotlib.pyplot as plt
import seaborn; seaborn.set()

plt.loglog(nrange, t_numpy, label='numpy')
plt.loglog(nrange, t_numexpr, label='numexpr')

plt.legend(loc='lower right')
plt.xlabel('Vectors size')
plt.ylabel('Execution Time (s)');


# # References
# - [NumPy reference](http://docs.scipy.org/doc/numpy/reference/)
# - [Getting the Best Performance out of NumPy](http://ipython-books.github.io/featured-01/)
# - [Numpy by Konrad Hinsen](http://calcul.math.cnrs.fr/Documents/Ecoles/2013/python/NumPy%20avance.pdf)
# - [Python Data Science Handbook](https://github.com/jakevdp/PythonDataScienceHandbook)
