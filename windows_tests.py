#!"C:\Users\cliffgoat\AppData\Local\Programs\Python\Python310\python.exe"

import os
import platform

### This line of code prints "howdy!" ###
print("howdy")

### Get current directory on Windows
dir = os.getcwd()
print(dir)

### Use powershell to echo hello as test
os.system("powershell.exe echo hello!")

### Use powershell to get registered user on computer
os.system("powershell.exe Get-ComputerInfo -Property OSRegisteredUser")

### List disks on computer on powershell
os.system("powershell.exe get-disk")