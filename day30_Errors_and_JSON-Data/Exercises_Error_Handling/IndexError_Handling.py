# Use what you've learnt about exception handling to prevent the program from crashing.
# If the user enters something that is out of range just print a default output of "Fruit pie". e.g.
# You'll need to catch the IndexError exception. You'll need the try, except and else keywords.

# ---------------------------------Original Code-----------------------------------------------------------------------
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    fruit = fruits[index]
    print(fruit + " pie")


make_pie(4)


# ---------------TODO: Catch the exception and make sure the code runs without crashing.---------------------
fruits = ["Apple", "Pear", "Orange"]


def make_pie(index):
    try:
        fruit = fruits[index]
        print(fruit + " pie")
    except IndexError:
        print("Fruit Pie")
    else:
        print(fruit + "pie")


make_pie(4)
