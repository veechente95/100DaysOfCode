import random
from GameData import data
from HigherLowerGameArt import logo, vs


def get_random_account():
    """Get data from random account"""
    return random.choice(data)


def format_data(account):
    """Pulls account name, description and country key data from GameData data. """
    name = account["name"]
    description = account["description"]
    country = account["location"]
    return f"{name}, {description}, {country}"


def check_answer(guess, a_followers, b_followers):
    """Compares user and computer guess and returns True if they got it right OR False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"
    

def play_game():
    print(logo)
    print(f"Compare A: {name}, a {description}, from {location}.")
    print(vs)
    print(f"Against B: {name}, a {description}, from {location}.")

    print(str(input("Who has more followers? Type 'A' or 'B': ")))






play_game()
