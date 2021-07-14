# to launch: python game.py

#imports
import random
import os 
from dotenv import load_dotenv

load_dotenv() #loads content of .env file into script's environment

player_name = os.getenv("PLAYER_NAME")  #Best practice: use all caps for .env variable # Reads variable from .env


#Welcome Message

print("Hello",player_name) #reads the variable from the environment #good to use same variable names as environment

print("Would you like to play a game?")
enter_game = input("Please choose: YES or NO")

enter_game = enter_game.lower() # case (un)sensitive to ensure it matches "if" statement

print("----------------")

#Start Game

game_name = ("Rock, Paper, Scissors, Shoot!")

if (enter_game == "yes"):
  print(game_name)
else:
  print("That makes me sad. I was looking forward to winning.")
  exit()


# ask for a user input
# source: https://docs.python.org/3/library/functions.html#input
player_choice = input("Please choose one of the following: 'Rock,' 'Paper,' or 'Scissors.'")
print("----------------")

player_choice = player_choice.lower() # convert user input to lowercase to remove case sensitivity

# validate user input

if (player_choice == "rock") or (player_choice == "paper") or (player_choice == "scissors"):
    print("YOU CHOSE:", player_choice)
else:
    print("*Sigh* PLEASE TRY AGAIN")
    exit()


# generate computer choice
# random item from list
# source: https://pynative.com/python-random-choice/#h-python-random-choice-function

computer_options = ["rock", "paper", "scissors"]
computer_choice = (random.choice(computer_options))

print("I CHOSE:", computer_choice)
print("----------------")


# determine winner
# display final results

print("AND THE WINNER IS:")
# source: https://thehelloworldprogram.com/python/python-game-rock-paper-scissors/

if (player_choice == computer_choice):
  print("We both chose", player_choice,". It's a tie! Good game!")
elif (player_choice == "rock"):
    if (computer_choice == "scissors"):
      print(player_choice, "smashes", computer_choice, "...YOU WIN! This time...")
    if (computer_choice == "paper"):
      print("I WIN!", computer_choice, "covers", player_choice,". So sad, you lose!")
elif (player_choice == "paper"):
    if (computer_choice == "rock"):
      print(player_choice, "covers", computer_choice, "...YOU WIN! This time...")
    if (computer_choice == "scissors"):
      print("I WIN!", computer_choice, "cuts", player_choice,". So sad, you lose!")
elif (player_choice == "scissors"):
    if (computer_choice == "paper"):
      print(player_choice, "cuts", computer_choice, "...YOU WIN! This time...")
    if (computer_choice == "rock"):
      print("I WIN!", computer_choice, "smashes", player_choice,". So sad, you lose!")
else: print("come back later")

print("----------------")
print("Thanks for playing,",player_name,"!")
 







