# docstrings means documentation string
# Python Comments vs Docstrings

# Python Comments
# Comments are descriptions that help programmers better understand the intent and functionality 
# of the program. They are completely ignored by the Python interpreter.

# Python docstrings
# As mentioned above, Python docstrings are strings used right after the definition of a function,
# method, class, or module (like in Example 1). They are used to document our code.
# We can access these docstrings using the doc attribute.


def cube(n):
    '''this function returns the cube of given number'''
    print(n*n*n)
cube(2)
print('docstring:', cube.__doc__) # accessing docstring through __doc__ attribute