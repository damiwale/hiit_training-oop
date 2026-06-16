# note = open("note.txt", "r")
# content = note.read()
# note.close()
# print(content)


import os


def create_file():
    """Create a new file"""
    if os.path.exists(FILE_NAME):
        print("File already exists.")
    else:
        with open(FILE_NAME, "w") as file:
            file.write("This is a new file created for student records.\n")
            print("File created successfully.")
            
            
            


# "w", "r", "a", "r+"
FILE_NAME = "students.txt"


note = open("note.txt", "a")
note.write("Hi You are welcome to python class, We are treating file operations in python")
note.close()

note = open("note.txt", "r")
content = note.read()
note.close()
# print(content)


def write_file():
    """Write data to file (overwrite existing content)"""
    with open(FILE_NAME, "w") as file:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        file.write(f"Name: {name}, Age: {age}\n")
    print("Data written successfully.")
    
write_file()

def append_file():
    """Add data to file without deleting old content"""
    with open(FILE_NAME, "a") as file:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        file.write(f"Name: {name}, Age: {age}\n")
    print("Data appended successfully.")

append_file()


def read_file():
    print("Reading file content...")
    """Read file content"""
    if not os.path.exists(FILE_NAME):
        print("File not found.")
        return

    with open("students.txt", "r") as file:
        content = file.read()
        if content == "":
            print("File is empty.")
        else:
            print("\n--- File Content ---")
            print(content)


read_file()


def search_file():    
    if not os.path.exists(FILE_NAME):
        print("File not found.")
        return

    keyword = input("Enter name to search: ")

    found = False
    with open(FILE_NAME, "r") as file:
        for line in file:
            if keyword.lower() in line.lower():
                print("Found:", line.strip())
                found = True

    if not found:
        print("Record not found.")
        
search_file()

def delete_file():
    """Delete the file"""
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("File deleted successfully.")
    else:
        print("File does not exist.")
        
# delete_file()