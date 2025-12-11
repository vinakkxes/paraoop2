class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"{self.brand} {self.model}: поехал")


class Car(Vehicle):
    def __init__(self, fuel_type):
        self.fuel_type = fuel_type
    
    def honk(self):
        print(f"{self.brand} {self.model}: сигналит")

class Bicycle(Vehicle):
    def __init__(self, gears):
        self.gears = gears
    
    def ring_bell(self):
        print(f"{self.brand} {self.model}: звенит")
