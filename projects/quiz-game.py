import os
from termcolor import colored

print("Hey there! Welcome to DevR-Quiz!")

want_to_play: str = input("Do you want to play?: ")

if want_to_play.lower() != "yes":
    print("Then why did you came here! Get out you stupid!!!")
    quit()

# all the questions
questions: list = [
    {
        "question": "What is the full form of DevR?",
        "answer": 2,
        "options": ["Dev Ratul", "Dev Raj", "Developer Ratul"],
    },
    {
        "question": "What is the full form of CPU?",
        "answer": 0,
        "options": [
            "Central Processing Unit",
            "Cooling Powered Utility",
            "Coding Power Unit",
        ],
    },
    {
        "question": "What is the best thing in the world?",
        "answer": 2,
        "options": [
            "Being Rich",
            "Being a programmer",
            "When your code works at the first attempt",
            "When you have a GF",
        ],
    },
    {
        "question": "What is GPU stand for?",
        "answer": 3,
        "options": [
            "Go Power Unit",
            "Good Power Utility",
            "Good Processing Unit",
            "Graphics Processing Unit",
        ],
    },
]

currentIndex: int = 0

# this var will be updated when the user will give correct answer
score: int = 0

# for showing up the next question
def nextQuestion(currentIndex: int, totalIndex: int) -> None:
    if currentIndex + 1 < totalIndex:
        askQuestion(currentIndex + 1)
    else:
        print(
            colored(
                f"The game has been ended thanks for playing. Your score was ({score}/{totalIndex})",
                "magenta",
            )
        )
        quit()


# for asking a question
def askQuestion(currentIndex: int) -> None:
    # accessing the global var so we can update/change it
    global score

    currentQuestion: dict = questions[currentIndex]

    print(colored(f"Q-{currentIndex + 1}: {currentQuestion['question']}", "cyan"))
    print("")

    for option in currentQuestion["options"]:
        print(f"{currentQuestion['options'].index(option) + 1}. {option}")

    print("")
    usersAnswer: str = input("Enter your decision here: ")

    correctAnswer: bool = True

    # if the user is typing alphaets then it will throw error when typecasting means the answer is still wrong
    try:
        correctAnswer = int(usersAnswer) - 1 == currentQuestion["answer"]
    except:
        correctAnswer = False

    if correctAnswer:
        # update the score cause the user has given correct answer
        score += 1
        print(colored("Your answer was correct", "green"))
    else:
        print(
            colored(
                f"Your answer was wrong! the correct answer was: '{questions[currentIndex]['options'][currentQuestion['answer']]}'",
                "red",
            )
        )

    nextQuestion(currentIndex, len(questions))


# at first ask the first question
askQuestion(currentIndex)