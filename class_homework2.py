class Vehicle:
    vehicle_type = "none"
    pass

class Car:
    price = 1000000

    def horse_powers(self):
        horse_powers = 150
        return horse_powers

class Nissan(Vehicle, Car):
    price = 2000000
    vehicle_type = 'Car'

    def horse_powers(self):
        horse_powers = 180
        return horse_powers


nissan = Nissan()
print(nissan.vehicle_type, nissan.price) # переопределил
print(nissan.horse_powers())