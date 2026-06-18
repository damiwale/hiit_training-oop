
class student:
    def __init__(self, first_name, last_name, dept, age, sex):
        self.first_name = first_name
        self.last_name = last_name
        self.dept = dept
        self.age = age
        self.sex = sex
    def print_full_name(self):
        print(f"first_name: {self.first_name} last_name: {self.last_name}")


student1 = student(first_name ="Olawale", last_name = "David", dept = "Accounting", age = "20", sex = "Male")

#print(student1.first_name)
#print(student1.last_name)
#print(student1.dept)
#print(student1.age)
#print(student1.sex)

student1.print_full_name()
    
        





