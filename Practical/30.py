class Hotel:
    def __init__(self, name):
        self.name = name
        self.rooms = []

    def add_room(self, room):
        if isinstance(room, Room):
            self.rooms.append(room)
            print(f"Room {room.room_number} added to the hotel {self.name}.")
        else:
            print("Only objects of type 'Room' can be added to the hotel.")

    def book_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if not room.is_occupied:
                    room.is_occupied = True
                    print(f"Room {room_number} has been booked.")
                else:
                    print(f"Room {room_number} is already occupied.")
                return
        print(f"Room {room_number} not found in the hotel {self.name}.")

    def check_out(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                if room.is_occupied:
                    room.is_occupied = False
                    print(f"Room {room_number} has been checked out.")
                else:
                    print(f"Room {room_number} is already available.")
                return
        print(f"Room {room_number} not found in the hotel {self.name}.")

    def list_rooms(self):
        if self.rooms:
            print(f"Rooms in {self.name}:")
            for room in self.rooms:
                print(room)
        else:
            print(f"There are no rooms in the hotel {self.name}.")
