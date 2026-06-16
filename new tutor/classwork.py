# write a program that allows the user to perform basic banking options e.eg
# select an option:
# 1. for balance
# 2. for recharge
# 3. for transfaer
# it ask the user to if they want to perform another transaction after completing one
# there should be a default at the start of the transaction that gets deducted as transaction is performed

# SOLUTION
# Simple Banking Application
'''
balance = 50000  # Default account balance

while True:
    print("\n===== BANKING MENU =====")
    print("1. Check Balance")
    print("2. Recharge")
    print("3. Transfer")
    print("4. Exit")

    option = input("Select an option (1-4): ")

    if option == "1":
        print(f"Your current balance is: ₦{balance}")

    elif option == "2":
        amount = float(input("Enter recharge amount: ₦"))

        if amount <= balance:
            balance -= amount
            print(f"Recharge successful!")
            print(f"Amount Recharged: ₦{amount}")
            print(f"Remaining Balance: ₦{balance}")
        else:
            print("Insufficient balance!")

    elif option == "3":
        amount = float(input("Enter transfer amount: ₦"))

        if amount <= balance:
            recipient = input("Enter recipient account number: ")
            balance -= amount
            print(f"Transfer of ₦{amount} to {recipient} successful!")
            print(f"Remaining Balance: ₦{balance}")
        else:
            print("Insufficient balance!")

    elif option == "4":
        print("Thank you for banking with us.")
        break

    else:
        print("Invalid option selected!")

    another = input("\nDo you want to perform another transaction? (yes/no): ").lower()

    if another != "yes":
        print("Thank you for banking with us.")
        break
    ''' 


#ANOTHER SOLUTION

balance = 50000
another_transaction = True

while another_transaction:
    print("Welcome to py Banking......")
    print("----------------")
    print("1. for. balance")
    print("2 for recharge")
    print("3 for transfer")
    op_code = input(": ")

    if op_code == "1":
        print(f"Your Balance is: {balance}")
    # perform recharge
    elif op_code == "2":
        phone_number = input("Enter The phone number: ")
        amount = input("Enter The Recharge amount: ")
        balance = balance - int(amount)
        print("Recharge successful")
# for Transfer
    elif op_code == "3":
        account_number = input("Enter account number: ")
        amount = float(input("Enter transfer amount: ₦"))

        if amount <= balance:
            balance -= amount
            print("Transfer successful")
            print(f"Remaining Balance: ₦{balance}")
        else:
            print("Insufficient balance")

    else:
        print("Invalid option")

another = input("Do you want to perform another transaction?\n 1 - Yes \n 2- No")
if another == "1":
     another_transaction = True
else:
    another_transaction = False



