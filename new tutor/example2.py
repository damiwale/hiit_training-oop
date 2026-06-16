#write a python program that asks the user for two numbers and:
#1. Decide if one is greater than the other and which one is greater Or
#2. Decides if they are equal
#3. print the result

#num_1 = input("enter a number:")
#num_2 = input("enter another number:")

#if num_1 > num_2:
#    print(f"{num_1} is greater than {num_2}")
#elif num_2 >num_1:
#    print(f"{num_2} is greater than {num_1}")
#else:
  #  print(f"{num_1} is equal {num_2}")

#another way

num_1 = input("enter a number: ")
num_2 = input("enter another number: ")

if num_1.isdigit() and num_2.isdigit():
    conv_num1 = int(num_1)
    conv_num2 = int(num_2)

    if conv_num1 > conv_num2:
        print(f"{conv_num1} is greater")
    elif conv_num1 < conv_num2:
        print(f"{conv_num2} is greater")
    else:
        print(f"the numbers are equal")
else:
         print("Only Numbers are required")
    
         


