#!/usr/bin/python3

#### Intended for setup using python 3.6+ on Linux or Windows

import os
import platform

o = platform.system()

if o == "Linux":
    print("we are doing linux")
    os.system("sudo mkdir /pythonTest")
    os.system("sudo touch /pythonTest/directions.txt")
    os.system("sudo df -hT")
else: 
    print("we are doing windows")
