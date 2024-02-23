#Number Guessing Game Objectives:

from random import randint

# Include an ASCII art logo.
from art import logo

#Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).
EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

# Check user's guess against actual answer. 
# Print "Too high." or "Too low." depending on the user's answer.
def check_answer(guess,answer,turns):
    if guess>answer:
        print("Too high!")
        return turns - 1
    elif guess<answer:
        print("Too low!")
        return turns - 1
    # If they got the answer correct, show the actual answer to the player.
    else:
        print(f"You got it! The answer was {answer}.")

#Make function to set difficulty
def self_difficulty():
    level = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if(level == "easy"):
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def play():
    # Allow the player to submit a guess for a number between 1 and 100.
    print(logo) 
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    #Choosing a random number between 1 and 100.
    answer = randint(1, 100)
    print(f"Pssst, the correct answer is {answer}") 
    turns = self_difficulty()
    guess = 0
    # Track the number of turns remaining.
    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")

        guess = int(input("Guess a number! "))

        turns = check_answer(guess,answer,turns)
        
        if(turns == 0):
            print("You've run out of guesses, you lose.")
            return
        elif guess != answer:
            print("Guess again.")   
play()

