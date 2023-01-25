# Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer.
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player.
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
logo = """ 
██████╗ ██╗   ██╗███████╗███████╗███████╗    ████████╗██╗  ██╗███████╗    ███╗   ██╗██╗   ██╗███╗   ███╗██████╗ ███████╗██████╗ 
██╔════╝ ██║   ██║██╔════╝██╔════╝██╔════╝    ╚══██╔══╝██║  ██║██╔════╝    ████╗  ██║██║   ██║████╗ ████║██╔══██╗██╔════╝██╔══██╗
██║  ███╗██║   ██║█████╗  ███████╗███████╗       ██║   ███████║█████╗      ██╔██╗ ██║██║   ██║██╔████╔██║██████╔╝█████╗  ██████╔╝
██║   ██║██║   ██║██╔══╝  ╚════██║╚════██║       ██║   ██╔══██║██╔══╝      ██║╚██╗██║██║   ██║██║╚██╔╝██║██╔══██╗██╔══╝  ██╔══██╗
╚██████╔╝╚██████╔╝███████╗███████║███████║       ██║   ██║  ██║███████╗    ██║ ╚████║╚██████╔╝██║ ╚═╝ ██║██████╔╝███████╗██║  ██║
 ╚═════╝  ╚═════╝ ╚══════╝╚══════╝╚══════╝       ╚═╝   ╚═╝  ╚═╝╚══════╝    ╚═╝  ╚═══╝ ╚═════╝ ╚═╝     ╚═╝╚═════╝ ╚══════╝╚═╝  ╚═╝
 """

EASY_TURNS = 10
HARD_TURNS = 5


def check_answers(guess, answer, turns):
    if guess > answer:
        print("Too high!")
        return turns - 1
    elif guess < answer:
        print("Too low!")
        return turns - 1
    else:
        print(f"You win! The correct number was {answer}")


def set_difficulty():
    difficulty = str(input(f"Type 'easy' for {EASY_TURNS} turns or 'hard' for {HARD_TURNS} turns: ")).lower()
    if difficulty == 'easy':
        return EASY_TURNS
    else:
        return HARD_TURNS


def play_game():
    print(logo)
    answer = random.randint(1, 100)

    print("Welcome To The Number Guessing Game! I'm thinking of a number between 1 and 100.")
    print(f"[Pss ... The correct answer is {answer}]")

    turns = set_difficulty()
    guess = 0

    while guess != answer:
        print(f"You have {turns} attempts remaining to guess the number.")
        guess = int((input("Make a guess: ")))
        turns = check_answers(guess, answer, turns)

        if turns == 0:
            print(f"You lose! You've run out of guesses. The correct answer was {answer}.")
        elif guess != answer:
            print("Guess again! ")


play_game()

