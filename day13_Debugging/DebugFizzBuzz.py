# Exercise 3 - FizzBuzz
# Changed 'or' to an 'and' statement and 'if' to 'elif' statements

for number in range(1, 101):
    if number % 3 == 0 or number % 5 == 0:
        print("FizzBuzz")
    if number % 3 == 0:
        print("Fizz")
    if number % 5 == 0:
        print("Buzz")
    else:
        print([number])

# Correct Answer 
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:     # changes 'or' to 'and' statement 
        print("FizzBuzz")
    elif number % 3 == 0:                       # made 'if' to elif
        print("Fizz")
    elif number % 5 == 0:                       # made 'if' to elif
        print("Buzz")
    else:
        print(number)                           # removed '[]' around number
