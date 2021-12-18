# data's are stored as key and value pairs in dictionaries
# the key and value can be a string or and integer
# and you can access the value using the key
# dictionaries are mutable
# they are also iterable
obj = {
  "name": "DevR",
  "age": 16,
  "isActive": True
}

# access object value using the key and update value
""" print(obj["name"])
print(obj["age"])
print(obj["isActive"])

obj["profession"] = "Programmer"
print(obj) """

# iterate through objects
""" for i in obj:
  print("Key:", i, "| Value:", obj[i]) """

# dictionary methods
newObj = obj.copy()
print(newObj)
print(obj.fromkeys(["name", "age"], 10)) # create a dictionary with 2 keys and set the value to 10
print(obj.get("name"))
print(obj.items())
print(obj.keys())
# print(obj.pop("age"))
# print(obj)
# obj.popitem()
# print(obj)
# print(obj.setdefault("profession", "Programmer"))
# print(obj)
obj.update({ "name": "Ratul" })
print(obj)
print(obj.keys())
