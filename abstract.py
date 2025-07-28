from abc import ABC, abstractmethod
import math

# Abstract base class
class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

    def description(self):
        return "This is a shape."

# Subclass 1: Rectangle
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

# Subclass 2: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

# Testing the classes
# shape = Shape()  

rectangle = Rectangle(5, 10)
print("Rectangle Area:", rectangle.area())
print(rectangle.description())

circle = Circle(7)
print("Circle Area:", round(circle.area(), 2))
print(circle.description())
