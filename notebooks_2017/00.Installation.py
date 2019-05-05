#!/usr/bin/env python
# coding: utf-8

# # Installation

# ### 1. Install [Anaconda](https://www.anaconda.com/downloads) (large) or [Miniconda](https://conda.io/miniconda.html) (small)

# ### 2. Open a terminal (Linux/MacOSX) or a conda prompt (Windows)

# ### 3. Configure git
# ```
# conda install git # install with conda if not present
# git config --global user.name “Prenom Nom"
# git config --global user.email “prenom.nom@domain.fr"
# git clone https://github.com/pnavaro/math-python.git
# ```

# ### 4. Create the conda environment
# 
# ```
# cd math-python
# conda env create -f binder/environment.yml
# ```

# ### 5. Activate the new environment
# 
# Activating the conda environment will change your shell’s prompt to show what virtual environment you’re using, and modify the environment so that running python will get you that particular version and installation of Python. 
# <pre>
# $ source activate math-python   (activate math-python on Windows)
# (math-python) $ python
# Python 3.6.2 (default, Jul 17 2017, 16:44:45) 
# [GCC 4.2.1 Compatible Apple LLVM 8.1.0 (clang-802.0.42)] on darwin
# Type "help", "copyright", "credits" or "license" for more information.
# >>> quit()
# </pre>
# 
# [Conda envs documentation](https://conda.io/docs/using/envs.html).

# ### Managing packages with conda
# 
# * Use conda-forge channel
# ```sh
# conda config --add channels conda-forge
# ```
# 
# * List all packages
# ```sh
# conda list
# ```
# 
# * Search a package
# ```sh
# conda search jupyter
# ```
# 
# You can also update or remove, check the [documentation](https://conda.io/docs/using/pkgs.html).

# ### Install jupyter with extensions
# 
# ```
# conda install jupyter_contrib_nbextensions
# conda install autopep8
# ```

# ### Enable autopep8 extension
# 
# ```
# jupyter nbextension enable code_prettify/autopep8
# ```

# ### Install the jupyter kernel
# 
# ```
# python -m ipykernel install --user --name math-python --display-name "Python (math-python)"
# ```
# 
# ### Run the jupyter notebook
# 
# ```
# jupyter notebook
# ```

# ## Installing Python Packages from a Jupyter Notebook
# 
# ### conda package in the current Jupyter kernel
# 
# Example with package `lorem` from *conda-forge*
# ```python
# import sys
# !conda install --yes --prefix {sys.prefix} -c conda-forge lorem
# ```
# 
# ### pip package in the current Jupyter kernel
# ```
# import sys
# !{sys.executable} -m pip install lorem
# ```

# In[2]:


import sys
print(sys.executable)

