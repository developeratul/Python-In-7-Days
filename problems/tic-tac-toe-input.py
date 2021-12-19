"""
Tic tac toe input

Here's the backstory for this challenge: imagine you're writing a tic-tac-toe game, where the board looks like this:

1:  X | O | X
   -----------
2:    |   |  
   -----------
3:  O |   |

    A   B  C
The board is represented as a 2D list:

board = [
    ["X", "O", "X"],
    [" ", " ", " "],
    ["O", " ", " "],
]
Imagine if your user enters "C1" and you need to see if there's an X or O in that cell on the board. To do so, you need to translate from the string "C1" to row 0 and column 2 so that you can check board[row][column].

Your task is to write a function that can translate from strings of length 2 to a tuple (row, column). Name your function get_row_col; it should take a single parameter which is a string of length 2 consisting of an uppercase letter and a digit.

For example, calling get_row_col("A3") should return the tuple (2, 0) because A3 corresponds to the row at index 2 and column at index 0in the board.
"""


def get_row_col(string):
    available_options = ["A1", "A2", "A3", "B1", "B2", "B3", "C1", "C2", "C3"]

    if string not in available_options:
        print("'{option}', this option is not allowed".format(option=string))

    letter = string[0]
    number = int(string[1])

    gameDict = {"A": 0, "B": 1, "C": 2}

    row = number - 1
    column = gameDict[letter]

    return (row, column)


print(get_row_col("C1"))
print(get_row_col("A3"))