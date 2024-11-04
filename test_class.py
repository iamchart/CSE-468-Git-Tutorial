class Person:
    def __init__(self, name, age, cars):
        self.name = name
        self.age = age
        self.cars = cars

    def __str__(self):
        return f"{self.name} ({self.age}) - Has {self.cars} car{'s' if self.cars != 1 else ''}"
