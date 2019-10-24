class Vehicle(object):
    def __init__(self, colour, max_speed):
        self.colour = colour
        self.max_speed = max_speed


class Motorbike(Vehicle):
    def __init__(self, colour, max_speed, weight, license_plate):
        Vehicle.__init__(self, colour, max_speed)
        self.weight = weight
        self.license_plate = license_plate


class Car(Vehicle):
    def __init__(self, colour, max_speed, year, model):
        Vehicle.__init__(self, colour, max_speed)
        self.year = year
        self.model = model

    @staticmethod
    def wheel_number():
        return 4


class Bicycle(Vehicle):
    def __init__(self, colour, max_speed, model_number):
        Vehicle.__init__(self, colour, max_speed)
        self.model_number = model_number
