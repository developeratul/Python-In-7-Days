"""
Type check

Write a function named only_ints that takes two parameters. Your function should return True if both parameters are integers, and False otherwise.

For example, calling only_ints(1, 2) should return True, while calling only_ints("a", 1) should return False.
"""


def only_ints(p1, p2):
    return type(p1) == int and type(p2) == int


print(only_ints(1, "ant"))
print(only_ints(1, 2))