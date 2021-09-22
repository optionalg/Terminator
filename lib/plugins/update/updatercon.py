import os
import time
import subprocess
import sys
import getpass
import colorama
from colorama import Fore
colorama.init()
user = getpass.getuser()
url = "https://github.com/G00Dway/Terminator"
dir1 = "/home/"+user+"/Terminator"
dir2 = "/root/Terminator"
database = "/usr/share/Terminator"
bin = "/usr/bin/tmconsole"
desktop = "/usr/share/applications/terminator.desktop"
print(Fore.BLUE+'[*]'+Fore.RESET+' Updating Terminator Framework (Console), This Will Take a While...')
try:
    if os.path.exists("/usr/share/Terminator"):
        os.system('git clone '+url+' /usr/share/Terminator_cache > /dev/null 2>&1')
        os.system('chmod +x /usr/share/Terminator_cache/bin/tmconsole/tmconsole > /dev/null 2>&1')
        os.system('rm -rf /usr/bin/tmconsole > /dev/null 2>&1')
        os.system('cp -r /usr/share/Terminator_cache/bin/tmconsole/tmconsole /usr/bin > /dev/null 2>&1')
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Terminator Console Updated Successfully!')
        sys.exit()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Update Terminator Framework Console!')
        sys.exit()
except:
    pass