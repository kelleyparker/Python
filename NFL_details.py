#!/usr/bin/env python
# -*- coding: utf-8 -*-
#
#  NFL_details.py
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



def cowboys(city="Dallas",mascot="Cowboys",owner="Jerry Jones"):
	print("The" , city, mascot, "owner is", owner, end='.\n')
def giants(city="New York",mascot="Giants",owner="John Mara"):
	print("The" , city, mascot, "owner is", owner, end='.\n')
def wft(city="Washington",mascot="WFT",owner="Dan Snyder"):
	print("The" , city, mascot, "owner is", owner, end='.\n')
def eagles(city="Philadelphia",mascot="Eagles",owner="Jeffrey Lurie"):
	print("The" , city, mascot, "owner is", owner, end='.\n')


cowboys(city="Arlington")
giants(mascot="NONE")
wft()
eagles()

def main(args):
    return 0

if __name__ == '__main__':
    import sys
    sys.exit(main(sys.argv))
