# note = open("note.txt", "r")
# content = note.read()
# note.close()
# print(content)


import os


def create_file():
    """create a new file"""
    if os.path.exists(FILE_NAME):
        print("file already exits.")
    else:
        with open(FILE_NAME, "W") as file:
            file.write("This is a new file created for student records. \n")
            print("file created successfully.")





# "w", "r", "a", "r+"
FILE_NAME = "students.txt"


note = open("note.txt", "a")
note.write("Hi You are welcome to python class, We are treating file operation")
note.close()

note = open("note.txt", "r")
content = note.read()
note.close()
# print(content)


def write_file():
    """write data to file (overwrite existing content)"""
    with open(FILE_NAME, "w") as file









