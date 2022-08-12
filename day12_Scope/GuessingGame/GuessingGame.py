# Objectives:
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from GuessingGameArt import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5


def check_answers(guess, answer, turns):
    """checks answer against guess. Returns the number of turns remaining."""
    if guess > answer:
        print("Too high.")
        return turns - 1
    elif guess < answer:
        print("Too low.")
        return turns - 1
    else:
        print(f"You got it! The correct number was {answer}!")


def set_difficulty():
    level = str(input("Select your difficulty. Type 'easy' or 'hard': ")).lower()
    if level == 'easy':
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS


def play_game():
    print(logo)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    answer = random.randint(1, 101)

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int((input("Make a guess: ")))
        turns = check_answers(guess, answer, turns)

        if turns == 0:
            print("You lose! You've run out of guesses.")
            return
        elif guess != answer:
            print("Guess again")


while input("Do you want to play the Number Guessing Game? Type 'y' or 'n': ") == "y":
    play_game()