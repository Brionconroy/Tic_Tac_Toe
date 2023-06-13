# TIC-TAC-Toe Python

## Introduction

Tic-tac-toe is a game where you must place three counters in a row to win. The board is 3 x 3, after each time you place a counter your apponent makes there move. if no one wins by the time all the counters are placed the result in a draw.

## User Experience (UX)

As a new visitor to the site, I want to be able to quickly and simply understand what the game is and the how to play.

# Features

## Rules

The instructions for the game appear as you start the program. 

## User name input

Each player is then asked for there name. This is so it can be added to a google sheets to keep a record of who wins the game.

## Game board

The game board is 3x3 each, a dictionary was used to map the coordenats and to save the data on the board.

## Result section

who ever wins the game will get congradulations.

If it is a draw that will olse be agnolaged 

## Features I'd like to add

- Score counter
- Play agianst the computer.
- Make the game more visualy attractive by adding colour.
- Extra game modes.

## Bugs


## Testing

I have tested this game in the folloing ways:

- I used the Ad-hoc test in Gitpod while i was making this game.
- I manulay tested the game by inputting in invalid data to the terminal, no errors where found.
- I passed my code throught the PEP8 validator with no errors.
- I tested the game in the terminal in Heroku, everthing worked perfecrt.

## Validation Testing

No errors where found when passing through the PEP8 validater.

## Deployment


## Credits


## Content










![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome,

This is the Code Institute student template for deploying your third portfolio project, the Python command-line project. The last update to this file was: **March 14, 2023**

## Reminders

- Your code must be placed in the `run.py` file
- Your dependencies must be placed in the `requirements.txt` file
- Do not edit any of the other files or your code may not deploy properly

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
