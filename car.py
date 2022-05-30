# A Simple Class to show how to create an object

class Car:
    def __init__(self):
        self.model = "Tesla"
        self.color = "Black"

new_car = Car
print(new_car.model)
