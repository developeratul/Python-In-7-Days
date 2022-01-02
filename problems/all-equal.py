"""
All equal

Define a function named all_equal that takes a list and checks whether all elements in the list are the same.

For example, calling all_equal([1, 1, 1]) should return True.
"""


def all_equal(l):
    result = True
    for i in range(len(l) - 1):
        if l[i] != l[i + 1]:
            result = False

    return result


print(all_equal([1, 1, 1, 1]))
print(all_equal([1, 2, 1, 1]))

# naive solution
""" def all_equal(items):
    for item1 in items:
        for item2 in items:
            if item1 != item2:
                return False
    return True """