# In this python file, you type in your name and it writes it to a text file within the directory.  Raw_input accomplishes this where input does not

name = raw_input("What is your name?")
print("Your name is " + name + ".")
print("This name has been written to a text file.")

text_file = open("NameTextFile.txt", "w")
text_file.write(name)
text_file.close()
