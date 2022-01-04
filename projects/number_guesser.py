from random import randint

range_of_number: str = input("Enter a number which will be the range: ")

if range_of_number.isdigit():
    range_of_number: int = int(range_of_number)
else:
    print("Please type a number next time")
    quit()

random_number: int = randint(0, range_of_number)
guesses: int = 0

while True:
    guesses += 1
    users_choice: str = input("Make your choice: ")

    if users_choice.isdigit():
        users_choice: int = int(users_choice)
    else:
        print("Please type a number next time")
        continue

    if users_choice == random_number:
        print("You got it correct!")
        break
    else:
        print("You were above the number" if users_choice > random_number else "You are below the number")

print(f"You got it in {guesses} guesses")