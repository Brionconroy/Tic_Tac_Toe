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
    Get users name and make sure the there is input validation.
    """
    print("Enter user name: ")
    while True:
        username = input("My name is: ")
        if not username.isalpha():
            print("Accept alphabetical characters only! Try again")
            continue
        else:
            print(f"You're going down {username}!")
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


playing_game = True

turn = 0

while playing_game:
    # Resets the screen
    os.system("cls" if os.name == "nt" else "clear") # This code was taken from CScode
    print_board(coordinate)
    # Player input
    users_turn = input()
    if users_turn == "e":
        # End the game
        playing_game = False

    turn += 1
    coordinate[int(users_turn)] = check_turn(turn)
