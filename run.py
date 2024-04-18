import random
import gspread
from google.oauth2.service_account import Credentials
# Importing all the libraries needed for this project


SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('python_games').sheet1
# Opening google sheet with the name python_games and storing it into SHEET variable.


# Sign up Page. Comparing username and password with the column 'Username' and 'Password' from google sheet.
def signup():
    print("Welcome to the game! Please sign up to continue.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    # Appending username and password in a row in the google sheet.
    SHEET.append_row([username, password])
    print("Sign up successful!")

 def login():
    print("Welcome back! Please login to continue.")
    # Added .strip to remove any space between names
    username = input("Enter your username: ").strip()
    password = input("Enter your password: ").strip()

    # To get the dimensions of the spreadsheet
    rows = SHEET.row_count
    cols = SHEET.col_count

    # Iterating over each row to find the matching username and password

    for row in range(2, rows + 1):  # Start from row 2 to skip the first row as it contains the headers

        stored_username = SHEET.cell(row, 1).value.strip()  # Username column
        stored_password = SHEET.cell(row, 2).value.strip()  # Password column

    # True condition if both input matches the data in the spread_sheet
        if stored_username == username and stored_password == password:
            print("Login successful!")
            return True

    print("Invalid username or password.")
    return False   

# First game: Guess the number
def guess_the_number():
    print("Welcome to Guess the Number!")
    number = random.randint(1, 100)
    tries = 0

# Using the while loop so the user can try as much as they want.
    while True:
        try:
            guess = int(input("Guess the number (between 1 and 100): "))
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Congratulations! You guessed {number} in {attempts} tries.")
                break
# Except handler in case the input is not a number                
        except ValueError:
            print("Please enter a valid number.")
