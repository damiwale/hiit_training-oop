
# Base on your understanding of oop-object oriented programming in python so far:
# Write a program that allows 5 people to enter their ages. it should have the following methods

# 1. A method to display each person's details e.g: full name: Esther Ade, Age: 14, category: underage
# 2. A method that displays only the person's age
# Note: After collecting these details from the persons as stated above. Display the detail for all of them
# Underage: <18

# Solution

'''
class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

    def get_category(self):
        if self.age < 18:
            return "Underage"
        else:
            return "Adult"

    def display_details(self):
        print(f"Full Name: {self.full_name}, Age: {self.age}, Category: {self.get_category()}")

    def display_age(self):
        print(f"Age: {self.age}")


# List to store all persons
people = []

# Collect details for 5 people
for i in range(5):
    print(f"\nEnter details for Person {i + 1}")
    full_name = input("Enter full name: ")
    age = int(input("Enter age: "))

    person = Person(full_name, age)
    people.append(person)

# Display details for all persons
print("\n--- PERSON DETAILS ---")
for person in people:
    person.display_details()

# Display only ages
print("\n--- PERSON AGES ---")
for person in people:
    person.display_age()
'''

# Another Solution

class Person:
    def __init__(self, full_name, age):
        self.full_name = full_name
        self.age = age

        if self.age >= 18:
            self.category = "Adult"
        else:
            self.category = "Underage"

 
    def get_details(self):
        print(f"full_name: {self.full_name}")
        print(f"Age: {self.age}")
        print(f"category: {self.category}")

    def get_age(self):
         print(f"age: {self.age}")

number_of_people = 5

persons = []
for i in range(number_of_people):
     full_name = input("Enter your full name: ")
     age  = int(input("Enter your age: "))

     person = Person(full_name, age)

# add person to the list
     persons.append(person)

for person in persons:
     print(f"................")
     person.get_details()

# create a class person and let them inherit