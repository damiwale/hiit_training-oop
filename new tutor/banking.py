# Simple Banking Application

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
