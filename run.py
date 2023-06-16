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
WORKSHEET = SHEET.worksheet('high_score')

coordinate = {1: "1", 2: "2", 3: "3", 4: "4",
              5: "5", 6: "6", 7: "7", 8: "8", 9: "9"}

playing_game = True

end_game = False

turn = 0

last_turn = -1


def welcome_message():
    """
    Welcomes the user to the game and asks them to input there name
    and exlains the roles of Tic-Tac_Toe to the user.
    """
    print("Well Hello there and welcome to Tic-Tac-Toe")
    print("To win join three counters in a row before your opponent")
    print("A draw will accoure when neither players can place a counter")
    print("To exit the game at any time press 'e")


def get_user_name(player, row):
    """
    Get users name and make sure that there is input validation.
    """
    while True:
        username = input("Enter Player"+str(player)+" name: ")
        if not username.isalpha():
            print("Accept alphabetical characters only! Try again")
            continue
        else:
            print(f"Good luck {username}!")
            break
    if player == 1:
        WORKSHEET.update_cell(row, 1, username)
    else:
        WORKSHEET.update_cell(row, 2, username)


def get_last_row_that_has_input():
    """
    This fucntion checks if there is a value in
    the google sheets cell, if so it goes to the next cell.
    """
    i = 1
    if WORKSHEET.cell(i, 1).value is not None:
        i = i + 1
    return i


def print_board(coordinate):
    """
    The function creates the game board in the terminal.
    Using f string syntax to be able to update the board.
    """
    game_board = (f"|{coordinate[1]}|{coordinate[2]}|{coordinate[3]}|\n"
                  f"|{coordinate[4]}|{coordinate[5]}|{coordinate[6]}|\n"
                  f"|{coordinate[7]}|{coordinate[8]}|{coordinate[9]}|\n")
    print(game_board)


def check_turn(turn):
    """
    This fucntion checks who's turn it is.
    """
    if turn % 2 == 0:
        return "O"
    else:
        return "X"


def winning_conditions(coordinate):
    """
    This finction determines the winning condtions for the game.
    """
    # This checks the winning condtions on the diaganals
    if (coordinate[1] == coordinate[5] == coordinate[9]) \
       or (coordinate[3] == coordinate[5] == coordinate[7]):
        return True
    # This checks the winning condtions on the verticals
    elif (coordinate[1] == coordinate[4] == coordinate[7]) \
        or (coordinate[2] == coordinate[5] == coordinate[8]) \
            or (coordinate[3] == coordinate[6] == coordinate[9]):
        return True
    # This checks the winning condtions on the horizontals
    elif (coordinate[1] == coordinate[2] == coordinate[3]) \
        or (coordinate[4] == coordinate[5] == coordinate[6]) \
            or (coordinate[7] == coordinate[8] == coordinate[9]):
        return True
    else:
        return False


input_row = get_last_row_that_has_input()


welcome_message()
get_user_name(1, input_row)
get_user_name(2, input_row)


while playing_game:
    # Keeps the same board on the screen.
    # This code was taken from CScode
    os.system("cls" if os.name == "nt" else "clear")
    print_board(coordinate)
    # Print statment of an invalid trun.
    if last_turn == turn:
        print("Spot taken! Pick another spot and try again")
    last_turn = turn
    print("Player " + str((turn % 2) + 1) + "'s turn: Pick your spot.")
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
            # Validates input to the board and updates the board.
            turn += 1
        coordinate[int(users_turn)] = check_turn(turn)
        # Check for a win.
    if winning_conditions(coordinate):
        playing_game, end_game = False, True
    # Draw result
    if turn > 8:
        playing_game = False

# This code was taken from CScode
os.system("cls" if os.name == "nt" else "clear")
print_board(coordinate)

if end_game:
    # winning result
    if check_turn(turn) == "X":
        WORKSHEET.update_cell(input_row, 3, "Player 1")
        print("player 1 wins")
    else:
        WORKSHEET.update_cell(input_row, 3, "Player 2")
        print("player 2 wins")
    # Exit game
elif users_turn == "e":
    WORKSHEET.update_cell(input_row, 3, "Game Not Finished")
    print("Goodbye...")
else:
    # Draw result.
    WORKSHEET.update_cell(input_row, 3, "Draw")
    print("It's a Draw!")

print("Good Game!")
