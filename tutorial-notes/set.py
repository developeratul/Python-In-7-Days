# dup's are not allowed in sets
# they are iterable but cannot be accessed using indexes like lists, cause they are stored in a random order
s = {1, 2, 3, 4, 4, 5, 1, 2, 3}

for i in s:
  print(i)