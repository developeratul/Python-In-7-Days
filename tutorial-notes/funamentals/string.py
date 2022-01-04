# strings are immutable it means you can't mutate it using indexes such as str[0] = "b"
# * python string slicing -> [starting index, ending index, steps]
""" pyString = "Ratul is a programmer"

name = pyString[0:6]
verb = pyString[6:9]
profession = pyString[11:]

print(name)
print(verb)
print(profession) """

# * loop through a string
""" name = "DeveloperRatul"
for i in name:
  print(i) """

# * string methods
""" name = "DeveloperRatul"
print(name.isalpha())

phone = "01872786579"
print(phone.isdigit()) """