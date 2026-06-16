import os

FILE_NAME = "newstudents.txt"

# CREATE A FILE checked
# UPDATE A FILE checked
# READ A FILE Checked
# DELETE A FILE Checked
# SEARCH FILE CONTENT Checked

def create_file():    
    if os.path.exists(FILE_NAME):
        print("File already exists.")
    else:
        with open(FILE_NAME, "w") as file:
            file.write("Text Content")
            print("File created successfully.")
                

def write_file():    
    with open(FILE_NAME, "w") as file:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        file.write(f"Name: {name}, Age: {age}\n")
    print("Data written successfully.")


def append_file():    
    with open(FILE_NAME, "a") as file:
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        file.write(f"Name: {name}, Age: {age}\n")
    print("Data appended successfully.")


def read_file():    
    if not os.path.exists(FILE_NAME):
        print("File not found.")        
        return 
    else:        
        with open(FILE_NAME, "r") as file:
            content = file.read()
            if content == "":
                print("File is empty.")
            else:
                print("\n--- File Content ---")
                print(content)


def search_file(keyword):    
    if not os.path.exists(FILE_NAME):
        print("File not found.")
        return
    else:
        if keyword.strip() == "":            
            keyword = input("Enter name to search: ")

        found = False
        with open(FILE_NAME, "r") as file:
            for line in file:
                if keyword.lower() in line.lower():
                    print("Found:", line.strip())
                    found = True
        if not found:
            print("Record not found.")


def delete_file():    
    if os.path.exists(FILE_NAME):
        os.remove(FILE_NAME)
        print("File deleted successfully.")
    else:
        print("File does not exist.")

FILE_NAME = "newstudents.txt"

def menu():
    while True:
        print("\n===== FILE HANDLING MENU =====")
        print("1. Create file")
        print("2. Write to file")
        print("3. Append to file")
        print("4. Read file")
        print("5. Search in file")
        print("6. Delete file")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":
            create_file()
        elif choice == "2":
            write_file()
        elif choice == "3":
            append_file()
        elif choice == "4":
            read_file()
        elif choice == "5":
            keyword = input("Enter name to search: ")
            search_file(keyword)
        elif choice == "6":
            delete_file()
        elif choice == "7":
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


# Run the program
# create_file()

# append_file()
# read_file()
# search_file()



menu()