def append_file():
    try:        
        age = int(input("Enter student age: "))    
        print(age)        
    except ValueError:
        print("Age must be a number.")
    except Exception as e:
        print("Error:", e)
        
        
append_file()  
