import gspread
import os
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('tic_tac_toe')

coordinate = {1 : "1", 2 : "2", 3 : "3", 4 : "4", 5 : "5", 6 : "6", 7 : "7", 8 : "8", 9 : "9"}

def welcome_message():
    """
    Welcomes the user to the game and asks them to input there name
    and exlains the roles of Tic-Tac_Toe to the user.
    """
    print("Well Hello there!")
    print("welcome to Tic-Tac-Toe")
    print("The board is 3x3")
    print("To win join three counters in a row before the computer")
    print("All spaces on the board taken up be counters will result in a draw")
    print("To exit the game at any time press 'e")

def get_user_name():
    """
    Get users name and make sure that there is input validation.
    """
    while True:
        username = input("Enter Player 1 name: ")
        if not username.isalpha():
            print("Accept alphabetical characters only! Try again")
            continue
        else:
            print(f"Good luck {username}!")
            break
    return username


def print_board(coordinate):
    """
    The function creates the game board in the terminal.
    Using f string syntax to be able to update the board.
    """
    game_board = (f"|{coordinate[1]}|{coordinate[2]}|{coordinate[3]}|\n"
                    f"|{coordinate[4]}|{coordinate[5]}|{coordinate[6]}|\n"
                    f"|{coordinate[7]}|{coordinate[8]}|{coordinate[9]}|\n"
                    )
    print(game_board)

def check_turn(turn):

    if turn % 2 == 0: return "O"
    else: return "X"

def winning_conditions(coordinate):
    """
    This finction determines the winning condtions for the game.
    """
    if (coordinate[1] == coordinate[5] == coordinate[9]) \
       or (coordinate[3] == coordinate[5] == coordinate[7]):
       return True
    elif (coordinate[1] == coordinate[4] == coordinate[7]) \
       or (coordinate[2] == coordinate[5] == coordinate[8]) \
       or (coordinate[3] == coordinate[6] == coordinate[9]):
       return True
    elif (coordinate[1] == coordinate[2] == coordinate[3]) \
       or (coordinate[4] == coordinate[5] == coordinate[6]) \
       or (coordinate[7] == coordinate[8] == coordinate[9]):
       return True
    else: return False

playing_game = True

end_game = False

turn = 0

last_turn = -1

welcome_message()
get_user_name_1()


while playing_game:
    # Keeps the same board on the screen.
    os.system("cls" if os.name == "nt" else "clear") # This code was taken from CScode
    print_board(coordinate)
    # Print statment of an invalid trun.
    if last_turn == turn:
        print("Someone has already gone there. pick another coordinate and try again")
    last_turn = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your coordinate on the board")
    # Player input.
    users_turn = input()
    # Exit the game.
    if users_turn == "e":
        print("Goodbye...")
        playing_game = False
        # Check if the user has has entered a valid input from 1 to 9.
    elif str.isdigit(users_turn) and int(users_turn) in coordinate:
        # Make sure spot has not been taken already.
        if not coordinate[int(users_turn)] in {"X", "O"}:
            # Validates input to the board and updates the board, if valid input.
              turn += 1
              coordinate[int(users_turn)] = check_turn(turn)
        # Check for a win.
    if winning_conditions(coordinate): playing_game, end_game = False, True
    # Draw result
    if turn > 8: playing_game = False




