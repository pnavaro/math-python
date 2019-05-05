#!/usr/bin/env python
# coding: utf-8

# # Jupyter Interactive widgets

# ## interact

# In[1]:


from ipywidgets import interact


# In[2]:


def f(x):
    return 3 * x 


# In[3]:


interact(f, x=(0, 100));  # IntSlider


# In[4]:


interact(f, x=(0, 100, 10));  # IntSlider


# In[5]:


from ipywidgets import IntSlider
interact(f, x=IntSlider(min=0, max=100, step=1, value=30));


# In[6]:


interact(f, x=(0, 1, 0.1)); # FloatSlider


# In[7]:


interact(f, x=True); # CheckBox


# In[8]:


interact(f, x=' CANUM '); # Text


# In[9]:


interact(f, x=[' CANUM ',2018]); # Dropdown


# ## Use interact  as a decorator.

# In[10]:


@interact(x=True, y=1.0)
def g(x, y):
    return (x, y)


# In[11]:


from ipywidgets import IntSlider
interact(f, x=IntSlider(min=-10, max=30, step=1, value=10));


# ## FloatSlider

# In[12]:


from ipywidgets import FloatSlider
slider = FloatSlider(
    value=7.5,
    min=5.0,
    max=10.0,
    step=0.1,
    description='Input:',
)

slider


# In[13]:


slider.value


# ## FloatText

# In[14]:


from ipywidgets import FloatText
from traitlets import dlink

text = FloatText(description='Value')
dlink((slider, 'value'), (text, 'value'))
text


# ## Basic interactive plot

# In[15]:


get_ipython().run_line_magic('matplotlib', 'inline')
import matplotlib.pyplot as plt
import numpy as np

def f(tau):
    plt.figure(2)
    t = np.linspace(0, 1, num=1000)
    plt.plot(t, 1 - np.exp(-t/tau), t, np.exp(-t/tau))
    plt.xlim(0, 1)
    plt.ylim(0, 1)
  


# In[16]:


from ipywidgets import interactive
interactive_plot = interactive(f, tau=(0.01, 0.2, 0.01))
interactive_plot


# ## interactive_manual

# In[17]:


from ipywidgets import interact_manual

def plot_gaussian(d):
    
    x, y = np.meshgrid(np.linspace(-1,1,100),np.linspace(-1,1,100))
    fig, ax = plt.subplots(1, 1)
    ax.contourf(x,y, np.exp(-(x*x+y*y)/ d))
    ax.axis('equal')
    fig.tight_layout()

    

interact_manual(plot_gaussian,d=FloatSlider(min=1e-4, max=1, step=1e-4));


# ## widgets

# In[18]:


import ipywidgets as widgets
from IPython.display import display


# In[19]:


w = widgets.IntSlider()
display(w)


# In[20]:


display(w)


# In[21]:


w.close()


# # Linking two similar widgets

# In[22]:


a = widgets.FloatText()
b = widgets.FloatSlider()
display(a, b)
mylink = widgets.jslink((a, 'value'), (b, 'value'))

