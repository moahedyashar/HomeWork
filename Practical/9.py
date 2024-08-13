class Vehicle:
    def drive(self):
        pass

class Bike(Vehicle):
    def drive(self):
        return "the Bike is driving"
    
class Truck(Vehicle):
    def drive(self):
        return "the truck is driving"
    
bike = Bike()
truck = Truck()

print(bike.drive())
print(truck.drive())