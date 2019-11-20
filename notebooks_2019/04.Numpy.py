# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:light
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.2.4
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# %matplotlib inline
import numpy as np
from matplotlib import pyplot as plt
plt.rcParams["figure.figsize"] = (10,6)

n = 100
X = np.random.normal(size=n).reshape(n,1)
b = np.array([1.0, 2.0])
y = np.random.normal(size=n) +  b[0] + b[1] * X[:,0]

x = np.linspace(-3,3,100)
plt.scatter(X[:,0], y, c='r')
plt.plot(x, b[0]+b[1]*x, 'b')

# +
from sklearn import linear_model
from sklearn.metrics import mean_squared_error, r2_score

model = linear_model.LinearRegression()

model.fit(X, y)
print('Coefficient: \n', model.coef_)
model.intercept_
# -



X = np.insert(X, 0, 1, axis=1)
X_sq_reg_inv = np.linalg.inv(X.T @ X)
w = X_sq_reg_inv.dot(X.T).dot(y)
w

# Calculate weights by least squares  (using Moore-Penrose pseudoinverse)
U, S, V = np.linalg.svd(X.T.dot(X))
X_sq_reg_inv = V.T.dot(np.diag(1/S)).dot(U.T)
w = X_sq_reg_inv.dot(X.T).dot(y)
w

w = np.linalg.pinv(X).dot(y)
w


