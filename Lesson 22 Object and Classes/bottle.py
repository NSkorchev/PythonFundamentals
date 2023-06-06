class Bottle:
    def __init__(self, ml, name, colour, material="plastic"):
        self.ml = ml
        self.name = name
        self.colour = colour
        self.material = material

    def open(self):
        print("Opening bottle")

    def close(self):
        print("Closing bottle")


bottle1 = Bottle(500, "Devin", "blue")
bottle2 = Bottle(1500, "Bankya", "blue")
bottle3 = Bottle(600, "Devin", "pink")
bottle4 = Bottle(500, "Gorna Banya", "white")
print(bottle1.ml)
bottle2.open()
bottle3.close()
print(bottle4)
