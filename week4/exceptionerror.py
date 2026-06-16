def append_file():
    try:
        age = int(input("Enter student age:"))
        print(age)
    except ValueError:
        print("Age must be a number.")
    except Exception as e:
        print("Error:", e)


append_file()


def dividebyzero():
    try:
        x = int(input("Enter number: "))
        return 10 / x
    except Exception as e:
        print("An error occurred")

# result = dividedbyzero()
# print("Result:", result)


 #try:
    file = open("data.txt", "r")
    











