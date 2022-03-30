#!"C:\Users\cliffgoat\AppData\Local\Programs\Python\Python310\python.exe"

import os
import platform
import shutil

### Create C:\VirtualMachines
os.makedirs('C:/VirtualMachines/WindowsServers/WindowsServer2019', exist_ok=True)
os.makedirs('C:/VirtualMachines/WindowsServers/WindowsServer2016', exist_ok=True)
os.makedirs('C:/VirtualMachines/WindowsServers/WindowsServer2012', exist_ok=True)
os.makedirs('C:/VirtualMachines/WindowsServers/WindowsServer2022', exist_ok=True)
os.makedirs('C:/VirtualMachines/Windows10/10Professional', exist_ok=True)
os.makedirs('C:/VirtualMachines/Windows11/11Professional', exist_ok=True)
os.makedirs('C:/VirtualMachines/Linux/RHEL9', exist_ok=True)
os.makedirs('C:/VirtualMachines/Linux/RHEL8', exist_ok=True)
os.makedirs('C:/VirtualMachines/Linux/RHEL7', exist_ok=True)
os.makedirs('C:/VirtualMachines/Linux/Ubuntu2110', exist_ok=True)
os.makedirs('C:/VirtualMachines/Linux/Ubuntu2004', exist_ok=True)
os.makedirs('C:/VirtualMachines/Linux/Ubuntu1804', exist_ok=True)
os.makedirs('C:/VirtualMachines/Linux/Kali', exist_ok=True)

### Create Games Folder for Epic, Battle.NET, Steam
os.makedirs('C:/Games/EpicGames', exist_ok=True)
os.makedirs('C:/Games/BattleNET', exist_ok=True)
os.makedirs('C:/Games/SteamLibrary', exist_ok=True)

### Create OBS folder on O:\ 10 TB drive
os.makedirs('O:/OBS', exist_ok=True)

### Create _bestVideos on O:\
os.makedirs('O:/_Best OBS Videos', exist_ok=True)

### Create _scratch on O:\
os.makedirs('O:/_Best OBS Videos', exist_ok=True)

### Create downloads folder on O:\
os.makedirs('O:/Downloads', exist_ok=True)

### Create FTP folder on C: for FTP server
os.makedirs('C:/ftp', exist_ok=True)

### Remove C:\VirtualMachines
#shutil.rmtree('C:/VirtualMachines')