file = open("sample.txt", "w")
file.write("Hello, this is the first line in the file.\n")
file.write("File handling in Python is easy to learn.\n")
file.close()
print("Data written successfully.\n")
  
  

file=open("sample.txt","r")
print("Reading file contents:")
content=file.read()  
print(content)
file.close()



file=open("sample.txt","a")
file.write("This line is added using append mode in basic file operations.\n")
file.close()
print("Data is appended succesfully.\n")




file=open("sample.txt","r")
print("The updated content in the file is:")
print(file.read())
file.close()
