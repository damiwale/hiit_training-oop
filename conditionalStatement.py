product = "Shoe"

if product == "Shoe" or product == "Bag":
    print("You will get 10% discount")

age = 18
if age >= 18:
    print("You are an adult")


age = 16
if age >= 18:
    print("You can vote")
else:
    print("You cannot vote")


score = 75
if score >= 70:
    print("Excellent")
elif score >= 50:
    print("Pass")
else:
    print("Fail")


age = 20
has_id = True
if age >= 18 and has_id == True:
    print("Access granted")


age = 20
has_id = True
if age > 18:
    if has_id == True:
        print("Access granted")
    else:
        print("You need an ID")
else:
    print("You are underage")


user_logged_in = True
cart_total = 750
payment_method = "Card"
acceptable_payment_methods = ["Card", "Cash"]


if user_logged_in:
    if cart_total > 0:
        if payment_method in acceptable_payment_methods:
            print("Processing Payment")
        else:
            print("Please get a card or cash")
    else:
        print("Your cart is empty")
else:
    print("Please log in")
