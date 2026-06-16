from module import add, subtract, divide, multiply, my_name

try:
    a = float(input("Enter a number:"))
    b = float(input("Enter another number:"))
    
    print(f"The sum is:{add(a,b)}")

except ValueError:
    print("Error occured with values entered")

