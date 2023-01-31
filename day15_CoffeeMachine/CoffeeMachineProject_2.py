from Menu import MENU, resources


# 4) Check if resources are sufficient
def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if not enough ingredients."""
    for item in order_ingredients:
        if order_ingredients[item] >= resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
        else:
            return True


# 5) Process coins
def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("How many quarters?: ")) * 0.25
    total += int(input("How many dimes?: ")) * 0.10
    total += int(input("How many nickles?: ")) * 0.05
    total += int(input("How many pennies?: ")) * 0.01
    return total


# 6) Check if transaction is successful
def is_transaction_successful(money_received, drink_cost):
    """Return True if payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry, that's not enough money. Money refunded.")
        return False


# 7) Make coffee if transaction is successful and there are enough resources to make drink
def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️")


profit = 0
is_on = True

while is_on:
    # 1) Ask User what they want
    choice = str(input(f"What would you like? "
                       f"Espresso (${MENU['espresso']['cost']}), "
                       f"latte (${MENU['latte']['cost']}), or "
                       f"cappuccino (${MENU['cappuccino']['cost']}): ")).lower()
    # 2) Turn off coffee machine by entering "off" to prompt
    if choice == "off":
        is_on = False
    # 3) Print report of all items and total money made
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Total Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])
