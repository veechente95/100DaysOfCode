# Building a coffee machine again using OOP this time
from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# create some objects from classes
menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True

while is_on:
    # 1) Ask User what they want
    options = menu.get_items()
    choice = str(input(f"What would you like? {options}: ")).lower()
    
    # 2) Turn off coffee machine by entering "off" to prompt
    if choice == "off":
    is_on = False
    
    # 3) Print report of all items and total money made
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    
    # Make drink if machine is resources sufficient AND money received is >= drink cost
    else:
        drink = menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink) and money_machine.make_payment(drink.cost):
            coffee_maker.make_coffee(drink)

            coffee_maker.make_coffee(drink)
