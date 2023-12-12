# Object- Oriented Programing, Nieko Garnes, v0.0

class Person: # Use PascalCase
    def __init__(self, name, age, weight): 
        self.name = name
        self.age = age
        self.weight = weight

    # To String Function
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weigh} pounds\n"



person1 = Person("George Washington", 13, 255.5)

print(person1)