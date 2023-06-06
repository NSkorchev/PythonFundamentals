class Car:
    def __init__(self, color, make, model, year):
        self.color = color
        self.make = make
        self.model = model
        self.year = year

    def accelerate(self):
        print("The car is accelerating.")

    def brake(self):
        print("The car is braking.")



my_car = Car("red", "Toyota", "Corolla", 2022)
my_car.accelerate()  # prints "The car is accelerating."
my_car.brake()       # prints "The car is braking."