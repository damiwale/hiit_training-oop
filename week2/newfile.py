import re #regular expression
a = 10
b = 5

result = a > b
print(result)
result = a < b
print(result)
result = a == b
print(result)
result = a !=b
print(result)
result = a >= b
print(result)
result = a <= b
print(result)

# logical operator
# and or


#input

# ctrol + / to comment out code
# num1 = int(input("Give me first number"))
# num2 = int(input("Give me second number"))
# print(num1 + num2)



name = input("what is your name?")
print("Hello" + name)


name = "Dayo"
age = 18
print(f"His name is {name}, His age is {age} years old")
#multi line
print(f"""
    His name is {name},
    His age is {age} years old
    He is a developer.
    """)


text = "I work with python"

result =re.search("python", text)
print(result.group())

text = "I have 2 apples and 3 oranges"
result = re.search(r"\d", text)
print(result.group())

text = "I have 2 apples and 3 oranges"
result = re.findall(r"\d", text)
print(result)

#logical operator

and or

