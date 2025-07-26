# Parent class 
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print(f"{self.name} makes a sound.")

    def eat(self):
        print(f"{self.name} is eating.")

# Child class 
class Dog(Animal):
    def speak(self):
        print(f"{self.name} says Woof!")

    def fetch(self):
        print(f"{self.name} is fetching the ball.")

# Child class 
class Cat(Animal):
    def speak(self):
        print(f"{self.name} says Meow!")

    def scratch(self):
        print(f"{self.name} is scratching the sofa.")

# Create objects
dog = Dog("Buddy")
cat = Cat("Whiskers")

# Common methods
dog.eat()
cat.eat()

# Overridden methods
dog.speak()
cat.speak()

# Unique methods
dog.fetch()
cat.scratch()
