1. Inheritance

Inheritance allows you to create a new class based on an existing class. The new class (child class) inherits attributes and methods from the parent class.

The child class can also add its own attributes and methods or override methods from the parent class.


Example:

class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound")

class Dog(Animal):
    def speak(self):
        print(f"{self.name} barks")

my_dog = Dog("Buddy")
my_dog.speak()  # Output: Buddy barks
