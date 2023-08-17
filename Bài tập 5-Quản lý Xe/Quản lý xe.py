class Car:
    def __init__(self, make, model, year, mileage):
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage

    def tang_km(self, miles):
        self.mileage += miles

    def display_info(self):
        print(f"Make: {self.make}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Mileage: {self.mileage}")


car1 = Car("Toyota", "Camry", 2010, 50000)
car1.tang_km(1000)
car1.display_info()

