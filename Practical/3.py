class car:
    def __init__(self, make , model, year):
        self.make = make 
        self.model = model
        self.year = year
    
    def print_details(self):
        print(f"car details: {self.make}, {self.model}, {self.year}")
              
car = car('toyota', 'filder', 2020)


car.print_details()
              