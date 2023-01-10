#TODO: Make a roler coaster ride that determines if you are tall enough (120 cm or taller) to ride
#TODO: If tall enough, determine price for age
#TODO: If they want the photo picture, ask if they want to pay an additional $3

height = int(input("Welcome to the roller coaster ride! How tall are you in cm?: "))
bill = 0

if height >= 120:
    print("You can ride the roller coaster!")
    age = int(input("What is your age?: "))
    if age < 12:
        bill = 5
        print("Child tickets are $5")
    elif age <= 18:
        bill = 7
        print("Youth tickets are $7")
    else:
        bill = 12
        print("Adult tickets are $12")
    
    wants_photo = input("Do you want a copy of your photo taken?: Y or N?: ")
    if wants_photo == "Y":
        bill += 3
        
    print(f"Your final bill is ${bill}")
else:
    print("Sorry, you are too short to ride! ")
