# TODO: Create unlimited positional arguments (*args) for sum
def add(*args):
    sum = 0
    for num in args:
        sum += num
    return sum


print(add(3, 5, 6))


# TODO: Create unlimited keyword arguments (**kwargs) - NOTE turns into a dict
def calculate(num, **kwargs):
    num += kwargs["add"]
    num *= kwargs["multiply"]
    print(num)


calculate(2, add=3, multiply=5)  # 25


# TODO: **kwargs can be used with classes to
class Car:

    def __init__(self, **kw):
        self.make = kw.get("make")
        self.model = kw.get("model")
        self.color = kw.get("color")
        self.seats = kw.get("seats")


my_car = Car(make="Nissan", model="Skyline")
print(my_car.model)
