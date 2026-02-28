'''
Package for simple learning
and exploration of clustering
methods of machine learning.
Submodules:
database : has built-in datasets, functions for selecting them,
userdialogue : tools for communication with the user, 
utils : helper functions that operate on datasets.
'''
from . import utils, userdialogue, database
__all__ = ["utils", "userdialogue", 'database']