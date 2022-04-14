#!/usr/bin/env python3

import os
import platform
import pathlib
import shutil


nflPath = 'C:/NFL Teams/'
nflGeos = [ 'South', 'North', 'East', 'West' ]
nfcEast = [ 'Cowboys', 'Commanders', 'Eagles', 'Giants']


shutil.rmtree('C:/NFL Teams/', ignore_errors=True)
os.mkdir('C:/NFL Teams/')


def main():
    createFolders()
    createNFCEastTextFiles()


def createFolders():
    for i in nflGeos:
        os.makedirs('C:/NFL Teams/AFC/%s' % i)
    for i in nflGeos:
        os.makedirs('C:/NFL Teams/NFC/%s' % i)

def createNFCEastTextFiles():

    for i in nfcEast:
        os.chdir('C:/NFL Teams/NFC/East')
        open('%s.txt' % i, 'w')
    for file in os.listdir('C:/NFL Teams/NFC/East'), teams in nfcEast:
        #print(file)
        f = open(file, 'w')
        f.write('This team is the %s' % teams )





if __name__ == "__main__":
    main()
