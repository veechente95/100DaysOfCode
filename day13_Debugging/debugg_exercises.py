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
year = int
