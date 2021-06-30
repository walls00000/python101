import car

class Battery:
    """A simple attempt to model a battery for an electric car"""

    def __init__(self, battery_size=75):
        """Initialize the battery's attributes"""
        self.battery_size = battery_size

    def describe_battery(self):
        """Print a statement describing the battery size."""
        print(f"The battery is a {self.battery_size}-kwh battery")

class ElectricCar(car.Car):
    """Represents an electric Car"""

    def __init__(self, make, model, year):
        """Initialize attibutes of the parent Car class"""
        super().__init__(make, model, year)
        self.battery = Battery()

    def describe_battery(self):
        """Print a statement describing the battery"""
        # TODO: Fix attribute not found exception!!!
        print(f"This car has a {self.battery.battery_size} battery")

    def fill_gas_tank(self):
        """Electric cars don't have a gas tank"""
        print("This car doesn't have a gas tank!")