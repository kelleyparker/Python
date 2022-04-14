#!/usr/bin/env python3

import os
import platform
import pathlib
import shutil


nflPath = 'C:/NFL Teams/'
nfcDivsNames = [ 'NFC South', 'NFC North', 'NFC East', 'NFC West' ]
afcDivsNames = [ 'AFC South', 'AFC North', 'AFC East', 'AFC West' ]

nfcEast = [ 'Cowboys', 'Commanders', 'Eagles', 'Giants']
nfcSouth = [ 'Buccaneers', 'Saints', 'Panthers', 'Falcons']
nfcWest = [ 'Cardinals', 'Rams', 'Seahawks', '49ers']
nfcNorth = [ 'Packers', 'Bears', 'Vikings', 'Lions']
nfcDivTeams = [ nfcEast, nfcSouth, nfcWest, nfcNorth ]

shutil.rmtree('C:/NFL Teams/', ignore_errors=True)
os.mkdir(nflPath)

def main():
    createFolders()

def createFolders():
    for i in afcDivsNames:
        os.makedirs('C:/NFL Teams/AFC/%s' % i)
    for i in nfcDivsNames:
        os.makedirs('C:/NFL Teams/NFC/%s' % i)



if __name__ == "__main__":
    main()