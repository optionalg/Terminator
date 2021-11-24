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
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Unable To Update, Update File Corrupted Or Removed!')
    except:
        pass

check()
sys.exit()