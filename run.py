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


def welcome_message():
    """
    Welcomes the user to the game and asks them to input there name
    and exlains the roles of Tic-Tac_Toe to the user.
    """

    print("Well Hello there!")
    print("welcome to Tic-Tac-Toe")
    print("The board is 3x3")
    print("Join three counters in a row before the computer to win")
    print("All spaces on the board taken up be counters will result in a draw")

    username = input("Enter user name: ")
    print(f"Youre going down {username}!")

print(welcome_message())