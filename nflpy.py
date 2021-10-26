#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  print.py
#  
#  Copyright 2021 Kelley Parker <kparker@atlld-kparker>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
#  
#  

print("########################################################")
print("### Welcome to the NFL lookup Python script, ###########")
print("### developed by Kelley Parker! How can I help you? ####")
print("########################################################")


nfcEast = ["Cowboys","Giants","Eagles","WFT"]
nfcWest = ["Cardinals","Rams","49ers","Seahawks"]
nfcNorth = ["Packers","Vikings","Bears","Lions"]
nfcSouth = ["Buccaneers","Saints","Falcons","Panthers"]

afcEast = ["Bills","Patriots","Jets","Dolphins"]
afcWest = ["Raiders","Chargers","Chiefs","Broncos"]
afcNorth = ["Bengals","Ravens","Browns","Steelers"]
afcSouth = ["Titans","Colts","Jaguars","Texans"]

nfcDivisions = [nfcEast,nfcWest,nfcNorth,nfcSouth]
afcDivisions = [afcEast,afcWest,afcNorth,afcSouth]

print("Type in the division whose teams you would like to see listed.\n")

print("1) NFC East")
print("2) NFC West")
print("3) NFC North")
print("4) NFC South\n")
print("5) AFC East")
print("6) AFC West")
print("7) AFC North")
print("8) AFC South\n")

print("9) List all NFC divisions")
print("10) List all AFC divisions")

inp = input("Type in your desired option from above: " )

if inp == "1":
	print("The teams in the NFC East are " + nfcEast[0] + ", " + nfcEast[1] + ", " + nfcEast[2] + ", and the " + nfcEast[3] + ".")
if inp == "2":
	print("The teams in the NFC West are " + nfcWest[0] + ", " + nfcWest[1] + ", " + nfcWest[2] + ", and the " + nfcWest[3] + ".")
if inp == "3":
	print("The teams in the NFC North are " + nfcNorth[0] + ", " + nfcNorth[1] + ", " + nfcNorth[2] + ", and the " + nfcNorth[3] + ".")
if inp == "4":
	print("The teams in the NFC South are " + nfcSouth[0] + ", " + nfcSouth[1] + ", " + nfcSouth[2] + ", and the " + nfcSouth[3] + ".")
if inp == "5":
	print("The teams in the NFC East are " + afcEast[0] + ", " + afcEast[1] + ", " + afcEast[2] + ", and the " + afcEast[3] + ".")
if inp == "6":
	print("The teams in the NFC West are " + afcWest[0] + ", " + afcWest[1] + ", " + afcWest[2] + ", and the " + afcWest[3] + ".")
if inp == "7":
	print("The teams in the NFC North are " + afcNorth[0] + ", " + afcNorth[1] + ", " + afcNorth[2] + ", and the " + afcNorth[3] + ".")
if inp == "8":
	print("The teams in the NFC South are " + afcSouth[0] + ", " + afcSouth[1] + ", " + afcSouth[2] + ", and the " + afcSouth[3] + ".")

if inp == "9":
	print("The divisions in the NFC are: " + str(nfcDivisions) + ".")
if inp == "10":
	print("The divisions in the AFC are: " + str(afcDivisions) + ".")
# still need to tidy up options 9 and 10 to output a cleaner result

else:
	print("That's all folks!")

	

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
