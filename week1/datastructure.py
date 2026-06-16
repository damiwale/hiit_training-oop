
#list
fruits = ["apple", "banana", "orange"]
# print("fruits:", fruits)
# find item based on position (index)

item = fruits[2] #read
print(item)

# modifying Editing
fruits[2] = "Mango"

# Add new item to list
fruits.append("carrot")

fruits.insert(3, "Melon")
print(fruits) #update


fruits.remove("carrot")
print("updated fruits:", fruits)

fruits.pop(3)
print("updated fruits:", fruits)



lastitem = fruits[-2]
print(lastitem)
# print("last fruit:", fruits[-1])

anotherlists = [1, 3, 2, 0, 5, 8, 6, 7,]
anotherlists.sort() # Ascending order
print(anotherlists)
anotherlists.reverse()  # Descending order
print(anotherlists)


# Dictionary
# key: Value
student = {
   "name": "kelvin",
   "age": 10,
}
