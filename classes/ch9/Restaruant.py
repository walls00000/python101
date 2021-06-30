class Restaurant:
    """A restaurant """

    def __init__(self, restaurant_name, cuisine_type):
        """Initialize name and type"""
        self.name = restaurant_name
        self.cuisine = cuisine_type

    def describe(self):
        print(f"{self.name} is a {self.cuisine} cuisine. ")

    def open(self):
        print(f"{self.name} is open")



my_restaurant = Restaurant("Chipotle", "Mexican")
my_restaurant.describe()
my_restaurant.open()

my_restaurant = Restaurant("Olive Garden", "Italian")
my_restaurant.describe()
my_restaurant.open()