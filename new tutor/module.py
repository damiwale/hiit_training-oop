
def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def subtract(num1, num2):
    return num1 - num2

my_name = "OLUMUREWA Olawale"

def compute_grade(score):
    if 70 <= score <= 100:
       return 'A'
   elif 60 <= score <= 69:
       return 'B'
   elif 50 <= score <= 59:
       return "C"
   elif 45 <= score <= 49:
       return 'D'
   elif 40 <= score <= 44:
       return 'E'
   elif 0 <= score <= 39:
       return 'F'
   else:
       return "invalid Score"

