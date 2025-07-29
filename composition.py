class Engine:
    def start(self):
        return "Engine started"

class Car:
    def __init__(self):
        self.engine = Engine()  # Car has an Engine(composition)

    def drive(self):
        return self.engine.start() + ", Car is driving"

c = Car()
print(c.drive())  # Output: Engine started, Car is driving
