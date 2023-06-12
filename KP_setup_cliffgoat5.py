import os

# Define the list of directory paths
os_list = [
    'WindowsServers/WindowsServer2019',
    'WindowsServers/WindowsServer2016',
    'WindowsServers/WindowsServer2012',
    'WindowsServers/WindowsServer2022',
    'Windows10/10Professional',
    'Windows11/11Professional',
    'Linux/RHEL9',
    'Linux/RHEL8',
    'Linux/RHEL7',
    'Linux/Ubuntu2110',
    'Linux/Ubuntu2004',
    'Linux/Ubuntu1804',
    'Linux/Kali'
]

# Create the directories using a loop
for os_path in os_list:
    os.makedirs(f'C:/VirtualMachines/{os_path}', exist_ok=True)

# Define the dictionary of directory paths and drive letters
directories = {
    'C:/VirtualMachines/WindowsServers/WindowsServer2019': 'C',
    'C:/VirtualMachines/WindowsServers/WindowsServer2016': 'C',
    'C:/VirtualMachines/WindowsServers/WindowsServer2012': 'C',
    'C:/VirtualMachines/WindowsServers/WindowsServer2022': 'C',
    'C:/VirtualMachines/Windows10/10Professional': 'C',
    'C:/VirtualMachines/Windows11/11Professional': 'C',
    'C:/VirtualMachines/Linux/RHEL9': 'C',
    'C:/VirtualMachines/Linux/RHEL8': 'C',
    'C:/VirtualMachines/Linux/RHEL7': 'C',
    'C:/VirtualMachines/Linux/Ubuntu2110': 'C',
    'C:/VirtualMachines/Linux/Ubuntu2004': 'C',
    'C:/VirtualMachines/Linux/Ubuntu1804': 'C',
    'C:/VirtualMachines/Linux/Kali': 'C',
    'C:/Games/EpicGames': 'C',
    'C:/Games/BattleNET': 'C',
    'C:/Games/SteamLibrary': 'C',
    'O:/OBS': 'O',
    'O:/_Best OBS Videos': 'O',
    'O:/_scratch': 'O',
    'O:/Downloads': 'O',
    'C:/ftp': 'C'
}

# Create the directories using a loop
for path, drive in directories.items():
    os.makedirs(path.replace(drive + ':/', drive + ':\\'), exist_ok=True)
