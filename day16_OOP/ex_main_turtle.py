import turtle
from turtle import Turtle, Screen

# create a new turtle object
# OUTPUT --- <turtle.Turtle object at 0x1090a5c90>
# new class object created saved at location in computer


timmy = Turtle()
print(timmy)
timmy.shape("turtle")
timmy.color("green")


def turtle_turn():
    turtle.forward(50)
    turtle.right(90)

turtle_turn()
turtle_turn()
turtle_turn()
turtle_turn()


# exit on click allows program to run until window is clicked
my_screen = Screen()
print(my_screen.canvheight)
my_screen.exitonclick()


