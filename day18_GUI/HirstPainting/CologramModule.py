# This module pulls the top colors displayed in an image
import turtle
import random


turtle.colormode(255)
mario = turtle.Turtle()
mario.speed("fastest")
mario.penup()
mario.hideturtle()
color_list = [(226, 4, 35), (249, 229, 200), (217, 231, 250), (109, 172, 230), (53, 93, 173), (242, 251, 249), (220, 163, 72), (238, 210, 90), (26, 134, 63), (153, 172, 54), (157, 89, 46), (73, 111, 194), (252, 236, 240), (29, 14, 4), (16, 34, 143), (88, 172, 59), (11, 19, 47), (233, 56, 80), (163, 184, 234), (249, 163, 154), (3, 24, 9), (177, 47, 76), (225, 123, 136), (127, 183, 128), (210, 88, 60), (250, 152, 160), (64, 9, 42), (173, 22, 12), (249, 222, 1), (89, 79, 17)]

mario.setheading(215)
mario.forward(300)
mario.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    mario.dot(20, random.choice(color_list))
    mario.forward(50)

    if dot_count % 10 == 0:
        mario.setheading(90)
        mario.forward(50)
        mario.setheading(180)
        mario.forward(500)
        mario.setheading(0)




# This displays and exits the turtle screen
screen = turtle.Screen()
screen.exitonclick()