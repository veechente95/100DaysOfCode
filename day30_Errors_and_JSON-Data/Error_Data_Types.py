# Try opening this file
try:
    file = open("a_file.txt")
    a_dictionary = {"key": "value"}
    print(a_dictionary["QWERTY"])

# FileNotFound Error - If file doesn't exist, we create it
except FileNotFoundError:
    file = open("a_file.txt", mode="w")
    file.write("File didn't exists so we created it by catching exceptions")

# KeyError - Can have multiple except blocks of code
except KeyError as error_message:
    print(f"The key {error_message} does not exist")

# if there were no exceptions, what else do you want to do
else:
    content = file.read()
    print(content)

# Finally runs code no matter what happens
finally:
    # raise allows you to create your own errors that you made up
    raise TypeError("This is an error I made up")


# -----------------------BMI example of raising an exception for invalid value ----------------------------------------
# Ex) raising exception to calculate BMI of someone that inputs height or weight that is unrealistic
# Yes the machine will run it, but how can we prevent someone from inputting that mistake

height = float(input("Height in meters: "))
weight = int(input("Weight in kilos: "))

if height > 3:
    raise ValueError("Human height is probably not over 3 meters.")

bmi = weight / height ** 2
print(bmi)