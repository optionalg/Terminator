import os
import time
import subprocess
import sys
import getpass
import colorama
from colorama import Fore
colorama.init()
def check():
    try:
        if os.path.exists("/usr/share/Terminator/lib/plugins/update/update.sh"):
            os.system('bash /usr/share/Terminator/lib/plugins/update/update.sh')
            print(Fore.YELLOW+'[+]'+Fore.RESET+' Reading Changelogs...')
            with open("/usr/share/Terminator/lib/plugins/update/data/changelog", "r") as f:
                for line in f:
                    print(Fore.GREEN+'Changelog:'+Fore.RESET+f' {line}')
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Unable To Update, Update File Corrupted Or Removed!')
    except:
        pass

check()
sys.exit()