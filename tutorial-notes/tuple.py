# tuples are immutable
# all the methods are same as lists (same as lists)
# all the list functions are also valid in tuple
# they are iterable

tup = (1, 2, 3, 4, 5)

print(len(tup)) # also works with strings
print(max(tup)) # returns the biggest item. Only works with integer list
print(min(tup)) # returns the smallest item. again only works with intereger list
print(tuple("DevR")) # this one is a class which takes a sequence as the argument
print(sum(tup)) # returns the sum of all the list items. Only for integers """

for i in tup:
  print(i)