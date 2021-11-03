import os
import time
import colorama
import sys
import getpass
from colorama import Fore
colorama.init()
user = getpass.getuser()
url = "https://github.com/G00Dway/Terminator"
try:
    if os.path.exists("/usr/share/Terminator"):
        print(Fore.BLUE+'[*]'+Fore.RESET+' Removing Previous Database...')
        os.system('rm -rf /usr/share/Terminator > /dev/null 2>&1')
        os.system('rm -rf /usr/var/tmf-meta-inf > /dev/null 2>&1')
        os.system('rm -rf /root/.tmf > /dev/null 2>&1')
        os.system('git clone '+url+' /usr/share/Terminator > /dev/null 2>&1')
    else:
        os.system('git clone '+url+' /usr/share/Terminator > /dev/null 2>&1')
except:
    pass