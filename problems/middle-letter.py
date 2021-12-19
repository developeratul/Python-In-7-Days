"""
Middle letter

Write a function named mid that takes a string as its parameter. Your function should extract and return the middle letter. If there is no middle letter, your function should return the empty string.

For example, mid("abc") should return "b" and mid("aaaa") should return ""
"""


def mid(string):
    stringLen = len(string)
    if stringLen % 2 != 0:
        middle_string_index = stringLen // 2
        result = string[middle_string_index]
        return result
    else:
        return ""


print(mid("abc"))