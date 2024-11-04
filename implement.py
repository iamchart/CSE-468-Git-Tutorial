from test_class import Person, Pilot
import random

# for i in range(10):
#     person = Person(f'Person {i+1}', random.randrange(13, 79), random.randrange(0, 10))
#     print(person)

person1 = Person("Alice", 30, 2)
person2 = Person("Bob", 25, 1)
pilot1 = Pilot("Charlie", 40, 1, "XY123", 2000)
pilot2 = Pilot("Dana", 34, 0, "YZ456", 3500)

arr = [person1, person2, pilot1, pilot2]

for i in arr:
    print(i)