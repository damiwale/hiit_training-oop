# methods
# Methods are functions inside classes or behaviours that an object have
class car:
   
    def __init__(self, color, brand, max_speed, manufacturing_year):
        self.color = color
        self.brand = brand
        self.max_speed = max_speed
        self.manufacturing_year = manufacturing_year

    def print_properties(self):
        print(f"color: {self.color}")
        print(f"brand: {self.brand}")
        print(f"max_speed: {self.max_speed}")
        print(f"manufacturing year: {self.manufacturing_year}")
    
    def print_color(self):
        print(f"color: {self.color}")


my_car1 = car(color="Blue", brand="Toyota", max_speed= "180 km/hr", manufacturing_year= 2021)
my_car2 = car(color="Red", brand="Korope", max_speed= "120 km/hr", manufacturing_year= 1997)

#my_car1.print_properties()
#my_car2.print_properties()
my_car1.print_color()
my_car2.print_color()
