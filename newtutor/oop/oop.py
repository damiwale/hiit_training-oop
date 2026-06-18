'''
class traiangle:
    def __int__(self,a,b,c,) -> None:
        self.a = a
        self.b = b
        self.c = c
'''
'''
class Rectangle:
    color = "red" # creating an attribute inside the class itself
    def __init__(self, length, breath):
        self.length = length # creating it inside method
        self.breath = breath
        self.color = color

    
obj1 = Rectangle(length=30, breath=60)


print(obj1.length)    
'''
'''
class Vehicle:
    running = False

    def __init__(self, owner):
        self.owner = owner

        def is_running(self):
            if self.running:
                print(f"{self.owner}'s vehicle car is running")

            else:
                print(f"{self.owner}'s vehicle car is not running")

v1 = Vehicle(owner="Divine Favour")

#print(v1.running)
print(v1.owner)
'''

class car:
   
    def __init__(self, color, brand, max_speed, manufacturing_year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.manufacturing_year = manufacturing_year


my_car1 = car(color="Blue", brand="Toyota", max_speed= "180 km/hr", manufacturing_year= 2021)
my_car2 = car(color="purple", brand="Lexus", max_speed= "200 km/hr", manufacturing_year= 2015)
my_car2.color ="white"
my_car3 = car(color="pink", brand="Toyota", max_speed= "250 km/hr", manufacturing_year= 2026)

print(my_car1.color)
print(my_car1.brand)
print(my_car1.max_speed)
print(my_car1.manufacturing_year)
print("........")

print(my_car2.color)
print(my_car2.brand)
print(my_car2.max_speed)
print(my_car2.manufacturing_year)
print(".........")

print(my_car3.color)
print(my_car3.brand)
print(my_car3.max_speed)
print(my_car3.manufacturing_year)



