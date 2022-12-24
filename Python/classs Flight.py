class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[] # list

    def add_passsenger(self,name):
        if not self.open_seats():
            return False
            
        self.passengers.append(name)
        return True

    def open_seats(self):
        return self.capacity-len(self.passengers)


flight=Flight(2)
people=["sukku","janu","chhotu","sristi"]
for person in people:
    success = flight.add_passsenger(person)
    if success:
        print(f"Added {person} to flight successfully")
    else:
        print(f"No available seats for {person}")
