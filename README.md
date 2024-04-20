Welcome,

## Python Games

- There are 2 different games in this project.
- 1st game is Guess a number
   - In this game, the user has unlimited tries to guess a pre-determined random number between 1 and 100.
   - If the guess is higher than the random number, the game will tell you that it is too high.
   - If the guess is lower than the random number, the game will tell you that it is too low.
   - It will keep going on until user guess the correct number.
- 2nd game is Rock Paper Scissors, a classic that doesn't need any introduction.

## ## Project Goals
### User Stories

- Play both games.
- Be able to sign up as a new user.
- Be able to login as existing an user.
- Be able to choose any game.

### Site Owner Goals

- Create a game which is easy and clear to user.
- Ensure that new user is able to signup.
- Ensure that existing user can login.
- Ensure errors are handled and displayed to user.
- Ensure that user is able to understand the game.

## User Experience
### Target Audience

- There is no specific audience for the game as both games are basic and can be played by any age group.

### User Requirements and Expectations

- A simple and fun game.
- Straightforward Navigation.
- Log-in works as expected and incorrect details do not allow the user access to their account.

#### Launch Game

- On loading the game, users are presented with the option of sign up, login and exit.
- On login, users are presented with the choices of choosing any of the game mentioned above.

#### Sign Up

- If user is a new player, they will be required to sign up.
- User will be required to enter a new name and password.
- Once sign up is successful, user will be ask to login to play the game.
- Operation: Sign Up Here
- Enter New Username
- Enter New Password

#### Login

- If user is an existing user, they will be asked to enter username and password
- If it matches will the data, the user will be logged in.
- A welcome message on the screen will be displayed for the users with their name
- The input goes through a validation process. If the user input is not correct they have an option to try again .

### User Stories
## Users

- I want  have an option as an existing user or new user.
- I want to be able to signup as new user.
- I want to be able to choose different games.
- I want to be able to log-in if I return to the game.
- I want to be able to exit.

## Site Owner

- I want users to have a positive experience while playing the game.
- I want user names and password to be saved to Google Spreadsheet when signing up.
- I want the user to get errors displayed in case of wrong input.
- I want data entry to be validated, to guide the user on how to correctly format the input.

### Technology Used
## Language Used

- Python.

## Python Libraries used
- GSpread - to connect with google sheets.
- Random - used to choose random words.
- Strip - to remove any spaces.

### Other websites/tools used

- GitHub was used for saving and storing files.
- GitPod was the IDE used for writing code.
- Heroku was used as the deploying platform for this site.

### 3rd Party Python Libraries used
- Google sheets API was used to store and check the user input and authorize the user identity
- Google OAuth was used to connect the project with the google account.

### Manual Testing
<details><summary>See user stories testing</summary>

1. I want to be able to have an option as existing user or new user

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Are you an existing user | Type Y/N | Y: Open login area / N: SignUp Area | Works as expected
<details>
    <summary>Screenshots</summary>
    <p>Sign Up</p>
    <img src="assets/screenshots/ustory1-signup.png" alt="Sign up area">
    <p>Log In</p>
    <img src="assets/screenshots/ustory1-login.png" alt="Login area">
</details> 

2. I want to able to signup as new user

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Sign Up Here | Enter New Username/ Enter New Password | Sign Up Complete : Login Page opens | Works as expected
<details>
    <summary>Screenshots</summary>
    <p>Sign Up Area</p>
    <img src="assets/screenshots/signup.png" alt="Sign up area">
    <p>Login area opens after sign up is confirmed</p>
    <img src="assets/screenshots/userstory2.png" alt="Login area">
</details> 

3. I want to be able to log-in if I return to the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Login To Play Hangman | Username/ Password | Login Successful : Open rules | Works as expected

<details>
    <summary>Screenshots</summary>
    <p>Log In Area</p>
    <img src="assets/screenshots/ustory1-login.png" alt="Login area">   
    <p>Open rules is prompted after login is successful</p>
    <img src="assets/screenshots/ustory3.png" alt="Open rules">
</details> 

4. I want to be able to read the rules of the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Open Rules  | Type Y/N| Y: Open rules/ N: Starts Game | Works as expected

<details>
    <summary>Screenshots</summary>   
    <p>Open rules is prompted</p>
    <img src="assets/screenshots/ustory3.png" alt="Open rules">
    <p>If user input is "Y"</p>
    <img src="assets/screenshots/rules.png" alt="Rules of the game">
    <p>If user input is "N"</p>
    <img src="assets/screenshots/gamestart.png" alt="Game started">
</details> 

5. I want to be able to restart game when I'm logged in

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Restart Game  | Type Y/N| Y: Game restarts/ N: Game ends, User logged out | Works as expected

<details>
    <summary>Screenshots</summary>   
    <p>Restart is prompted</p>
    <img src="assets/screenshots/restartq.png" alt="Restart Question">
    <p>If user input is "Y"</p>
    <img src="assets/screenshots/restart.png" alt="Game restarts">
    <p>If user input is "N"</p>
    <img src ="assets/screenshots/ustory5.png" alt="Game ends">   
</details>

6. I want users to have a positive experience whilst playing the game

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | Simple navigation and game play  | Colored messages and straightforward instructions | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/ustory1-signup.png" alt="Sign up area">
    <img src="assets/screenshots/userstory2.png" alt="Login area">
    <img src="assets/screenshots/ustory3.png" alt="Open rules"> 
    <img src="assets/screenshots/restartq.png" alt="Restart Question">
</details>

7. I want user name and password to be saved to Google Spreadsheet

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Sign-Up | Users input their name and password which has not been previously registered  | Username and password are saved to Google Spreadsheet| Works as expected |

<details>
    <summary>Screenshots</summary>
    <p>Google Spread Worksheet</p>
    <img src="assets/screenshots/worksheet.png" alt="Worksheet">      
</details> 

8. I want the user to get errors displayed in case of wrong input

 **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | User inputs invalid input when questions are prompted. User inputs invalid value during log-in or sign-up | Feedback message displayed to the user | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/us9.png" alt="User Exist area">
    <img src="assets/screenshots/errorsignup.png" alt="Sign up area">
    <img src="assets/screenshots/errorlogin.png" alt="Login area">
    <img src="assets/screenshots/errorrules.png" alt="Open rules"> 
    <img src="assets/screenshots/errorrestart.png" alt="Restart Question">
</details>

9. I want data entry to be validated, to guide the user on how to correctly format the input

| **Feature**   | **Action**                    | **Expected Result**          | **Actual Result** |
| ------------- | ----------------------------- | ---------------------------- | ----------------- |
| Across all screen | User inputs invalid data | Feedback message with instructions diplayed to the user | Works as expected |

<details>
    <summary>Screenshots</summary>
    <img src="assets/screenshots/us9.png" alt="User Exist area">
    <img src="assets/screenshots/signU9.png" alt="Sign up area">
    <img src="assets/screenshots/loginUS9.png" alt="Login area">
    <img src="assets/screenshots/errorrules.png" alt="Open rules"> 
    <img src="assets/screenshots/errorrestart.png" alt="Restart Question">
</details>

