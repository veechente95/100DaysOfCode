import turtle
from turtle import Turtle, Screen

michelangelo = Turtle()
michelangelo.shape("turtle")
michelangelo.color("green")
michelangelo.forward(100)

my_screen = Screen()

# exit on click allows program to run until window is clicked
my_screen.exitonclick()
