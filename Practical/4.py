import math

class Circle:
    def __init__(self, radius):
        self.radius = radius

    def compute_area(self):
        return math.pi * self.radius * self.radius
    
circle = Circle(5)
print(f"the area is {circle.compute_area()}")