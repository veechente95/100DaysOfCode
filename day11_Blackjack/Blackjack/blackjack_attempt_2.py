# House Rules -  The deck is unlimited in size. There are no jokers. The Jack/Queen/King all count as 10.
# The Ace can count as 11 or 1. cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]. The cards in the list have equal
# probability of being drawn. Cards are not removed from the deck as they are drawn. The computer is the dealer.

import random
logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""


def deal_card():
    """Return a random card from the card deck."""
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    card = random.choice(cards)
    return card


# Create a function called calculate_score() that takes a List of cards as input and returns the score.
# Check for a blackjack (a hand with only 2 cards: ace(11) + 10) & return 0 instead of the score. 0 means blackjack
# Check for an 11 (ace). If the score is over 21, remove the 11 and replace it with a 1.
def calculate_score(cards):
    """Takes a list of cards and calculates score."""
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)
    return sum(cards)


# Create a new func & pass in the user & computer score. If user & computer score are the same, then it's a draw.
# If computer has blackjack (0), user loses. If user has blackjack (0), user wins. If user score is > 21, user loses.
# If computer score > 21, computer loses. If none of the above, then the player with the highest score wins.
def compare(user_score, computer_score):
    """Compares the user and computer total card score"""
    if user_score == computer_score:
        return "Draw!"
    elif computer_score == 0:
        return "You lose! Computer has blackjack!"
    elif user_score == 0:
        return "You win with a blackjack!"
    elif user_score > 21:
        return "You went over 21! You lose!"
    elif computer_score > 21:
        return "Computer went over! You win!"
    elif user_score > computer_score:
        return "You win!"
    else:
        return "You lose!"


# Deal the user and computer 2 cards each using deal_card() and append().
def play_game():
    print(logo)

    user_cards = []
    computer_cards = []
    is_game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())

# If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.
# If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function
# to add another card to the user_cards List. If no, then the game has ended.
# The score will need to be rechecked with every new card drawn until the game ends.
    while not is_game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"User cards {user_cards}. Current score: {user_score}")
        print(f"Computer's first card: [{computer_cards[0]}]")

        if user_score == 0 or computer_score == 0 or user_score > 21:
            is_game_over = True
        else:
            draw_card = str(input("Do you want to draw another card? Select 'yes' or 'no: ")).lower()
            if draw_card == "yes":
                user_cards.append(deal_card())
            else:
                is_game_over = True

    # Once the user is done, the computer should keep drawing cards as long as it has a score less than 17.
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)

    print(f"Your finals hand: {user_cards}. Final score: {user_score}")
    print(f"Computer's finals hand: {computer_cards}. Final score: {computer_score}")
    print(compare(user_score, computer_score))

    compare(user_score, computer_score)


# Ask the user if they want to restart the game.
while input("Do you want to play a game of blackjack? Type 'yes' or 'no': ").lower() == 'yes':
    play_game()
    print(logo)
else:
    print("Bye Bye!")
