# slicing is same everywhere in python
""" l = ["Ratul", "DevR", "Coder"]

print(l)

l[2] = "Developer Ratul"

print(l) """

# appending new item
""" l.append("Programmer")

print(l) """

# deleting
""" del l[-1]

print(l) """

# destructuring
""" [name, profession] = ['DevR', "Coder"]
print(name, "is a", profession) """

# list comprehention
# the syntax: [expression, for item in list, if condition] no (", ")
""" a = [x for x in range(10) if x % 2 == 0]
print(a) """

# list methods
""" l = [3, 1, 2, 7, 4, 5]

l.append(5)
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.index(2))

print(l.count(5))

l.clear()
print(l) """

# list functions
""" l = [1, 2, 3, 4, 5, 6]

print(len(l)) # also works with strings
print(max(l)) # returns the biggest item. Only works with integer list
print(min(l)) # returns the smallest item. again only works with intereger list
print(list("DevR")) # this one is a class which takes a sequence as the argument
print(sum(l)) # returns the sum of all the list items. Only for integers """

# for loop
""" l = [1, 2, 3, 4, True, "DevR", False, 8 + 9j]

for i in l:
  if type(i) == int:
    i *= 2
  print(i) """