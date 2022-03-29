import os

#cwd = os.getcwd()
#print("Here's the current workding directory:",cwd)

#print("I will create a test folder here:")
#os.mkdir("testFolder/")

#print("I will create testFolder2 and testFolder3 here with permissions.")
#os.makedirs("testFolder2/testFolder3")

print("I will list the contents of the current directory here:")
diros = os.listdir()
print(diros)

print("I will list the contents of the /tmp directory here:")
dirTmp = os.listdir("/home/admkparker/")
print(dirTmp)
