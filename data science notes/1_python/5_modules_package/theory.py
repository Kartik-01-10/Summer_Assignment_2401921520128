# MODULES, PACKAGING, AND IMPORT IN PYTHON

# 1. MODULES
# A module is simply a Python file that contains functions, classes, or variables.
# You can reuse code from a module by importing it into another Python file.

# Example:
# Suppose you have a file named math_utils.py with the following content:
# def add(a, b):
#     return a + b

# You can use this function in another file by importing the module:
# import math_utils
# result = math_utils.add(2, 3)

# 2. IMPORTING MODULES
# Python provides several ways to import modules:

# a. import module_name
#    Imports the entire module. You access functions using module_name.function_name

# b. from module_name import function_name
#    Imports only specific functions or classes. You can use them directly without prefix.

# c. from module_name import *
#    Imports everything from the module. Not recommended because it can cause naming conflicts.

# d. import module_name as alias
#    Imports the module with a short alias name. Useful for long module names.

# Example:
# import numpy as np
# np.array([1, 2, 3])

# 3. BUILT-IN MODULES
# Python comes with many built-in modules like math, os, sys, datetime, logging, etc.
# You can use them without installing anything.

# Example:
# import math
# print(math.sqrt(16))  # Output: 4.0

# 4. THIRD-PARTY MODULES
# These are external libraries that you can install using pip.
# Example: numpy, pandas, requests

# To install a third-party module:
# pip install module_name

# 5. CUSTOM MODULES
# You can create your own module by writing Python code in a .py file.
# Then import it into other files as needed.

# 6. PACKAGES
# A package is a collection of modules organized in folders.
# A folder becomes a package when it contains a special file named __init__.py
# This file can be empty or contain initialization code.

# Example folder structure:
# my_package/
# ├── __init__.py
# ├── module1.py
# └── module2.py

# You can import modules from a package like this:
# from my_package import module1
# from my_package.module2 import function_name

# 7. RELATIVE IMPORTS (used inside packages)
# You can import modules relative to the current file location using dots.

# Example:
# from . import module1       # Import module1 from the same package
# from ..subpackage import module2  # Import module2 from a parent package

# 8. PYTHONPATH
# Python searches for modules in the current directory, standard library, and paths listed in PYTHONPATH.
# You can add custom paths to PYTHONPATH to make your modules discoverable.

# SUMMARY
# - A module is a single Python file
# - A package is a folder containing multiple modules and an __init__.py file
# - Use import statements to reuse code from modules and packages
# - Built-in modules are available by default
# - Third-party modules require installation using pip
# - Custom modules are created by you for organizing and reusing your code