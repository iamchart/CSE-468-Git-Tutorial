class Person:
    def __init__(self, name, age, cars):
        self.name = name
        self.age = age
        self.cars = cars

    def __str__(self):
        return f"{self.name} ({self.age}) - Has {self.cars} car{'s' if self.cars != 1 else ''}"

class Pilot(Person):
    def __init__(self, name, age, cars, license_no, flight_hours):
        super().__init__(name, age, cars)
        self.license_no = license_no
        self.flight_hours = flight_hours
    
    def __str__(self):
        return f"{self.name} ({self.age}) [License No. {self.license_no}] has {self.flight_hours} hours of flight"
