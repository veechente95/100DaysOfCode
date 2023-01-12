import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_on = True

while game_on:
    game_images = [rock, paper, scissors]
    user_choice = int(input("Please select '0' for rock, '1' for paper or '2' for scissors: "))
    computer_choice = random.randint(0, 2)

    if user_choice >= 3 or user_choice < 0:
        print("Invalid choice. Please select 0, 1, or 2.")
    elif user_choice == 0 and computer_choice == 2:
        print("YOU WIN! Rock beats scissors.")
        print(game_images[user_choice])
        print(game_images[computer_choice])
    elif user_choice == 1 and computer_choice == 0:
        print("YOU WIN! Paper beats rock.")
        print(game_images[user_choice])
        print(game_images[computer_choice])
    elif user_choice == 2 and computer_choice == 1:
        print("YOU WIN! Scissors beats paper.")
        print(game_images[user_choice])
        print(game_images[computer_choice])
    else:
        print("Computer Wins :(")
        print(game_images[user_choice])
        print(game_images[computer_choice])

    play_again = (input("Would you like to play again? Please select 'yes' or 'no': ")).lower()
    if play_again == "no":
        print("Bye! Thanks for playing!")
        game_on = False
