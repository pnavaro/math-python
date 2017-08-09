from distutils.core import setup
from distutils.extension import Extension
from Cython.Distutils import build_ext
import numpy

ext_modules = [Extension("dgemm",
                         ['dgemm.pyx'],
                         include_dirs=[numpy.get_include()]
                         )
               ]

setup(
    name='my_dgemm',
    author='Pierre Navaro',
    author_email='pierre.navaro@univ-rennes1.fr',
    cmdclass={'build_ext': build_ext},
    ext_modules=ext_modules, requires=['numpy', 'cython']
)

# To build Python interface for dgemm C function, run:
# python setup.py build_ext --inplace
