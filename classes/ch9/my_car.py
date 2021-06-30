import car
import electric_car

my_new_car = car.Car("audi", "a4", 2019)
print(my_new_car.get_descriptive_name())

my_new_car.odometer_reading = 23
my_new_car.read_odometer()

ecar = electric_car.ElectricCar("prius", "e", 2011)
print(ecar.get_descriptive_name())

bt = electric_car.Battery(99)
bt.describe_battery()



