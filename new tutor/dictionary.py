# Dictionary - key - value pairs
'''
table = {"name": "Table 1", "height": "10cm", "width": 25, "color": "red"}

dictionary = {"key": "value"}
# key is a string
# value is any valid data type

color = table.get("color")
#name = table["name"]
print(table)


print("Before adding names")
print(table)
print("")

table["Name 1", "Name 2", "Name 3", "Name 4"]
print("after adding names")
print(table)
'''


#write a python program that initialize a dictionary with the variable name "person" 
#i.e person ={}
#collect the following from a user:
#Name, Age, Weight etc and append it to the initialized disctionary.
# 1. print the Dictionary
# 2. print all the details the user gave from the dictionary E.g
#Your Name is : Samuel
#Your Age is : 13

#Solution
'''
table = {"name": "Table 1", "height": "10cm", "width": 25,}

print(table)
table["color"] = input("Enter the color of the table:")

print(table.get("color"))
'''

#class work

# write a python program that tells auser their grade in a particular course
# 1. collect the course code from the user
# 2. collect the score
# 3. Display the course code, score an the grade i.e CSC 101-65-B
# Note:
# A: 70-100
# B: 60-69
# C: 50-59
# D: 45-49
# E: 40-44
# F:   
#SOLUTION
'''
def get_grade(score):
   if 70 <= score <= 100:
       return 'A'
   elif 60 <= score <= 69:
       return 'B'
   elif 50 <= score <= 59:
       return 'C'
   elif 45 <= score <= 49:
       return 'D'
   elif 40 <= score <= 44:
       return 'E'
   elif 0 <= score <= 39:
       return 'F'
   else:
       return None

course_code = input("csc 101: ").strip().upper()

while True:
   try:
       score = int(input("30 (1-100): "))
       if 0 <= 30 <= 100:
           break
       else:
           print("Score must be between 1 and 100. Try again.")
   except ValueError:
       print("Invalid input. Please enter a number.")

grade = get_grade(score)
print(f"\nResult: {course_code}-{score}-{grade}")
'''
# OR

course_code = input("Enter The course code")
score_str = input("Enter your Score: ")

if score_str.isdigit():
    score = int(score_str)

if score >= 70 and score <= 100:
    print(f"{course_code} - {score} - A")
elif score >= 60 and score <= 69:
    print(f"{course_code} - {score} - B")
elif score >= 50 and score <= 59:
    print(f"{course_code} - {score} - C")
elif score >= 45 and score <= 49:
    print(f"{course_code} - {score} - D")
elif score >= 40 and score <= 44:
    print(f"{course_code} - {score} - E")
elif score >= 0 and score <= 39:
    print(f"{course_code} - {score} - F")
else:
    print("score only ranges from 0 - 100")


print("The score must be a number.....")


