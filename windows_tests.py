#!"C:\Users\cliffgoat\AppData\Local\Programs\Python\Python310\python.exe"

import os
import platform
import shutil

### This line of code prints "howdy!" ###
#print("howdy")

### Get current directory on Windows
#dir = os.getcwd()
#print(dir)

### Use powershell to echo hello as test
#os.system("powershell.exe echo hello!")

### Use powershell to get registered user on computer
#os.system("powershell.exe Get-ComputerInfo -Property OSRegisteredUser")

### List disks on computer on powershell
#os.system("powershell.exe get-disk")

### Create subfolders of NFL Teams on C:\
os.makedirs('C:/NFL Teams/NFC/NFC East', exist_ok=True)
os.makedirs('C:/NFL Teams/NFC/NFC West', exist_ok=True)
os.makedirs('C:/NFL Teams/NFC/NFC North', exist_ok=True)
os.makedirs('C:/NFL Teams/NFC/NFC South', exist_ok=True)
os.makedirs('C:/NFL Teams/AFC/AFC East', exist_ok=True)
os.makedirs('C:/NFL Teams/AFC/AFC West', exist_ok=True)
os.makedirs('C:/NFL Teams/AFC/AFC North', exist_ok=True)
os.makedirs('C:/NFL Teams/AFC/AFC South', exist_ok=True)

# Remove these folders I created on C:\
#shutil.rmtree('C:/NFL Teams/', ignore_errors=True)