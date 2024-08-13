class Shape:
    def area(self):
        pass

class Square(Shape):
    def __init__(self, side_length):
        self.side_length = side_length
    def area(self):
        return self.side_length ** 2
    
class Triangle(Shape):
    def __init__(self, height, length):
        self.height = height
        self.length = length
    def area(self):
        return 0.5 * self.height * self.height
    
square = Square(5)
triangle = Triangle(4, 5)

print(triangle.area())
print(square.area())