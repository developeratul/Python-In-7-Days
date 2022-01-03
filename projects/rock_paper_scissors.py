from random import randint
from termcolor import colored

choices: list = [
    colored("rock", "magenta"),
    colored("paper", "cyan"),
    colored("scissor", "yellow"),
]

user_won_attempts = 0
computer_won_attempts = 0

while True:
    print("What is your choice\n")

    for choice in choices:
        print(f"{choices.index(choice) + 1}. {choice}")

    users_choice: str = input("\nMake your choice (press 'q' to quit): ")
    computers_choice: str = choices[randint(0, len(choices) - 1)]

    if users_choice == "q":
        break
    elif users_choice.isdigit():
        users_choice: int = int(users_choice)

        if users_choice <= len(choices):
            users_choice: str = choices[users_choice - 1]
        else:
            print("Please enter value in range of (1-3)\n")
            continue

        print(f"\nYou: {users_choice}")
        print(f"Computer: {computers_choice}\n")

        gameDict: dict = {
            colored("rock", "magenta"): {
                colored("paper", "cyan"): 0,
                colored("scissor", "yellow"): 1,
                colored("rock", "magenta"): 0.5,
            },
            colored("paper", "cyan"): {
                colored("paper", "cyan"): 0.5,
                colored("scissor", "yellow"): 0,
                colored("rock", "magenta"): 1,
            },
            colored("scissor", "yellow"): {
                colored("paper", "cyan"): 1,
                colored("scissor", "yellow"): 0.5,
                colored("rock", "magenta"): 0,
            },
        }

        users_score = gameDict[users_choice][computers_choice]
        computers_score = gameDict[computers_choice][users_choice]

        if users_score == 1:
            print(colored("You won!\n", "green"))
            user_won_attempts += 1
        elif users_score == 0.5:
            print(colored("You tied\n", "yellow"))
        else:
            print(colored("You lose\n", "red"))
            computer_won_attempts += 1

    else:
        print("Please type a digit next time\n")
        continue

print(f"\nYou won {user_won_attempts} matches")
print(f"Computer won {computer_won_attempts} matches\n")

print("Thanks for playing! Bye :)")