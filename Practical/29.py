class Flight:
    def __init__(self, flight_number, destination):
        self.flight_number = flight_number
        self.destination = destination
        self.passengers = []

    def add_passenger(self, person):
        if isinstance(person, Person):
            self.passengers.append(person)
            print(f"Passenger '{person.name}' added to flight {self.flight_number}.")
        else:
            print("Only objects of type 'Person' can be added as passengers.")

    def remove_passenger(self, passport_number):
        for person in self.passengers:
            if person.passport_number == passport_number:
                self.passengers.remove(person)
                print(f"Passenger '{person.name}' removed from flight {self.flight_number}.")
                return
        print(f"No passenger with passport number '{passport_number}' found on flight {self.flight_number}.")

    def list_passengers(self):
        if self.passengers:
            print(f"Passengers on flight {self.flight_number} to {self.destination}:")
            for person in self.passengers:
                print(f" - {person.name} (Passport: {person.passport_number})")
        else:
            print(f"No passengers on flight {self.flight_number}.")
