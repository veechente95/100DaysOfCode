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

ATTEMPTS = 10
GUESS_NUMBER = random.randint(1, 100)


def calculate_score(user_guess, GUESS_NUMBER, turns):
    if user_guess != GUESS_NUMBER:
        new_attempts = ATTEMPTS - 1
    return new_attempts


def play_game():
    is_game_over = False

    print(logo)
    print("Welcome To The Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print(f"Pss ... The correct answer is {GUESS_NUMBER}")
    print(f"You have {ATTEMPTS} attempts remaining to guess the number.")
    user_guess = int(input("Make a guess: "))

    while not is_game_over:
        if user_guess > GUESS_NUMBER:
            print("Too high! Guess again.")
            print(f"You have {calculate_score(user_guess)} attempts remaining.")
        elif user_guess < GUESS_NUMBER:
            new_attempts = ATTEMPTS - 1
            print("Too low! Guess again. ")
            print(f"You have {calculate_score(user_guess)} attempts remaining. ")
        elif user_guess == GUESS_NUMBER:
            print(f"You win! The correct number was {GUESS_NUMBER}")
        else:
            if user_guess == 0:
                print(f"You lose! The correct number was {GUESS_NUMBER}")
            is_game_over = True


play_game()



