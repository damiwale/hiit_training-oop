#loop >= while and for

#for i in range(500):
 #   print(i)

#print("========")
#print("SPACE")
#print("SPACE")
#print("========")

#for loop

fruits = ["apple", "banana", "mango", "orange"]

for fruit in fruits:
    print(fruit)


for index, fruit in enumerate(fruits):
    fruits[index] = fruit +"s"
print(fruits)


for i in range(70):
    if i == 49:
        continue #to skip
    else:
        print(i)

for i in range(70):
    if i == 49:
        break #to stop
    else:
        print(i)

for i in range(70):
    if i == 49:
        pass #nothing
    else:
        print(i)



#while loop

count = 1
while count <= 5:
    print (count)
    count += 1

#example

fruits = ["apple", "banana", "mango", "orange"]
number_of_fruits = len(fruits)

count = 0
while count < number_of_fruits:
    print(fruits[count])
    count += 1







