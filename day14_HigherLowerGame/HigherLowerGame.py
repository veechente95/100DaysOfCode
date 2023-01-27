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
    country = account["country"]
    return f"{name}, a {description} from {country}."


def check_answer(guess, a_followers, b_followers):
    """Compares user and computer guess and returns True if they got it right OR False if they got it wrong."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"


def play_game():
    """This runs the game while True"""
    print(logo)
    score = 0
    game_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_continue:
        account_a = account_b
        account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}")
        print(vs)
        print(f"Against B: {format_data(account_b)}")

        guess = (str(input("Who has more followers? Type 'a' or 'b': "))).lower()
        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]
        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        print(logo)
        if is_correct:
            score += 1
            print(f"You got it right! Current score: {score}.")
        else:
            game_continue = False
            print(f"Sorry, you got it wrong. Final score: {score}.")


play_game()
