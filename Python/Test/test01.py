from functools import cmp_to_key

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

def compare_people_by_age(person1, person2):
    if person1.age < person2.age:
        return -1
    elif person1.age > person2.age:
        return 1
    else:
        return 0

people = [
    Person("Alice", 30),
    Person("Bob", 25),
    Person("Charlie", 35)
]

# Using cmp_to_key to convert the comparator function
sorted_people = sorted(people, key=cmp_to_key(compare_people_by_age))

for person in sorted_people:
    print(person.name, person.age)
