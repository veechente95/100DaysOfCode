# OOP combines some data like attributes (variables) and functionality like methods (functions).
class Waiter:
    # Attributes or variables
    is_holding_plate = True
    tables_responsible = [4, 5, 6]

    # Methods or functionality
    def take_order(table, order):
        # takes order to chef

    def take_payment(amount):
        # adds money to restaurant
        
  
# Create a class - Class are made using Pascal case (all new words start with an upper case letter)

# car = object
# Class = CarBlueprint
car = CarBlueprint()


# Importing Turtle class example 
from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("aquamarine3")
my_screen = Screen()
timmy.forward(100)
timmy.left(90)

my_screen.exitonclick()


# Importing PrettyTable class example
from prettytable import PrettyTable
table = PrettyTable()
table.add_column("Pokemon Name", ["Pikachu", "Squirtle", "Charmander"])
table.add_column("Type", ["Electric", "Water", "Fire"])
table.align = "l"
