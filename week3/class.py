# class newbrand
#   def_init_(self):  # contructor
#       self.brand = "pepsi"
#       self.author


# initialization
# personBrand = NewBrand()
# print(personBrand.brand)


# class person:
#  class attributes
#   laptop = "HP"

# def__init__(self, name, brand, food):   #contructor
#   instance attributes
#   self.name = name
#   self.brand = brand
#   self.food = food

#   def greeting(self)
#       print(f"Hello, My name is {self.name} good afternoon)


# personbrand = person("peace", "pepsi")
# print(personBrand.brand)
# print(personBrand.food)
# print(personBrand.laptop)


# personBrand.greeting()

# principles of oop
# 1) Inheritance
# 2) polymorphism
# 3) Encapsulation
# 4) Abtraction

# # Inheritance


# class father:
#   def__init__(self, accountBalance):
#       self.accountBalance = accountBalance

#   def show_balance(self):
#       print("father's balance:", self.accountBalance)


# class son(father): # Inheritance
#   pass


# son = son("$3000")
# son.show_balance()





class AdeDaddy:
    accountBalance = 4000

    def show_father_balance(self):
        print("father's Balance", AdeDaddy.accountBalance)


class Ade(AdeDaddy):     # Inheritance
    accountBalance = AdeDaddy.accountBalance
























