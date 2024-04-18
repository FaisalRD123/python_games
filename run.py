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
# Opening google sheet witht the name python_games


# Sign up Page. Comparing username and password with the column 'Username' and 'Password' from google sheet.
def signup():
    print("Welcome to the game! Please sign up to continue.")
    username = input("Enter a username: ")
    password = input("Enter a password: ")
    SHEET.append_row([username, password])
    print("Sign up successful!")
