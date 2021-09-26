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
print(Fore.BLUE+'[*]'+Fore.RESET+' Updating Terminator Framework (Database), This Will Take a While...')
try:
    if os.path.exists("/usr/share/Terminator"):
        os.system("rm -rf /usr/share/Terminator > /dev/null 2>&1")
        os.system("git clone "+url+" /usr/share/Terminator > /dev/null 2>&1")
        sys.exit()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Update Terminator Framework Database!')
        sys.exit()
except:
    pass
