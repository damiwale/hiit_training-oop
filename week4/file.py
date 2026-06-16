file = open("note.txt", "r+")
content = file.read()
print(content)
file.seek(7) #move the file pointer to the begining
file.write("30")
content = file.read()
print(content)
file.close()





