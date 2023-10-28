# Importing in Python is the process of loading code from a Python module into the current script.
# The import statement allows you to load modules and use their functions, classes or variables within your own scripts:
# To import a module in Python, you use the import statement followed by the name of the module.

import math

# You can also import specific functions or variables from a module using the from keywfrom 
from math import sqrt

# You can also import multiple functions or variables at once by separating them with a comma:

from math import sqet, pi 

# it's also possible to import all functions and variables from a module using the * wildcard. 

from math import *

# Python also allows you to rename imported modules using the as keyword. 

import math as m

# Python has a built-in function called dir that you can use to view the names of 
# all the functions and variables defined in a module. 
# This can be helpful for exploring and understanding the contents of a new module.

print(dir(math))