#!/usr/bin/env python
# coding: utf-8

# # Julia Set
# 
# Modified version from [Loic Gouarin](https://github.com/gouarin/GTSage2014/)
# 
# [Julia set on wikipedia](https://en.wikipedia.org/wiki/Julia_set)

# In[1]:


get_ipython().run_line_magic('matplotlib', 'inline')
get_ipython().run_line_magic('config', "InlineBackend.figure_format = 'retina'")


# In[2]:


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm

plt.rcParams['figure.figsize'] = (6,6)


# In[3]:


nx, ny = 512, 512 # mesh
lim, maxit = 400, 2000 # limits 
vmin, vmax = 0, 200 

x = np.linspace(-1.6, 1.6, nx)
y = np.linspace(-1.6, 1.6, ny)
c = -0.772691322542185 + 0.124281466072787j


# # Pure Python

# In[4]:


def juliaset_python(x, y, c, lim, maxit):
    """ 
    returns Julia set
    """
    julia = np.zeros((x.size, y.size))

    for i in range(x.size):
        for j in range(y.size):
            z = x[i] + 1j*y[j]
            ite = 0
            while abs(z) < lim and ite < maxit:
                z = z**2 + c
                ite += 1
            julia[j, i] = ite

    return julia


# In[5]:


def plot_julia_set(julia):
    plt.figure(figsize=(6,6))
    plt.imshow(julia, cmap = cm.Greys, vmin=vmin, vmax=vmax)


# In[6]:


plot_julia_set(juliaset_python(x, y, c, lim, maxit))


# # Fortran

# In[7]:


get_ipython().run_line_magic('load_ext', 'fortranmagic')


# In[8]:


get_ipython().run_cell_magic('fortran', '--f90flags "-O3 -fopenmp" --extra "-L/usr/local/lib -lgomp"', 'subroutine juliaset_fortran(x, y, c, lim, maxit, julia)\n\n    real(8),    intent(in)  :: x(:)\n    real(8),    intent(in)  :: y(:)\n    complex(8), intent(in)  :: c\n    real(8),    intent(in)  :: lim\n    integer,    intent(in)  :: maxit\n    integer,    intent(out) :: julia(size(x),size(y))\n\n    real(8)    :: zr, zi, limsq, cr, ci, tmp\n    complex(8) :: z\n    integer    :: ite, nx, ny\n\n    nx = size(x)\n    ny = size(y)\n    limsq = lim * lim\n    cr = real(c)\n    ci = imag(c)\n\n    !$OMP PARALLEL DEFAULT(NONE) &\n    !$OMP FIRSTPRIVATE(nx,ny,x,y,c,limsq,maxit,cr,ci) &\n    !$OMP PRIVATE(i,j,ite,zr,zi, tmp) &\n    !$OMP SHARED(julia)\n    !$OMP DO SCHEDULE(DYNAMIC)\n    do i = 1, nx\n       do j = 1, ny   \n            zr = x(i)\n            zi = y(j)\n            ite = 0\n            do while (zr*zr+zi*zi < limsq .and. ite < maxit)\n                tmp = zr*zr - zi*zi \n                zi = 2*zr*zi + ci\n                zr = tmp + cr\n                ite = ite + 1\n            end do\n            julia(j, i) = ite\n        end do\n    end do\n    \n    !$OMP END PARALLEL\n\n\nend subroutine juliaset_fortran')


# In[9]:


plot_julia_set(juliaset_fortran(x, y, c, lim, maxit))


# # Numpy

# In[10]:


import itertools

def juliaset_numpy(x, y, c, lim, maxit):
    julia = np.zeros((x.size, y.size), dtype=np.int32)

    zx = x[np.newaxis, :]
    zy = y[:, np.newaxis]
    
    z = zx + zy*1j
    
    for ite in itertools.count():
        
        z = z**2 + c 
        mask = np.logical_not(julia) & (np.abs(z) >= lim)
        julia[mask] = ite
        if np.all(julia) or ite > maxit:
            return julia
            

    


# In[11]:


plot_julia_set(juliaset_numpy(x, y, c, lim, maxit))


# # Cython

# In[12]:


import os, sys

if sys.platform == 'darwin':
    os.environ['CC'] = 'gcc-8'
    os.environ['CXX'] = 'g++-8'
else:
    os.environ['CC'] = 'gcc'
    os.environ['CXX'] = 'g++'


# In[13]:


get_ipython().run_line_magic('load_ext', 'cython')


# In[14]:


get_ipython().run_cell_magic('cython', '', 'import numpy as np\nimport cython\n\n@cython.boundscheck(False)\n@cython.wraparound(False)\ndef juliaset_cython(double [:] x, double [:] y, double complex c, double lim, int maxit):\n    cdef:\n        int [:, ::1] julia = np.zeros((x.size, y.size), dtype = np.int32)\n        double tmp, zr, zi, lim2 = lim*lim\n        double cr = c.real, ci = c.imag\n        int ite, i, j, nx=x.size, ny=y.size\n\n    for i in range(nx):\n        for j in range(ny):\n            zr = x[i] \n            zi = y[j]\n            ite = 0\n            while (zr*zr + zi*zi) < lim2 and ite < maxit:\n                zr, zi = zr*zr - zi*zi + cr, 2*zr*zi + ci\n                ite += 1\n            julia[j, i] = ite\n\n    return julia')


# In[15]:


plot_julia_set(juliaset_cython(x, y, c, lim, maxit))


# In[16]:


get_ipython().run_cell_magic('cython', '--v -f -c-fopenmp --link-args=-fopenmp', "import numpy as np\nimport cython\nfrom cython.parallel import prange\nfrom libc.stdlib cimport malloc, free \n\n@cython.boundscheck(False)\n@cython.wraparound(False)\ndef juliaset_cython_omp(double [:] x, double [:] y, double complex c, double lim, int maxit):\n    cdef:\n        int [:, ::1] julia = np.zeros((x.size, y.size), dtype = np.int32)\n        double tmp, zr, zi, lim2 = lim*lim\n        double cr = c.real, ci = c.imag\n        int  i, j, nx=x.size, ny=y.size\n        int *ite\n\n    for j in prange(ny, nogil=True, schedule='dynamic'):\n        ite = <int *> malloc(sizeof(int))\n        for i in range(nx):\n            zr = x[i] \n            zi = y[j]\n            ite[0] = 0\n            while (zr*zr + zi*zi) < lim2 and ite[0] < maxit:\n                zr, zi = zr*zr - zi*zi + cr, 2*zr*zi + ci\n                ite[0] += 1\n            julia[j, i] = ite[0]\n        free(ite)\n        \n    return julia")


# In[17]:


plot_julia_set(juliaset_cython_omp(x, y, c, lim, maxit))


# # numba

# In[18]:


from numba import autojit

@autojit
def juliaset_numba(x, y, c, lim, maxit):
    julia = np.zeros((x.size, y.size))
    lim2 = lim*lim
    
    c = complex(c)  # needed for numba
    for j in range(y.size):
        for i in range(x.size):

            z = complex(x[i], y[j])
            ite = 0
            while (z.real*z.real + z.imag*z.imag) < lim2 and ite < maxit:
                z = z*z + c
                ite += 1
            julia[j, i] = ite

    return julia


# In[19]:


plot_julia_set(juliaset_numba(x, y, c, lim, maxit))


# In[20]:


get_ipython().run_line_magic('reload_ext', 'pythran.magic')


# In[21]:


get_ipython().run_cell_magic('pythran', '-fopenmp', '\nimport numpy as np\n\n#pythran export juliaset_pythran(float64[], float64[],complex, int, int)\ndef juliaset_pythran(x, y, c, lim, maxit):\n    """ \n    returns Julia set\n    """\n    julia = np.zeros((x.size, y.size), dtype=np.int32)\n\n    #omp parallel for private(z)\n    for j in range(y.size):\n        for i in range(x.size):\n            z = x[i] + 1j*y[j]\n            ite = 0\n            while abs(z) < lim and ite < maxit:\n                z = z**2 + c\n                ite += 1\n            julia[j, i] = ite\n\n    return julia')


# In[ ]:


plot_julia_set(juliaset_pythran(x, y, c, lim, maxit))


# In[ ]:


import pandas as pd
from collections import defaultdict
results = defaultdict(list)

functions = [juliaset_python,
             juliaset_fortran,
             juliaset_numpy,
             juliaset_cython,
             juliaset_cython_omp,
             juliaset_numba,
             juliaset_pythran]

for f in functions:

    _ = get_ipython().run_line_magic('timeit', '-oq -n 1 f(x, y, c, lim, maxit)')
    results['etime'] += [_.best]


# In[ ]:


results = pd.DataFrame(results, index=list(map(lambda f:f.__name__[9:],functions)))


# In[ ]:


results["speed_up"] = [results.etime[0]/t for t in results.etime]


# In[ ]:


results.sort_values(by="speed_up",axis=0)

