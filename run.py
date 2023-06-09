import gspread
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

    username = input("Enter user name: ")
    print(f"You're going down {username}!")

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


print_board(coordinate)