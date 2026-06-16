product = "shoe"

if product =="shoe" or product =="bag"
    print("you will get 10% discount")

age = 18

if age >=18:
    print("you are an adult")


age = 16
if age >= 18:
    print("you can vote")
else:
    print("you cannot vote")


score = 75 
if score >= 70:
    print("excellent")
elif score >= 50:
    print("pass")
else:
    print("fail")

age = 20
has_id =True
if age >=18 and has_id == True:
    print("Access granted")



age = 20
has_id =True
if age > 18:
    if has_id == True:
        print("access granted") #nested condition
    else:
        print("You need an ID")
else:
    print("You are underage")

    #multi level condition

user_logged_in = True
cart_total = 750
payment_method = "card"
acceptable_payment_methods = ("card", "cash")


if not user_logged_in:
    if cart_total > 0:
        if payment_method in acceptable_payment_methods:
            print("processing payment")
        else:
            print("please get a card")
    else:
        print("Your cart is empty")
else:
    print("please log in")









