# game.py

print("Rock, Paper, Scissors, Shoot!")


# ask for a user input
# source: https://docs.python.org/3/library/functions.html#input
player_choice = input("Please choose one of the following: 'rock,' 'paper,' or 'scissors.'")
print("----------------")
# validate user input

if (player_choice == "rock") or (player_choice == "paper") or (player_choice == "scissors"):
    print("YOU CHOSE:", player_choice)
else:
    print("BOOOOOO! WRONG! TRY AGAIN")
    exit()


# generate computer choice
# source: https://pynative.com/python-random-choice/#h-python-random-choice-function
import random

computer_options = ["rock", "paper", "scissors"]
computer_choice = (random.choice(computer_options))
# random item from list
print("I CHOSE:", computer_choice)

print("----------------")


# determine winner
# display final results
print("AND THE WINNER IS:")
# source: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/
if (player_choice == computer_choice):
  print("We both chose", player_choice, ". It's a tie! Good game!")
elif (player_choice == "rock"):
    if (computer_choice == "scissors"):
      print(player_choice, "smashes", computer_choice, "...YOU WIN! This time...")
    if (computer_choice == "paper"):
      print("ME!!!", computer_choice, "covers", player_choice,". So sad, you lose!")
elif (player_choice == "paper"):
    if (computer_choice == "rock"):
      print(player_choice, "covers", computer_choice,"...YOU WIN! This time...")
    if (computer_choice == "scissors"):
      print("ME!!!", computer_choice, "cuts", player_choice,". So sad, you lose!")
elif (player_choice == "scissors"):
    if (computer_choice == "paper"):
      print(player_choice, "cuts", computer_choice,"...YOU WIN! This time...")
    if (computer_choice == "rock"):
      print("ME!!!", computer_choice, "smashes", player_choice,". So sad, you lose!")
else: print("come back later")
 



#ADD a play again option?
#restart_or_quit = input("PLAY AGAIN? Type 'yes' or 'no.'")





