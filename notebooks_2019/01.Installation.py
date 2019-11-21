# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     comment_magics: false
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

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Installation (my advices)

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# - Windows: Install [Anaconda](https://www.anaconda.com/downloads) (large) or [Miniconda](https://conda.io/miniconda.html) (small)
# ```
# conda install jupyter jupytext -c conda-forge
# ```
# - Macosx: Install Python with [Homebrew](https://brew.sh) and package with `pip3`
# ```
# brew install python
# pip3 install jupyter jupytext
# ```
# - Linux: Use packaging system and install missing ones with pip with `--user` flag
# ```
# apt-get install python3-numpy
# python3 -m pip install --user jupyter jupytext
# ```

# + {"slideshow": {"slide_type": "fragment"}, "cell_type": "markdown"}
# ### Get the notebooks

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# - with git
# ```
# git clone https://github.com/pnavaro/math-python.git
# ```
# - Or download the zip archive: https://github.com/pnavaro/math-python/archive/master.zip

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# # Jupyter Notebook
#
#
# To open the notebook
# ```
# jupyter notebook
# ```
# You should see the notebook open in your browser. If not, go to http://localhost:8888/tree
#
# The Jupyter Notebook is an interactive environment for writing and running code. 
# The notebook is capable of running code in [a wide range of languages](https://github.com/jupyter/jupyter/wiki/Jupyter-kernels). 
# However, each notebook is associated with Python3 kernel.

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Code cells allow you to enter and run code
#
# **Make a copy of this notebook by using the File menu.**
#
# Run a code cell using `Shift-Enter` or pressing the <button class='btn btn-default btn-xs'><i class="icon-step-forward fa fa-step-forward"></i></button> button in the toolbar above:
#
# There are two other keyboard shortcuts for running code:
#
# * `Alt-Enter` runs the current cell and inserts a new one below.
# * `Ctrl-Enter` run the current cell and enters command mode.

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Managing the Kernel
#
# Code is run in a separate process called the Kernel.  The Kernel can be interrupted or restarted.  Try running the following cell and then hit the <button class='btn btn-default btn-xs'><i class='icon-stop fa fa-stop'></i></button> button in the toolbar above.
#
# The "Cell" menu has a number of menu items for running code in different ways. These includes:
#
# * Run and Select Below
# * Run and Insert Below
# * Run All
# * Run All Above
# * Run All Below

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Restarting the kernels
#
# The kernel maintains the state of a notebook's computations. You can reset this state by restarting the kernel. This is done by clicking on the <button class='btn btn-default btn-xs'><i class='fa fa-repeat icon-repeat'></i></button> in the toolbar above.
#
#
# Check the [documentation](https://jupyter-notebook.readthedocs.io/en/latest/examples/Notebook/Notebook%20Basics.html).

# + {"slideshow": {"slide_type": "slide"}, "cell_type": "markdown"}
# ## Installing Python Packages from a Jupyter Notebook
#
# ### conda package in the current Jupyter kernel
#
# Example with package `lorem` from *conda-forge*
# ```
# %conda install lorem
# ```
#
# ### pip package in the current Jupyter kernel
# ```
# %pip install lorem
# ```

# + {"slideshow": {"slide_type": "fragment"}}
import sys
print(sys.executable)
# -

