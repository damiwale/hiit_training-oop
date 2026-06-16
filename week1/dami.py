newlist = [3,5,2,7,8,9,8,6,4,1]
item = newlist[0]
print(item)

profile ={"name": "Bola","age": 24,"city":"Lagos"}
keyvalue = profile["age"]
print(keyvalue)


newlist[3] = 10
print(newlist)

profile["name"] = "Edward"

print(profile)


newlist.pop(3)
print(newlist)


profile.pop("age")
print(profile)

newlist.append(13) 