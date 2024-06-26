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
# Opening google sheet python_games and storing it into SHEET variable.

# Fetch user records from the spreadsheet and store them in a dictionary


def fetch_user_records():
    users = {}
    rows = SHEET.get_all_values()
    for row in rows[1:]:  # Start from the second row to skip the header
        username = row[0].strip()  # Username is in the first column
        password = row[1].strip()  # Password is in the second column
        users[username] = password
    return users

# Global variable to store user records


USERS = fetch_user_records()

# Signup function


def signup():
    print("Sign Up")
    # Get username input and strip leading/trailing whitespace
    username = input("Enter your username: ").strip()
    # Get password input and strip leading/trailing whitespace
    password = input("Enter your password: ").strip()

    # Fetch user records from the spreadsheet
    rows = SHEET.get_all_values()

    # Check if the username already exists in the spreadsheet
    existing_usernames = [row[0].strip() for row in rows[1:]]  # Skip head row
    if username in existing_usernames:
        print("Username already exists. Please choose a different username")
        return False

    # Append new user to the spreadsheet
    new_row = [username, password]
    SHEET.append_row(new_row)
    print("Sign up successful!")

    # Add new user to the globally stored USERS dictionary
    USERS[username] = password
    return True

# Login function


def login():
    print("Welcome back! Please login to continue.")
    # Get username input and strip leading whitespace
    username = input("Enter your username:\n ").strip()
    # Get password input and strip leading whitespace
    password = input("Enter your password:\n ").strip()
    # Check if the entered username exists in the stored user records
    if username in USERS:
        # If username exists, check if password matches the stored password
        if USERS[username] == password:
            print("Login successful!")
            return True
        else:
            print("Invalid password.")
    else:
        print("Invalid username.")
    return False

# First game: Guess the number


def guess_the_number():
    print("Welcome to guess the number game!")
    number = random.randint(1, 100)
    attempts = 0
    # Using the while loop so the user can try as much as they want.
    while True:
        try:
            guess = int(input("Guess the number (between 1 and 100):\n "))
            # Condition in case the input in not in the given range
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue
            attempts += 1
            if guess < number:
                print("Too low!")
            elif guess > number:
                print("Too high!")
            else:
                print(f"Wow! You guessed {number} in {attempts} tries.")
                break
        # Except handler in case the input is not a number
        except ValueError:
            print("Please enter a valid number.")


def rock_paper_scissors():  # First game: Rock Paper Scissor
    print("Welcome to Rock, Paper, Scissors!")
    choices = ['rock', 'paper', 'scissors']  # List of available choices
    while True:
        # User input. .lower() method so input is alphabet + no characters.
        user_choice = input("Enter choice (rock, paper, scissors): ").lower()
        # Random choice given to computer. Imported from random
        computer_choice = random.choice(choices)
        print(f"Computer chooses: {computer_choice}")

        if user_choice in choices:
            if user_choice == computer_choice:  # Tie condition
                print("It's a tie!")
            # Win condition
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                 (user_choice == 'paper' and computer_choice == 'rock') or \
                 (user_choice == 'scissors' and computer_choice == 'paper'):
                print("You win!")
            else:
                print("Computer wins!")
            break
        else:   # In case the input is wrong
            print("Invalid choice. Please enter rock, paper, or scissors.")


def main():
    # Main Function
    # Using the while loop so the user can try as much as they want.
    while True:
        # Choices once the user logged in
        print("\nSelect a game:")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3):\n ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("Thank you for playing!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")


if __name__ == "__main__":
    while True:   # Using the while loop so the user try as much as they want.
        print("\nSelect an option:")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your option: (1, 2, or 3):\n ")

        if option == '1':  # 1st Choice: Sign up
            signup()

        elif option == '2':  # 2nd Choice: Login
            if login():
                main()
                break
        elif option == '3':
            print("Exit!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
