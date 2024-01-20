class Car:
    # Constructor method (initializer)
    def __init__(self, year, make, model):
        # Instance attributes
        self.year = year
        self.make = make
        self.model = model

    # Instance method
    def check_model(self):
        print(f"{self.year} {self.make} {self.model}")

# Creating an instance of the Car class
my_car = Car(year = 1999, make="Toyota", model="Camry")

# Accessing attributes and calling methods
print(f"Year: {my_car.year}")
print(f"Make: {my_car.make}")
print(f"Model: {my_car.model}")
my_car.check_model()