'''
def greet():
    print("Hello, Everyone!")

    greet()

'''
'''
def greet(Favour):
    print(f"Hello, {Favour}")

greet("Favour")
greet("Ade")
greet("Sandra")
'''
'''
def add(a, b, c):
    print(a + b  c)

add(12, 5, 10)
'''
'''
def division(a, b):
    return a / b
    
result = division(12, 4)
print(result)

'''
'''
def greet(name="Anonymous User"):
    print(f"Hello, {name}")

greet() 
greet("David") 
'''
'''
def company(name, branch):
    print(name, branch)

company(branch="ikeja", name="HIIT")
'''

'''
def local_greet():
    name = "Adebayo"
    print(f"Hello, {name}")

local_greet()
'''
'''
def add2(a=0, b=0, c=0, d=0):
    print("f")
'''


    #USE OF FUNCTION
    #Write a program that accepts inputs from the user and performs arithmetic
    # operations using functions:
    #1. create a seperate functions that: add, subtract, multiply, and divide numbers passed to them as parameters and returns the result
    #2. collect two numbers from the user
    #3. use the functions to perform the computation
    #4. Display the result of the operation

def add(num1, num2):
    return num1 + num2

def multipl(num1, num2):
    return num1 * num2

def divide(num1, num2):
    return num1 / num2

def subtract(num1, num2):
    return num1 - num2

a = input("Enter a number:")
b = input("Enter another number:")

a_int = int(a)
b_int =int(b)

sum_result = add(num1=5, num2=10)
print(f"The sum is: {sum_result}")



#solution
'''
def add(a, b):
    """Return the sum of a and b."""
    return a + b

def subtract(a, b):
    """Return the difference of a and b."""
    return a - b

def multiply(a, b):
    """Return the product of a and b."""
    return a * b

def divide(a, b):
    """Return the quotient of a divided by b.
    Raises ValueError if b is zero."""
    if b == 0:
        raise ValueError("Division by zero is not allowed.")
    return a / b


# ── 2. Collect two numbers from the user ─────

def get_number(prompt):
    """Repeatedly ask until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("  ⚠  Please enter a valid number.\n")


# ── 3 & 4. Main program ───────────────────────

def main():
    print("=" * 40)
    print("       ARITHMETIC CALCULATOR")
    print("=" * 40)

    # Collect inputs
    num1 = get_number("Enter the first number : ")
    num2 = get_number("Enter the second number: ")

    # ── 3. Use functions to perform computations ──
    results = {
        "Addition      (+)": add(num1, num2),
        "Subtraction   (-)": subtract(num1, num2),
        "Multiplication(×)": multiply(num1, num2),
    }

    # Division is handled separately because it can fail
    try:
        results["Division      (÷)"] = divide(num1, num2)
    except ValueError as e:
        results["Division      (÷)"] = f"Error – {e}"

    # ── 4. Display results ────────────────────────
    print("\n" + "-" * 40)
    print(f"  Results for  {num1}  and  {num2}")
    print("-" * 40)

    for operation, result in results.items():
        if isinstance(result, float):
            # Show whole numbers without a decimal point
            formatted = int(result) if result == int(result) else result
            print(f"  {operation} = {formatted}")
        else:
            print(f"  {operation} = {result}")   # error string

    print("=" * 40)


if __name__ == "__main__":
    main()
'''
