# Define a function called paint_calc() so that the code below works.
import math

test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5


def paint_calc(height, width, cover):
    area = height * width
    # math.ceil "ceiling" rounds to whole number
    num_of_cans = math.ceil(area / cover)   
    print(f"You will need {num_of_cans} cans of paint")


paint_calc(height=test_h, width=test_w, cover=coverage)


