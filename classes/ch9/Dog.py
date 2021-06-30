class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes. """
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command. """
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

# myDog = Dog("Leo", 11)
# myDog.sit()
# myDog.roll_over()
# print(f"My dog's name is {myDog.name}")
# print(f"My dog's age is {myDog.age}")


names = [ "leo", "meatball", "barksalot", "sparkie", "slick" ]
age=3
for name in names:
    myDog = Dog(name,age)
    age = age + 1
    myDog.sit()
    myDog.roll_over()
    print(f"My dog's name is {myDog.name}")
    print(f"My dog's age is {myDog.age}")


