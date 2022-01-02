"""
  Categories of functions in python
  1. Built-in
  2. Modules
  3. User defined
"""
# * builtin functions such as type(), sum(), len(), min(), max() etc

# * modules
# import pi
# from math import pi, sin
""" from math import *

print(pi)
print(sin(90)) """

# * User defined
# get the sum of a list
""" from math import floor


def average(list, rounded=False):
    '''Get the average of a list'''
    sum_of_list = sum(list)
    length_of_list = len(list)
    result = (
        floor(sum_of_list / length_of_list) if rounded else sum_of_list / length_of_list
    )
    return result


l = [1, 23, 21, 50, 100, 80, 53]

# get the doc string of a function
print(average.__doc__)

print(average(l)) """

# write a function which takes a list of name as the argument and greets hello world to each of them
def greet(list):
    for i in list:
        # template string
        greet = "Hello {name}! how you doing!".format(name=i)
        print(greet)


l = ["Ratul", "devR", "Developer Ratul"]

greet(l)