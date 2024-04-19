Welcome,

## Python Games

- There are 2 different games in this project.
- 1st game is Guess a number
   - In this game, the user has unlimited tries to guess a pre-determined random number between 1 and 100.
   - If the guess is higher than the random number, the game will tell you that it is too high.
   - If the guess is lower than the random number, the game will tell you that it is too low.
   - It will keep going on until user guess the correct number.
- 2nd game is Rock Paper Scissors, a classic that doesn't need any introduction.

## Creating the Heroku app

When you create the app, you will need to add two buildpacks from the _Settings_ tab. The ordering is as follows:

1. `heroku/python`
2. `heroku/nodejs`

You must then create a _Config Var_ called `PORT`. Set this to `8000`

If you have credentials, such as in the Love Sandwiches project, you must create another _Config Var_ called `CREDS` and paste the JSON into the value field.

Connect your GitHub repository and deploy as normal.

## Constraints

The deployment terminal is set to 80 columns by 24 rows. That means that each line of text needs to be 80 characters or less otherwise it will be wrapped onto a second line.

---

Happy coding!
