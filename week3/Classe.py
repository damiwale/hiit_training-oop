# class NewBrand:
#     def __init__(self):  # Contructor
#         self.__brand = "Pepsi"
        # self.author = "Peace"


# # Initialization
# personBrand = NewBrand()
# print(personBrand.brand)


# class Person:
#     # Class Attributes
#     laptop = "HP"

#     def __init__(self, name, brand, food):  # Contructor
#         # Instance Attributes
#         self.name = name
#         self.brand = brand
#         self.food = food

#     def greeting(self):
#         print(f"Hello, My name is {self.name} Good afternoon")


# personBrand = Person("Peace", "Pepsi", "Beans")
# print(personBrand.brand)
# print(personBrand.food)
# print(personBrand.laptop)


# personBrand.greeting()

# # Principles of OOP
# # 1) Inheritance
# # 2) Polymorphism
# # 3) Encapsulation
# # 4) Abstraction

# # inheritance


# class Father:
#     def __init__(self, accountBalance):
#         self.accountBalance = accountBalance

#     def show_balance(self):
#         print("Father's balance:", self.accountBalance)


# class Son(Father):  # Inheritance
#     pass


# son = Son("$3000")
# son.show_balance()




class AdeDaddy:
    accountBalance = 4000

    def show_father_balance(self):
        print("Father's Balance", AdeDaddy.accountBalance)


class Ade(AdeDaddy):  # Inheritance
    accountBalance = AdeDaddy.accountBalance

    def __init__(self, ownMoney):
        self.ownMoney = Ade.accountBalance + ownMoney
        Ade.accountBalance = self.ownMoney

    def total_money(self):
        print("Total moeny Son has", Ade.accountBalance)


ade = Ade(8000)
ade = Ade(4000)
ade = Ade(4000)
ade.total_money()


class Father:
    def __init__(self, accountBalance):
        self.accountBalance = accountBalance


class Son(Father):
    def __init__(self, accountBalance, pocketMoney):
        super().__init__(accountBalance)  # Call Father

        self.pocketMoney = pocketMoney

    def show_money(self):
        print("Father's balance:", self.accountBalance)
        print("Son's pocket money:", self.pocketMoney)


son1 = Son("$3000", "$200")
son1.show_money()


class Dog:
    def speak(self):
        print("Bark")


class Cat:
    def speak(self):
        print("Meow")


class Cow:
    def speak(self):
        print("Moo")


animals = [Dog(), Cat(), Cow()]

for animal in animals:
    animal.speak()

# Encapsulation: For hiding attributes and methods


class BankAccount:
    def __init__(self, balance):
        # Private:
        self.__balance = balance

    def deposit(self, amount):
        if amount > 0:
            self.__balance = self.__balance + amount

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount

    def get_balance(self):
        return self.__balance


account = BankAccount(1000)
account.withdraw(200)
print(account.get_balance())



from abc import ABC, abstractmethod
# Abstraction

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass


class Dog1(Animal):
    def speak(self):
        print("Bark")


class Cat1(Animal):
    def speak(self):
        print("Meow")


dog1 = Dog1()