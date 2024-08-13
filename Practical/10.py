class Bird:
    def fly(self):
        pass

class Eagle(Bird):
    def fly(self):
        return "eagles are flying"
    
class Penguin(Bird):
    def fly(self):
        return "penguins can't fly"
    
eagle = Eagle()
penguin = Penguin()

print(penguin.fly())
        