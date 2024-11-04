from test_class import Person
import random

for i in range(10):
    person = Person(f'Person {i+1}', random.randrange(13, 79), random.randrange(0, 10))
    print(person)