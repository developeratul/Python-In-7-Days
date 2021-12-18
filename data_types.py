# rating = 5.0
# print(rating, type(rating))

# name = "Ratul"
# print(name, type(name))

# isPassed = False
# print(isPassed, type(isPassed))

# marks = 98
# print(marks, type(marks))

# complex_number = 5 + 8j
# print(complex_number, type(complex_number))

# list = ["Ratul", "Turzo", "Shahadat", "Walid"]
# print(list, type(list))

# * Test
name = input("Enter your name: ")
age = int(input("Enter your age: "))
year_of_birth = complex(int(input("Enter the year of your birth: ")), 0)
is_new_user = False
list_of_favouite_fruites = input(
    "What are your favourite fruites (', '): ").split(", ")

print(".")
print("..")
print("...")
print(name, "is", age, "years old", "\nBorned in:", year_of_birth, "\nis new user:",
      is_new_user, "\nList of his favourite fruites", list_of_favouite_fruites)
