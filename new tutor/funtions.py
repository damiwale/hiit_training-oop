
#USE OF FUNCTION
    #Write a program that accepts inputs from the user and performs arithmetic
    # operations using functions:
    #1. create a seperate functions that: add, subtract, multiply, and divide numbers passed to them as parameters and returns the result
    #2. collect two numbers from the user
    #3. use the functions to perform the computation
    #4. Display the result of the operation

#solution


def add(num1, num2):
    return num1 + num2

def multiply(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def subtract(num1, num2):
    return num1 - num2

a = input("Enter a number:")
b = input("Enter another number:")

x = float(a)
y = float(b)

sum_result = add(x, y)
rounded = round(sum_result, 2)
#print(f"The sum is: {sum_result:.3f}")
#print(f"Rounded: {rounded}")
print(f"The sum is: {add(x,y)}")
print(f"The product is: {multiply(x,y)}")
try:
    print(f"The division is: {divide(x,y)}")
   except zeroDivisionError:
    print("cannot divide by zero")
print(f"The difference is:{abs(subtract(x,y))}")

except ValueError:
print("A value error occured")

