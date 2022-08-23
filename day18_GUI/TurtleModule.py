# '*' means you can import everything from module
import turtle
from turtle import Turtle, Screen
import random

ninja_turtle = Turtle()
ninja_turtle.shape("turtle")
ninja_turtle.pensize(2)
ninja_turtle.speed("fastest")
colors = ["red", "DarkSeaGreen", "cyan", "purple", "gold", "blue"]
turtle.colormode(255)
directions = [0, 90, 180, 270]


# TODO: Draw dash lines
# for i in range(15):
#     ninja_turtle.forward(20)
#     ninja_turtle.penup()
#     ninja_turtle.forward(20)
#     ninja_turtle.pendown()

# TODO: Draw triangle, square, pentagon ... decagon(10) shapes using list of colors
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for i in range(num_sides):
#         ninja_turtle.forward(100)
#         ninja_turtle.right(angle)
#
#
# for shape_side_num in range(3, 11):
#     ninja_turtle.color(random.choice(colors))
#     draw_shape(shape_side_num)


# TODO: Make a spirograpgh

def random_rgb_color():
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    random_color = (red, green, blue)
    return random_color


# # TODO: Generate random RBG colors AND random walk
# for i in range(200):
#     ninja_turtle.color(random_rgb_color())
#     ninja_turtle.forward(30)
#     ninja_turtle.setheading(random.choice(directions))

def spirograph(size_of_gap):
    for i in range(int(360 / size_of_gap)):
        ninja_turtle.color(random_rgb_color())
        ninja_turtle.circle(100)
        ninja_turtle.setheading(ninja_turtle.heading() + size_of_gap)


spirograph(5)


# This displays and exits the turtle screen
screen = Screen()
screen.exitonclick()
