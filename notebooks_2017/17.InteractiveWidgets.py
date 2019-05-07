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

# %% [markdown]
# # Jupyter Interactive widgets

# %% [markdown]
# ## interact

# %%
from ipywidgets import interact


# %%
def f(x):
    return 3 * x 


# %%
interact(f, x=(0, 100));  # IntSlider

# %%
interact(f, x=(0, 100, 10));  # IntSlider

# %%
from ipywidgets import IntSlider
interact(f, x=IntSlider(min=0, max=100, step=1, value=30));

# %%
interact(f, x=(0, 1, 0.1)); # FloatSlider

# %%
interact(f, x=True); # CheckBox

# %%
interact(f, x=' CANUM '); # Text

# %%
interact(f, x=[' CANUM ',2018]); # Dropdown


# %% [markdown]
# ## Use interact  as a decorator.

# %%
@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)


# %%
from ipywidgets import IntSlider
interact(f, x=IntSlider(min=-10, max=30, step=1, value=10));

# %% [markdown]
# ## FloatSlider

# %%
from ipywidgets import FloatSlider
slider = FloatSlider(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Input:',
)

slider

# %%
slider.value

# %% [markdown]
# ## FloatText

# %%
from ipywidgets import FloatText
from traitlets import dlink

text = FloatText(description='Value')
dlink((slider, 'value'), (text, 'value'))
text

# %% [markdown]
# ## Basic interactive plot

# %%
%matplotlib inline
import matplotlib.pyplot as plt
import numpy as np

def f(tau):
    plt.figure(2)
    t = np.linspace(0, 1, num=1000)
    plt.plot(t, 1 - np.exp(-t/tau), t, np.exp(-t/tau))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
  


# %%
from ipywidgets import interactive
interactive_plot = interactive(f, tau=(0.01, 0.2, 0.01))
interactive_plot

# %% [markdown]
# ## interactive_manual

# %%
from ipywidgets import interact_manual

def plot_gaussian(d):
    
    x, y = np.meshgrid(np.linspace(-1,1,100),np.linspace(-1,1,100))
    fig, ax = plt.subplots(1, 1)
    ax.contourf(x,y, np.exp(-(x*x+y*y)/ d))
    ax.axis('equal')
    fig.tight_layout()

    

interact_manual(plot_gaussian,d=FloatSlider(min=1e-4, max=1, step=1e-4));

# %% [markdown]
# ## widgets

# %%
import ipywidgets as widgets
from IPython.display import display

# %%
w = widgets.IntSlider()
display(w)

# %%
display(w)

# %%
w.close()

# %% [markdown]
# # Linking two similar widgets

# %%
a = widgets.FloatText()
b = widgets.FloatSlider()
display(a, b)
mylink = widgets.jslink((a, 'value'), (b, 'value'))
