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

# First game: Rock Paper Scissor

def rock_paper_scissors():
    print("Welcome to Rock, Paper, Scissors!")

# List of available choices
    choices = ['rock', 'paper', 'scissors']
    while True:
        try:

# Input for choices. .lower() function to avoid so the input can be only small alphabet + no symbols or chracters.
            user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
            computer_choice = random.choice(choices)
            print(f"Computer chooses: {computer_choice}")

# Condition if the user choice is not in the list.
            if user_choice not in choices:
                print("Invalid choice. Please enter rock, paper, or scissors.")
# Tie condition
            elif user_choice == computer_choice:
                print("It's a tie!")

# Win condition
            elif (user_choice == 'rock' and computer_choice == 'scissors') or \
                    (user_choice == 'paper' and computer_choice == 'rock') or \
                    (user_choice == 'scissors' and computer_choice == 'paper'):
                print("You win!")
            else:
                print("Computer wins!")
            break
# Except handler in case user presses ctrl + C.
        except KeyboardInterrupt:
            print("\nThanks for playing Rock, Paper, Scissors!")
            break


# Main Function
def main():

# Using the while loop so the user can try as much as they want.
    while True:

# Choices once the user logged in

        print("\nSelect a game:")
        print("1. Guess the Number")
        print("2. Rock, Paper, Scissors")
        print("3. Exit")
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            guess_the_number()
        elif choice == '2':
            rock_paper_scissors()
        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")

if __name__ == "__main__":

# Using the while loop so the user can try as much as they want.
    while True:
        print("\nSelect an option:")
        print("1. Sign Up")
        print("2. Login")
        print("3. Exit")
        option = input("Enter your option (1, 2, or 3): ")

# 1st Choice: Sign up
        if option == '1':
            signup()
            
# 2nd Choice: Login           
        elif option == '2':
            if login():
                main()
                break
        elif option == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please enter 1, 2, or 3.")
