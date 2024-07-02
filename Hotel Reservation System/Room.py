class Room:
    def __init__(self, room_number, room_type):
        self.room_number = room_number
        self.room_type = room_type
        self.is_available = True

    def reserve(self):
        if self.is_available:
            self.is_available = False
            return f'The room {self.room_number} has been booked.'
        else:
            return f'The room {self.room_number} is not available.'

    def cancel_reservations(self):
        if not self.is_available:
            self.is_available = True
            return f'The room {self.room_number} reservation has been canceled.'
        else:
            return f'The room {self.room_number} is available.'

    def __str__(self):
        status = "available" if self.is_available else "not available"
        return f"Room {self.room_number}, Type: {self.room_type}, Status: {status}"

class Hotel:
    def __init__(self):
        self.rooms = []

    def add_room(self, room):
        self.rooms.append(room)
        return f'Added a {room}'

    def check_is_available(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.is_available
        return f'The room {room_number} is not found.'

    def reserve_room(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.reserve()
        return f'The room {room_number} is not found.'

    def cancel_reservations(self, room_number):
        for room in self.rooms:
            if room.room_number == room_number:
                return room.cancel_reservations()
        return f'The room {room_number} is not found.'

hotel = Hotel()
room1 = Room(101, 'Single')
room2 = Room(102, 'Double')

print(hotel.add_room(room1))
print(hotel.add_room(room2))

print(hotel.check_is_available(101))
print(hotel.reserve_room(101))
print(hotel.check_is_available(101))
print(hotel.cancel_reservations(101))
print(hotel.check_is_available(101))
