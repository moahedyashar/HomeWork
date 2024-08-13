class Rectangle:
    def __init__(self, width, length):
        self.width = width
        self.length = length

    def compute_area(self):
        return self.width * self.length
    
    def compute_peimeter(self):
        return 2 * (self.width + self.length)
    
rectangle = Rectangle(3, 5)

print(f'area: {rectangle.compute_area()}')
print(f'perimeter: {rectangle.compute_peimeter()}' )