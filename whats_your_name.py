name = raw_input("What is your name?")
print("Your name is " + name + ".")
print("This name has been written to a text file.")

text_file = open("NameTextFile.txt", "w")
text_file.write(name)
text_file.close()