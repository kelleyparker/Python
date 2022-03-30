#!/usr/bin/python
#!C:\Users\cliffgoat\AppData\Local\Programs\Python\Python310\python.exe

import os
import platform

cwd = os.getcwd()
print("Here's the current workding directory:",cwd)

#print("I will create a test folder here:")
#os.mkdir("testFolder/")

#print("I will create testFolder2 and testFolder3 here with permissions.")
#os.makedirs("testFolder2/testFolder3")

#print("I will list the contents of the current directory here:")
#diros = os.listdir()
#print(diros)

#print("I will list the contents of the /tmp directory here:")
#dirTmp = os.listdir("/home/admkparker/")
#print(dirTmp)

#d = input("What's the desired Linux path you want me to check?")
#lstat = os.lstat(d)
#print(lstat)

#cwd = os.getcwd()
#print("Here's the current workding directory:",cwd)

#f = input("To which directory do you want to change?")
#os.chdir("/home/kparker")
#print("You are now in the current directory:")
#f = os.getcwd()
#print(f)

######################################################
### Running ls commands on linux current directory ###
######################################################


### List current working directory in long-listing format
#cmd = 'ls -l'
#os.system(cmd)

### Fdisk listing 
#cmdfdisk = 'sudo fdisk -l'
#os.system(cmdfdisk)

######################################################
######################################################
######################################################

### What OS I'm using 
#myos = platform.system()
#print(myos)

### The release I'm using
#myRel = platform.release()
#print(myRel)

### The platform I'm using
#myPlat = platform.platform()
#print(myPlat)

### The version I'm using
#myVer = platform.version()
#print(myVer)
