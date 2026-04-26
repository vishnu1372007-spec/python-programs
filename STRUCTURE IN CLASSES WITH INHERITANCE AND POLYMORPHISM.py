class vehicles:
    def move(self):
        print("vehicles are moves")
class car(Vehicles):
    def drive(self):
        print("drive from one place to another")
class bike(vehicles):
    def ride(self):
        print("bike rides")
c=car()
c.drive()
c.move()
b=bike()
b.drive()
b.ride
