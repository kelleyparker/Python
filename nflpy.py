#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  print.py
#  
#  Copyright 2021 Kelley Parker 
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

nfcDivisionsNames = ["NFC East","NFC West","NFC North","NFC South"]
afcDivisionsNames = ["AFC East","AFC West","AFC North","AFC South"]
nfcDivisionsTeamVars = [nfcEast,nfcWest,nfcNorth,nfcSouth]
afcDivisionsTeamVars = [afcEast,afcWest,afcNorth,afcSouth]

nflDivisions = ["NFC Conference","AFC Conference"]
nflTeamVars = [afcDivisionsTeamVars,nfcDivisionsTeamVars]



def printMenu():
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
	print("11) List all NFL teams")
	global inp
	inp = 0
	inp = input("Type in your desired option from above: ")


def readResponse():
	if inp == "1":
		print("The teams in the NFC East are the " + nfcEast[0] + ", " + nfcEast[1] + ", " + nfcEast[2] + ", and the " + nfcEast[3] + ".")
		printMenu()
	if inp == "2":
		print("The teams in the NFC West are the " + nfcWest[0] + ", " + nfcWest[1] + ", " + nfcWest[2] + ", and the " + nfcWest[3] + ".")
	if inp == "3":
		print("The teams in the NFC North are the " + nfcNorth[0] + ", " + nfcNorth[1] + ", " + nfcNorth[2] + ", and the " + nfcNorth[3] + ".")
	if inp == "4":
		print("The teams in the NFC South are the " + nfcSouth[0] + ", " + nfcSouth[1] + ", " + nfcSouth[2] + ", and the " + nfcSouth[3] + ".")
	if inp == "5":
		print("The teams in the NFC East are the " + afcEast[0] + ", " + afcEast[1] + ", " + afcEast[2] + ", and the " + afcEast[3] + ".")
	if inp == "6":
		print("The teams in the NFC West are the " + afcWest[0] + ", " + afcWest[1] + ", " + afcWest[2] + ", and the " + afcWest[3] + ".")
	if inp == "7":
		print("The teams in the NFC North are the " + afcNorth[0] + ", " + afcNorth[1] + ", " + afcNorth[2] + ", and the " + afcNorth[3] + ".")
	if inp == "8":
		print("The teams in the NFC South are the " + afcSouth[0] + ", " + afcSouth[1] + ", " + afcSouth[2] + ", and the " + afcSouth[3] + ".")
	if inp == "9":
		print("The divisions in the NFC are the " + nfcDivisionsNames[0] + ", " + nfcDivisionsNames[1] + ", " + nfcDivisionsNames[2] + ", and the " + nfcDivisionsNames[3] + ".")
	if inp == "10":
		print("The divisions in the AFC are the " + afcDivisionsNames[0] + ", " + afcDivisionsNames[1] + ", " + afcDivisionsNames[2] + ", and the " + afcDivisionsNames[3] + ".")
	if inp == "11":
		print(nflTeamVars)
	# if inp == ("Exit") or ("ex") or ("EX") or ("Ex") or ("EXIT") or ("exit") or ("xit") or ("XIT"):
		# print("Thanks for using this program!")
		# exit
	else:
		print("That is not a valid response, please resubmit your response.")
		printMenu()
		

printMenu()
readResponse()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
