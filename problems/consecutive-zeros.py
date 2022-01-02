"""
Consecutive zeros

The goal of this challenge is to analyze a binary string consisting of only zeros and ones. Your code should find the biggest number of consecutive zeros in the string. For example, given the string:

"1001101000110"
The biggest number of consecutive zeros is 3.

Define a function named consecutive_zeros that takes a single parameter, which is the string of zeros and ones. Your function should return the number described above.
"""


def consecutive_zeros(string):
    string_list = string.split("1")
    for i in string_list:
        if i == "":
            string_list.remove(i)
    result = 0
    for i in string_list:
        if len(i) > result:
            result = len(i)
    return result


print(consecutive_zeros("1000000"))
print(consecutive_zeros("1001101000110"))