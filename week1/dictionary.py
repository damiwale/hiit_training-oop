
student ={"name": "wale", "age": 15}
studentcopy = student.copy() #to keep a copy
# print(student["name"])

# print(student.get("name"))

student["address"] = "36,Adebayo Road, Ikeja"

print(student)

student["name"] = "paul" #to add names

print(student)


name = student.get("name")
print(name)

keys = student.keys() #to show the keys in the dictS
print("keys", keys)

Values = student.values() #to show the value in a dists
print("Values", Values)

items = student.items()
print("items", items)


student.pop("age") #to remove items in the dic

del student["address"] #to delete items in the dict

print(student)
student.clear() # to claer all the items in the dict
print(student)

print(studentcopy)


text = "preference "

print(text[0])
print(text[1:3])


print(len(text)) #to count the number of items in the list

print(text.upper())
print(text.lower())
print(text.capitalize())

text = text.strip()
#text = text.rstrip()
#text = text.lstrip()


print("length", len(text))


text1 = " preference is the key to success "
print("length", len(text1))
text1 = text1.lstrip()
print("length", len(text1))
text1 = text1.rstrip()
print("length", len(text1))

#to replace
text1 = text1.replace("preference","smart move")
print(text1)

