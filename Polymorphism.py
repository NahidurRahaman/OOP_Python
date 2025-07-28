class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):
        print("Dog says: Woof!")

class Cat(Animal):
    def speak(self):
        print("Cat says: Meow!")

class Cow(Animal):
    def speak(self):
        print("Cow says: Moo!")

# Polymorphism in action
def animal_sound(animal):
    animal.speak()

# Creating objects
animals = [Dog(), Cat(), Cow()]

for a in animals:
    animal_sound(a)
