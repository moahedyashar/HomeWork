class Laptop:
    def __init__(self, brand, model, price):
        self._brand = brand
        self._model = model
        self._price = price 
    
    def apply_discount(self, discount):
        self._price -= self._price * (discount/100)

    def display_details(self):
        return f"details: {self._brand}, {self._model}, {self._price}"
        

laptop = Laptop("DELL", 2020, 10000)
laptop.apply_discount(20)
print(laptop.display_details())