# -*- coding: utf-8 -*-
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
#     display_name: Python 3.7
#     language: python
#     name: python3
# ---

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Getting Started with NumPy
#
# - It is handy to import everything from NumPy into a Python console:
# ```python
# from numpy import *
# ```
# - But it is easier to read and debug if you use explicit imports.
# ```python
# import numpy as np
# ```

# %%
import numpy as np
print(np.__version__)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Numpy Arrays
#
# It was initially developed by [Travis Oliphant](https://www.continuum.io/people/travis-oliphant).
#
# - There are important differences between NumPy arrays and Python lists:
#     - NumPy arrays have a fixed size at creation.
#     - NumPy arrays elements are all required to be of the same data type.
#     - NumPy arrays operations are performed in compiled code for performance.
# - Most of today's scientific/mathematical Python-based software use NumPy arrays.
# - NumPy gives us the code simplicity of Python, but the operation is speedily executed by pre-compiled C code.

# %% {"slideshow": {"slide_type": "slide"}}
import random, operator
L1 = [random.random() for i in range(10000)]
L2 = [random.random() for i in range(10000)]

%timeit res = [l1+l2 for l1,l2 in zip(L1,L2) ]


# %% {"slideshow": {"slide_type": "slide"}}
%timeit res = list(map(operator.add, L1, L2))

# %%
A1 = np.array(L1)
A2 = np.array(L2)
%timeit A1 + A2

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Sub-arrays

# %% [markdown] {"slideshow": {"slide_type": "fragment"}}
# The numpy array slicing `x[lower:upper:step]` extracts a portion of a sequence by specifying a lower and upper bound. be aware that the lower-bound element is included, but the upper-bound element is **not** included. The default step value is 1 and can be negative.

# %% {"slideshow": {"slide_type": "fragment"}}
a = np.array([10,11,12,13,14])
a[:2], a[-5:-3], a[0:2], a[-2:] # negative indices work

# %% {"slideshow": {"slide_type": "fragment"}}
a[::2], a[::-1]

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Finite differences
#
# We want to compute derivative of $f(x) = \sin(x)$ with finite difference method.
# $$
#     \frac{\partial f}{\partial x} \sim \frac{f(x+dx)-f(x)}{dx}
# $$
#
# derivatives values are centered in-between sample points.
#
# Numpy provides the linspace function that returns an array of values equally spaced. You can also use the $sin$ function applied to all elements of $x$. Element wise operations are the “default mode”.

# %%
%matplotlib inline
import matplotlib.pyplot as plt

# %%
%config InlineBackend.figure_format = "retina" # HD screen
plt.rcParams["figure.figsize"] = (9, 4) # figure size on jupyter

# %%
x, dx = np.linspace(0, 4*np.pi, 100, endpoint=False, retstep=True)
f = np.sin(x)
df = (f[1:]-f[:-1])/ dx
xc = 0.5*(x[:-1]+x[1:])
plt.plot(x, np.cos(x), 'r', xc, df, 'bo' );

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# Compute derivative using the second order formula:
#
# $$
#     \frac{\partial f_i}{\partial x} \sim \frac{f_{i+1}-f_{i-1}}{2dx}
# $$
#
# Plot the result.
#

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Numpy `diff` and `gradient`

# %% {"slideshow": {"slide_type": "fragment"}}
f = np.sin(x)
df = np.gradient(f)/dx
df.size

# %%
df = (np.diff(f[1:], n=1)+np.diff(f[:-1], n=1))/(2*dx)
df.size

# %% {"slideshow": {"slide_type": "fragment"}}
plt.plot(x[1:-1], np.cos(x[1:-1]), 'r', x[1:-1], df, 'bo' );

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Fast Fourier Transform
#
# $$
# y'(x) = \sum_{k=-\infty}^{+\infty} (\frac{2\pi}{L} k Y_k ) e^{2\pi/L kx}
# $$

# %% {"slideshow": {"slide_type": "slide"}}
n, L = 64, 4*np.pi
x = np.linspace(0,L,n, endpoint=False)
k = 2*np.pi/L*np.concatenate((np.arange(n//2),np.arange(-n//2,0)))
f = np.sin(x)
df = np.real(np.fft.ifft(1j * kx * np.fft.fft(f)))
plt.plot(x, np.cos(x), 'r', x, df, 'bo' );

# %% [markdown]
# ## Gray-Scott model
#
# The reaction-diffusion system described here involves two generic chemical species U and V, whose concentration at a given point in space is referred to by variables u and v. As the term implies, they react with each other, and they diffuse through the medium. Therefore the concentration of U and V at any given location changes with time and can differ from that at other locations.
#
# The overall behavior of the system is described by the following formula, two equations which describe three sources of increase and decrease for each of the two chemicals:
#
#
# $$
# \begin{array}{l}
# \displaystyle \frac{\partial u}{\partial t} = D_u \Delta u - uv^2 + F(1-u) \\
# \displaystyle \frac{\partial v}{\partial t} = D_v \Delta v + uv^2 - (F+k)v
# \end{array}
# $$
#
# $D_u, D_v, F$ and $k$ are constant.
#
# The classic Euler scheme is used to integrate the time derivative.
#
# [Reaction-Diffusion by the Gray-Scott Model: Pearson's Parametrization](https://mrob.com/pub/comp/xmorphia/)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ## Initialization
#
# $u = 1$ everywhere et $v = 0$ in the domain except in a square zone where $v = 0.25$ and $ u = 0.5$. This square located in the center of the domain is  $[0, 1]\times[0,1]$ with a size of $0.2$.
#
# Parameters:

# %% {"slideshow": {"slide_type": "fragment"}}
Du, Dv = .1, .05
F, k = 0.0545, 0.062

# %% {"slideshow": {"slide_type": "slide"}}
plt.rcParams['figure.figsize'] = (10,6)  # increase figure size in jupyter

# %% {"slideshow": {"slide_type": "fragment"}}
ext_domain = plt.Rectangle((0,0), 1, 1, ec="k", fc="b")
int_domain = plt.Rectangle((0.4,0.4), 0.2, 0.2, fc="r", ec="k")
ax = plt.gca()  # current figure, create one if it doesn't exist
ax.add_patch(ext_domain)
ax.add_patch(int_domain)
plt.axis('scaled')

# %% [markdown]
# To represent values of $u$ and $v$ on the mesh we will use numpy arrays. Numpy provides `ndarray` multi-dimensional array object
# and derived objects such as masked arrays and matrices. It provides also a set of functions for fast array mathematical operations.
#
#

# %% [markdown]
# ## Multidimensional array

# %%
np.arange(4*5).reshape(4,5)

# %%
np.zeros((4,5))

# %%
np.full((4,5),3)

# %%
np.arange(1,5) * np.arange(1,6)[:,np.newaxis]

# %%
np.fromfunction(lambda i,j: i+j,(4,5))


# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# # Laplacian
#
# The laplacian is computed with the following numerical scheme
#
# $$
# \Delta u_{i,j} \approx u_{i,j-1} + u_{i-1,j} -4u_{i,j} + u_{i+1, j} + u_{i, j+1}
# $$

# %%
def laplacian_python(u):
    
    delta_u = u.copy()
    for i in range(1,nx-1):
        for j in range(1,ny-1):
            delta_u[i][j] = u[i][j-1]+u[i-1][j] \
                             -4*u[i][j]+u[i+1][j]+u[i][j+1]
    
    return delta_u


# %%
%timeit laplacian_python(u)

# %%
x = np.linspace(-np.pi,np.pi,100)
y = np.linspace(-np.pi,np.pi,100)
xx, yy = np.meshgrid(x, y, sparse=True)
z = np.exp(-(xx)*(xx))*np.exp(-(yy)*(yy))

# %%
plt.contourf(x,y,z)

# %% [markdown] {"slideshow": {"slide_type": "slide"}}
# ### Exercise
#
# Rewrite the laplacian function using Numy arrays operations
#
# ```py
# def laplacian(u):
#     delta_u = np.copy(u)
#     ###
#     return delta_u
# ```

# %% [markdown]
# # Slices Are References
# - Slices are references to memory in the original array.
# - Changing values in a slice also changes the original array.
#
#

# %%
a = np.arange(10)
b = a[3:6]
b  # `b` is a view of array `a` and `a` is called base of `b`

# %%
b[0] = -1
a  # you change a view the base is changed.

# %%
c = a[7:8].copy() # Explicit copy of the array slice
c[0] = -1 
a

# %% [markdown]
# # Fancy Indexing

# %%
a = np.random.randint(20, size=(4, 5))
a

# %%
locations = a % 3 == 0 # locations can be used as a mask
a[locations] = 0 #set to 0 only the values that are divisible by 3
a

# %%
a += a == 0
a

# %% [markdown]
# ### Exercise 
#
# Write the initialization of the Grayscott model using fancy indexing
#
# ```py
#
# def init(n):
#    u = np.zeros((n,n),dtype=np.float64)
#    ###
#    return u
# ```

# %%
nx, ny = 100, 100
dx, dy = 1./nx, 1./ny

u, v = [], []
for i in range(nx):
    u.append([0 for j in range(ny)])
    
for i in range(nx):
    for j in range(ny):
        if 400 < i < 600 and 400 < j < 600:
            u[i][j] = 0.5

# %% [markdown]
# # Array Operations over a given axis

# %%
a = np.arange(20).reshape(5,4)
a

# %%
a.sum(axis=0) # sum of each column

# %%
a.mean(axis=1) # mean of each line

# %% [markdown]
# # Broadcasting rules
#
# Broadcasting rules allow you to make an outer product between two vectors: the first method involves array tiling, the second one involves broadcasting. The last method is significantly faster.
#
#

# %%
n = 1000
a = np.arange(n)
ac = a[:, np.newaxis]   # column matrix
ar = a[np.newaxis, :]   # row matrix

# %%
%timeit np.tile(a, (n,1)).T * np.tile(a, (n,1))

# %%
%timeit ac * ar

# %%
np.all(np.tile(a, (n,1)).T * np.tile(a, (n,1)) == ac * ar)


# %% [markdown]
# ## Periodic domain

# %%
def periodic_bc(u):
    u[0, :] = u[-2, :]
    u[-1, :] = u[1, :]
    u[:, 0] = u[:, -2]
    u[:, -1] = u[:, 1]


# %%
def grayscott(U, V, Du, Dv, F, k):
    
    u, v = U[1:-1,1:-1], V[1:-1,1:-1]

    Lu = laplacian(U)
    Lv = laplacian(V)

    uvv = u*v*v
    u += Du*Lu - uvv + F*(1 - u)
    v += Dv*Lv + uvv - (F + k)*v

    periodic_bc(U)
    periodic_bc(V)


# %%
%%time
from tqdm import tqdm_notebook as tqdm
from PIL import Image
U, V = init(300)

def create_image():
    global U, V
    for t in range(40):
        grayscott(U, V, Du, Dv, F, k)
    V_scaled = np.uint8(255*(V-V.min()) / (V.max()-V.min()))
    return V_scaled

def create_frames(n):

    return [create_image() for i in tqdm(range(n))]
    
frames = create_frames(500)

# %%
import imageio
frames_scaled = [np.uint8(255 * frame) for frame in frames]
imageio.mimsave('movie.gif', frames_scaled, format='gif', fps=60)

# %% [markdown]
# ![grayscott](movie.gif "grayscott")

# %% [markdown]
# # Numpy Matrix
#
# Specialized 2-D array that retains its 2-D nature through operations. It has certain special operators, such as $*$ (matrix multiplication) and $**$ (matrix power).

# %%
m = np.matrix('1 2; 3 4') #Matlab syntax
m

# %%
a = np.matrix([[1, 2],[ 3, 4]]) #Python syntax
a

# %%
a = np.arange(1,4)
b = np.mat(a) # 2D view, no copy!
b, np.may_share_memory(a,b)

# %%
a = np.matrix([[1, 2, 3],[ 3, 4, 5]])
a * b.T # Matrix vector product

# %%
m * a # Matrix multiplication

# %%
a = np.random.randint(20, size=(4, 4))
b = np.arange(4)

np.linalg.solve(a,b)
