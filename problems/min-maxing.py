"""
Min-maxing

Define a function named largest_difference that takes a list of numbers as its only parameter.

Your function should compute and return the difference between the largest and smallest number in the list.

For example, the call largest_difference([1, 2, 3]) should return 2 because 3 - 1 is 2.

You may assume that no numbers are smaller or larger than -100 and 100.
"""


def largest_difference(l):
    largest_number = 0
    smallest_number = l[0]
    for i in l:
        if i > largest_number:
            largest_number = i
        if i < smallest_number:
            smallest_number = i
    return largest_number - smallest_number


print(largest_difference([22, 33, 11, 23, 3982]))
print(largest_difference([1, 2, 3, 4, 5]))
