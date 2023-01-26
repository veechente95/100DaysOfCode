# TODO Debugging Exercises

# TODO 1) Describe the problem
# Range needs to be (1, 21) if i == 20. Computer counts from 0, 1, 2...
def my_function():
    for i in range(1, 20):   # change to (1, 21)
        if i == 20:
            print("You got it!")

my_function()


# TODO 2)  Reproduce the bug
# IndexError - dice images list counts from 0 to 5
from random import randint
dice_images = ["1️⃣", "2️⃣", "3️⃣", "4️⃣", "5️⃣", "6️⃣"]
dice_num = randint(1, 6)    # change to (0, 5)
print(dice_images[dice_num])


# TODO 3)  Play Computer - Pretend you are reading code line by line
# Why is it that when you inout 1994, nothing gets printed? # Need to add >= operation on elif line of code

year = int(input("What's your year of birth?: "))
if year > 1980 and year < 1994:         # (True) 1994 is greater than 1980 and (False) 1994 is not less than 1994 - Statement become False
    print("You are a millennial!")      # line doesn't print because False and True boolean make a False statement 
elif year > 1994:                       # (False) 1994 is not less than 1994
    print("You are a Gen Z!")           # line does not print

    
# TODO 4) Fix console errors before you continue
# TypeError - '>' not supported between instances of 'str' and 'int'

age = input("How old are you?: ")
if age > 18:
    print(f"You can drive at age {age}")

# Answer
age = int(input("How old are you?: "))   # convert to int() here
if age > 18:
    print(f"You can drive at age {age}")
