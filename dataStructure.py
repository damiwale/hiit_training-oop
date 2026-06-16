# List
fruits = ["apple", "banana", "orange"]
# print("Fruits:", fruits)
# Find Item based on position(index)

item = fruits[2] #Read
print(item)

# Modifying Editing
fruits[2] = "mongo"

# Add new item to list
fruits.append("Carrot")

fruits.insert(3, "Melon")
print(fruits) #Update


fruits.remove("Carrot")
print("Updated Fruits:", fruits)

fruits.pop(3)
print("Updated Fruits:", fruits)



lastItem = fruits[-2]
print(lastItem)
# print("Last fruit:", fruits[-1])

anotherLists = [1, 3, 2, 0, 5, 8, 6, 7]
anotherLists.sort()  # Ascending Order
print(anotherLists)
anotherLists.reverse()  # Descending Order
print(anotherLists)


# Dictionary
# Key: Value
student = {
    "name": "Kelvin",
    "age": 10,
}

suppliers = {
    "Ade": 20,
    "Bimbo": 40,
    "Shola": 50
}

print(suppliers)

AdeBags = suppliers["Ade"]
print(AdeBags)


f"Number of Ade's Bag is {AdeBags} If it is enough we can supply him more"

print(f"""Number of Ade's Bag is 
      {AdeBags} If it is enough we can supply him more""" )

suppliers["Ade"] = 40
suppliers["Ade"] = suppliers["Ade"] + 50

print(suppliers)


# Tuple

newTuple = (1, 2, 4)
# Access tuple
Tuple2 = newTuple[1]

print(Tuple2)


# Sets
# Has no duplicate
newSet1 = {1, 2, 3, 4, 5}
newSet2 = {2, 3, 4, 7, 9}

# Union
# Intersection
# Difference

unionSet = newSet1.union(newSet2)
print(unionSet)
intersectionSet = newSet1.intersection(newSet2)
print(intersectionSet)

differenceSet = newSet1.difference(newSet2)
print(differenceSet)



