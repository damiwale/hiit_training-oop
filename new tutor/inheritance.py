

class Animal:
    def __init__(self, name, no_of_legs):
        self.name = name
        self.no_of_legs = no_of_legs
#inheritance

class Dog(Animal):
    pass

my_dog = Dog(name="Tig", no_of_legs=4)
    
print(my_dog.no_of_legs)

