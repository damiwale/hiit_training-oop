
anotherlists = [1, 3, 2, 0, 7, 7, 5, 8, 6, 7]

anotherlists.sort()  # Ascending order
print(anotherlists)

anotherlists.reverse()  # Descending order
print(anotherlists)

totalitemsinthelist = len(anotherlists)
print(totalitemsinthelist)

howmanyTimeIhave7 = anotherlists.count(7)
print(howmanyTimeIhave7)

Is7InTheList = 7 in anotherlists
print(Is7InTheList)

anotherlist1 = anotherlists[1:10]
print(anotherlist1)


newlist = [2, 1, 4, 56, 1, 3, 4, 7, 8, 9]

indexof56 = newlist.index(56)
print(indexof56)

list1 = [1, 2, 3]
list2 = [4, 5, 6]

combinedList = list2 + list1
print(combinedList)
