import os
import sys
import platform
##################
#osn = os.name
#print("The name of your OS is " + osn + ".")
#if osn == "posix": print("You are using a Linux operating system.")
##################
#plat = sys.platform
#print(plat)
#osun = os.uname()
#print(osun)
#bits = platform.architecture()
#print(bits)
##################

#t = os.ctermid()
#print(t)
#u = os.environb
#print(u)

showDir = os.listdir(".")
upPath = os.listdir("..")
upperPath = os.listdir("../..")
rootPath = os.listdir("/")
print("The current path is " + str(showDir) + "\n")
print("The path above this one is " + str(upPath) + "\n")
print("The path above that one is " + str(upperPath) + "\n")
print("The root path is " + str(rootPath) + "\n")



def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
