class Vehicle:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def disp_info(self):
        return f"Make: {self.make}, Model: {self.model}"


class Car(Vehicle):

    def __init__(self, make, model, year):
        Vehicle.__init__(self, make, model)

        self.year = year

    def disp_info(self):
        vehicle_info = Vehicle.disp_info(self)

        return f"{vehicle_info}, Year: {self.year}"


car = Car("Hyundai", "Santro", 2015)

print(car.disp_info())