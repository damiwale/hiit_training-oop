# talking about methods

class car:

    def __init__(self, name, brand, no_of_tyres):
        self.name = name
        self.brand = brand
        self.no_of_tyres = no_of_tyres

    def accelerate(self):
        print(f"{self.name} is Accelerating.......")


ferrari = car(name="wale's ferrari", brand="Mobile car", no_of_tyres=4)
ferrari_2 = car(name="Samuel's ferrari", brand="Mobile car", no_of_tyres=8)

print(ferrari.name)
print(ferrari_2.name)


