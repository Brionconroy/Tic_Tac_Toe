# TIC-TAC-Toe Python

## Introduction

In the game tic-tac-toe you must place three counters in a row to win. The board is 3 x 3. After each time you place a counter your opponent makes their move. If no one wins by the time all the counters are placed, the result is a draw.

## User Experience (UX)

As a new visitor to the site, I want to be able to understand quickly and simply what the game is and how to play.

# Features

## Rules

The instructions for the game appear as you start the program.

## User name input

Each player is then asked for their name. This is so it can be added to Google sheets to keep a record of who wins the game.

## Game board

The game board is 3 x 3. A dictionary was used to map the coordinates and to save the data on the board.

## Result section

Whoever wins the game will get congratulations.

If it is a draw that will also be acknowledged. 

## Features I'd like to add

- Score counter
- Play against the computer.
- Make the game more visually attractive by adding colour.
- Extra game modes.

## Bugs


## Testing

I have tested this game in the following ways:

- I used the Ad-hoc test in Gitpod while I was making this game.
- I manually tested the game by inputting in invalid data to the terminal, no errors were found.
- I passed my code through the PEP8 validator with no errors.
- I tested the game in the terminal in Heroku, everything worked perfectly.

## Validation Testing

No errors were found when passing through the PEP8 validator.

## Deployment

- Make a clone of your repository.
- Set up a new Heroku app.
- Set the buildpacks to Python and NodeJS.
- Link your repository and your Heroku app.
- Click deploy.

Coding Institute's mock terminal app was used in Heroku.

## Credits

- Thanks to the tutors at Coding Institute and to my mentor Anthony for guiding me through my first project.
- I would also like to thank Katie Duggan for proof reading the content.

## Content

+ Code Institute love_sandwiches. [Coding Institute](https://learn.codeinstitute.net/courses/course-v1:CodeInstitute+LS101+2021_T1/courseware/293ee9d8ff3542d3b877137ed81b9a5b/c92755338ef548f28cc31a7c3d5bfb46/)
+ How to add Json data to a file. [Stack over flow](https://stackoverflow.com/questions/12309269/how-do-i-write-json-data-to-a-file)
+ Dictionary help and board display. [Youtube](https://www.youtube.com/watch?v=Q6CCdCBVypg)












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
