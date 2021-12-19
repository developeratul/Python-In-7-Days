"""
Flatten a list
Write a function that takes a list of lists and flattens it into a one-dimensional list.

Name your function flatten. It should take a single parameter and return a list.

For example, calling:

flatten([[1, 2], [3, 4]])
Should return the list:

[1, 2, 3, 4]
"""


def flatten(l):
    result = []
    for i in l:
        if type(i) == list:
            for j in i:
                result.append(j)
        else:
            result.append(i)
    return result


print(flatten([[1, 2], [3, 4], 5, 6, 7]))
print(flatten([[1, 2], [3, 4]]))
