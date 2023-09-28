class Gaadi:

    def __init__(self, make, model):
        self.make = make
        self.model = model

    def disp_info(self):
        return f"Make: {self.make}, Model: {self.model}"


class Car(Gaadi):

    def __init__(self, make, model, year):
        super().__init__(make, model)

        self.year = year

    def disp_info(self):
        vehicle_info = super().disp_info()

        return f"{vehicle_info}, Year: {self.year}"


car = Car("Hyundai", "Santro", 2015)

print(car.disp_info())