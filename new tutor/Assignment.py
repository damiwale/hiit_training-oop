
'''
QUESTION
Write a program that does grading for scores entered:
1. Ask the user to enter the number of courses
2. Per course ask for course code and scores
3. Display the result of the courses and their course code. E.G CSC 101 - 65 - B , CSC 11 - 70-A etc
NOTE:
A: 70-100
B: 60-69
C: 50-59
D: 45-49
E: 40-44
F: 0-39
'''
#Solution
from module import compute_grade
number_of_courses = int(input("Enter the number of courses you want to grade"))
course_list = []
for i in range(number_of_courses):
    course_code = input(f"Enter the course code {i+1}: ")
    score = int(input(f"Enter the score ${i+1}: "))
    print(" ")
    course_list.append(score)

    course = {"code": course_code, "score": score}
    
    course_list.append(course)

# printing the result
for course in course_list:
    score = course.get("score")
    print(f"{course.get("code")} - {score} - {compute_grade(score)}")



