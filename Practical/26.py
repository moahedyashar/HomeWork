class Ticket:
    def __init__(self, movie_name, seat_number, price):
        self.movie_name = movie_name
        self.seat_number = seat_number
        self.price = price
    
    def display_details(self):
        print(f"""movie: {self.movie_name},\
        seat: {self.seat_number},\
        price: {self.price}""")

    
    
    def add_discount(self, discount):
        if discount > 0:
            self.price -= self.price * (discount/100)
        else:
            print('invalid discount rate')
ticket = Ticket('interstellar', 35, 500)

print(ticket.price)
