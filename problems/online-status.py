"""
Online status

The aim of this challenge is, given a dictionary of people's online status, to count the number of people who are online.

For example, consider the following dictionary:

statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}
In this case, the number of people online is 2.

Write a function named online_count that takes one parameter. The parameter is a dictionary that maps from strings of names to the string "online" or "offline", as seen above.

Your function should return the number of people who are online.
"""


def online_count(dictionary):
    activeUsers = []
    for i in dictionary:
        if dictionary[i] == "online":
            activeUsers.append(dictionary[i])
    return len(activeUsers)


statuses = {
    "Alice": "online",
    "Bob": "offline",
    "Eve": "online",
}

print(online_count(statuses))

# short version
""" def online_count(people):
    return len([p for p in people if people[p] == "online"]) """