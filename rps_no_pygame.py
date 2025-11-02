import random

moves = ["rock", "paper", "scissors"]    # set of possible moves

print("This is a rock paper scissors game built without the pygame module. Enter your move below.")     # introduces the player
user_move = input("Your move is:", )    # asks for user input
if user_move in ("rock", "paper", "scissors"):      # checks if user input is valid
    comp_move = random.choice(moves)    # randomly generates the computer's move
    print("The computer's move is:", comp_move)     # displays the computer's move
else:
    print("Invalid move. Please enter rock, paper, or scissors.")

if user_move == comp_move:   # checks for a tie
    print("It's a tie. Please play again.")
    print("Your move is", )
else:
    if (user_move=="rock" and comp_move == "scissors") or (user_move == "paper" and comp_move == "rock") or (user_move == "scissors" and comp_move == "paper"):     # checks for a win by the user
        print("You Win!")
    else:
        print("You Lose!")
