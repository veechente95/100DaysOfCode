import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_symbols = int(input(f"How many symbols would you like?\n"))
number_numbers = int(input(f"How many numbers would you like?\n"))

#Hard Level - Order of characters randomised:
password_list = []
for characters in range(1, number_letters + 1):     # letters +1 captures end of range to not exclude value
    password_list.append(random.choice(letters))
for characters in range(1, number_symbols + 1):
    password_list += random.choice(symbols)
for characters in range(1, number_numbers + 1):
    password_list += random.choice(numbers)

random.shuffle(password_list)
print(password_list)

password = ""
for char in password_list:
    password += char

print(f"Your password is: {password}")