class Vehicle:
    def __init__(self, vehicle_type, model, price):
        self.vehicle_type = vehicle_type
        self.model = model
        self.price = price

        self.owner = None

    def buy(self, money, owner):
        self.money = money
        if self.owner is not None:
            return "Car already sold"

        if self.price > money:
            return "Sorry, not enough money"

        if self.price <= money:
            self.owner = owner
            return f"Successfully bought a {self.vehicle_type}. Change: {self.money - self.price:.2f}"

    def sell(self):
        if self.owner is not None:
            self.owner = None
            return

        return "Vehicle has no owner"

    def __repr__(self):
        if self.owner is None:
            return f"{self.model} {self.vehicle_type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.vehicle_type} is owned by: {self.owner}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type, model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)
