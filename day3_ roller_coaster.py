#TODO: Make a roler coaster ride that determines if you are tall enough (120 cm or taller) to ride
#TODO: If tall enough, determine price for age

height = int(input("Welcome to the roller coaster ride! How tall are you in cm?: "))

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?: "))
    if age < 12:
        print("Please pay $5")
    elif age <= 18:
        print("Please pay $7")
    else:
        print("Please pay $12")
else:
    print("Sorry, you are too short to ride! ")
