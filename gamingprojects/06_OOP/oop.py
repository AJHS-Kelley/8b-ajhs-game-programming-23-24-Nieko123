# Object- Oriented Programing, Nieko Garnes, v0.1

class Person: # Use PascalCase
    def __init__(self, name, age, weight): 
        self.name = name
        self.age = age
        self.weight = weight
        self.weakness = None
        self.nemesis = None

    # To String Function
    def __str__(self):
        return f"Name: {self.name}\nThis person is {self.age} years old.\nThey weigh {self.weight} pounds\n"

    def classFunction():
        print("This is an example class function.\n")
        print("It only works when called on an object of that class.")

person1 = Person("George Washington", 45, 255.5)
person2 = Person("John F Kennedy", 52, 167.5)
# print(person1)
# print(person2)

# if person1_weight > person2.weight:
#     print(f"{person1.name} weighs more than {person2.name}.")
# elif person1.weight == person2.weight:
#     print("Each person weighs the same.\n")
# else:
#     print(f"{person2.name} weighs more than {person1.name}.")

# person1.classFunction()

# Changing Properties after creation
print(person1.name)
person1.name = "George Washington"
print(person1.name)

# Deleting Properties -- Danger
# This is does not 'reset' a property, it deletes
print(person1.name)
del person1.name
# print(person1)

# Dleting Objects -- Delete them
del person1

# Adding Properties to objects
person2.weakness = "Kryptonite"
print(person2)
print(person2.weakness)

