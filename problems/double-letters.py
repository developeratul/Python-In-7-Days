"""
Double letters

The goal of this challenge is to analyze a string to check if it contains two of the same letter in a row. For example, the string "hello" has l twice in a row, while the string "nono" does not have two identical letters in a row.

Define a function named double_letters that takes a single parameter. The parameter is a string. Your function must return True if there are two identical letters in a row in the string, and False otherwise
"""


def double_letters(string):
    result = False
    for i in range(len(string) - 1):
        if string[i] == string[i + 1]:
            result = True
    return result


print(double_letters("boom"))
print(double_letters("damn!"))

# shorter solution
# using a list comprehension, zip, and any
""" def double_letters(string):
    return any([a == b for a, b in zip(string, string[1:])]) """