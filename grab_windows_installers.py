# URL for 7ZIP Windows x64 installer exe: https://www.7-zip.org/a/7z2201-x64.exe
# URL for Steam Windows installer exe: https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe
import requests
import os
import platform

installDir = 'D:/installers'
os.makedirs(installDir, exist_ok=True)

url7exe = 'https://www.7-zip.org/a/7z2201-x64.exe' # Set variable to URL of current Windows x64 latest 7zip installer
# (exe) from 7-zip.org
steamExe = 'https://cdn.akamai.steamstatic.com/client/installer/SteamSetup.exe'
nppExe = 'https://github.com/notepad-plus-plus/notepad-plus-plus/releases/download/v8.4.8/npp.8.4.8.Installer.x64.exe'
canvaExe = 'https://desktop-release.canva.com/Canva%20Setup%201.59.0.exe'
epicMsi = 'https://launcher-public-service-prod06.ol.epicgames.com/launcher/api/installer/download' \
          '/EpicGamesLauncherInstaller.msi'

arrayOfInstallers = [url7exe, steamExe, nppExe, canvaExe, epicMsi]
x = 0

for i in arrayOfInstallers:
    r = requests.get(i, allow_redirects=True)
    open(f"D:/installers/installer{x}.exe", 'wb').write(r.content)
    x = x+1
