# -*- coding: utf-8 -*-
# # Locally weighted regression
#
# https://en.wikipedia.org/wiki/Local_regression

# %matplotlib inline
import matplotlib.pyplot as plt
import numpy as np
from scipy import linalg

# ## Initialize noisy data
#
# - Create a numpy array `x` of equally spaced values in [0,3$\pi$] with the function `np.linspace`
# - Create a numpy array `noise` (same size as `x`) with the function `np.random.normal` with standard deviation is equal to 0.25
# - Create the numpy array `y = sin(x) + noise`
# - Plot the the function `y = sin(x)` and the scatter plot 

print(np.linspace.__doc__)

print(np.random.normal.__doc__)


# To compute a locally weighted linear regression of this dataset ($x$,$y$)
# we will do the following:
#
# Fit $\theta$ to minimize $ \sum_i^m w_i (y_i - \theta^T x_i)^2 $
#
# Weights are computed with the function (bell shape kernel):
#
# $$
# w_i = exp(\frac{(x_i−x)^2}{2\tau^2})
# $$
#
#

# $$
# \begin{aligned}
# \begin{bmatrix} \sum w_i & \sum w_i x_i \\ 
#                 \sum w_i x_i & \sum w_i x_i x_i
# \end{bmatrix}
# \begin{bmatrix} 
# \theta_0 \\ 
# \theta_1 
# \end{bmatrix}   = \begin{bmatrix}  
# \sum w_i y_i \\  
# \sum w_i y_i x_i \end{bmatrix}  
#     \\
#     & \mathbf{A} \Theta = \mathbf{b}
#     \\
#     &  \Theta = \mathbf{A}^{-1} \mathbf{b}
# \end{aligned}
# $$
#
# - Write the code to compute the numpy array `w`
# - Build this system using `numpy.sum` function
# - Solve the system with `scipy.linalg.solve`
# - compute the fitted $y_{predict} = \theta_0 + \theta_1 x$ values with $\tau = 0.1$
# - plot the fitted curve and try to change $\tau$

def lowess_bell_shape_kern(x, y, tau = .005):
    """lowess_bell_shape_kern(x, y, tau = .005) -> yest
    Locally weighted regression: fits a nonparametric regression curve to a scatterplot.
    The arrays x and y contain an equal number of elements; each pair
    (x[i], y[i]) defines a data point in the scatterplot. The function returns
    the estimated (smooth) values of y.
    The kernel function is the bell shaped function with parameter tau. Larger tau will result in a
    smoother curve. 
    """
    m = len(x)
    yest = np.zeros(m)

    #Initializing all weights from the bell shape kernel function    
    w = np.array([np.exp(- (x - x[i])**2/(2*tau)) for i in range(m)])     
    
    #Looping through all x-points
    for i in range(m):
        weights = w[:, i]
        b = np.array([np.sum(weights * y), np.sum(weights * y * x)])
        A = np.array([[np.sum(weights), np.sum(weights * x)],
                    [np.sum(weights * x), np.sum(weights * x * x)]])
        theta = linalg.solve(A, b)
        yest[i] = theta[0] + theta[1] * x[i] 

    return yest


# +
#Initializing noisy non linear data
x = np.linspace(0,1,100)
noise = np.random.normal(loc = 0, scale = .25, size = 100)
y = np.sin(x * 3 * np.pi ) 
y_noise = y + noise

f = 0.25
yest_bell = lowess_bell_shape_kern(x,y)

#Plotting the noisy data and the kernell at around x = 0.2
plt.figure(figsize=(10,6))
plt.plot(x,y,color = 'darkblue', label = 'sin()')
plt.scatter(x,y_noise, facecolors = 'none', edgecolor = 'darkblue', label = 'sin() + noise')
plt.plot(x,yest_bell,color = 'red', label = 'Loess: bell shape kernel')
plt.legend()
plt.title('Sine with noise: Loess regression and bell shaped kernel')
plt.show()


# -


