"""A class that can be  used to represent a car"""

class Car:
    """A simple attempt to represent a car"""
    def __init__(self, make, model, year):
        """Initialize attributes to describe a car"""
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        """Return  a neatly formatted descriptive name."""
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        """Print a statement showing the car's mileage"""
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        """Set the odometer reading to the given value"""
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer")

    def increment_odometer(self, miles):
        """Add the given amount to the odometer reading"""
        self.odometer_reading += miles
        print(f"Odomerter has been incremented to {self.odometer_reading}")

    def fill_gas_tank(self):
        """Fill the gas tank"""
        print("glug glug glug glug . . . . slurp")




# my_tesla = ElectricCar("tesla", "model s", 2021)
# print(my_tesla.get_descriptive_name())
# my_tesla.describe_battery()
# my_tesla.fill_gas_tank()
# my_tesla.describe_battery()
# print(f"My tesla has a battery of {my_tesla.battery.battery_size} kwh")
#
# my_new_car = Car("audi", "a4", 2019)
# print(my_new_car.get_descriptive_name())
# my_new_car.fill_gas_tank()
# my_new_car.read_odometer()
# my_new_car.update_odometer(23000)
# for i in range(10):
#     my_new_car.increment_odometer(15)
#
# my_new_car.update_odometer(232344)
# my_new_car.read_odometer()




# my_old_car = Car("ford", "Modle T", 1940)
# print(my_new_car.get_descriptive_name())