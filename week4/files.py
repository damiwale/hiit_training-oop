file = open("note.txt", "r+")
content = file.read()
print(content)
file.seek(7)  # Move the file pointer to the beginning
file.write("70")
content = file.read()
print(content)
file.close()