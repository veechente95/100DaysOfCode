# TODO: Debugging Exercises

# Range needs to be (1, 21) if i == 20. Computer counts from 0, 1, 2...
def my_function():
    for i in range(1, 20):
        if i == 20:
            print("You got it!")
      
        
# Correct way
def my_function():
    for i in range(1, 21):
        if i == 20:
            print("You got it!")


my_function()
