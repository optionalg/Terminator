import os
import time
import colorama
import sys
import getpass
from colorama import Fore
colorama.init()
user = getpass.getuser()
path1 = "/home/"+user+"/Terminator"
path2 = "/root/Terminator"
url = "https://github.com/G00Dway/Terminator"
try:
    if os.path.exists("/usr/share/Terminator"):
        os.system('rm -rf /usr/share/Terminator')
        os.system('git clone '+url+' /usr/share/Terminator > /dev/null 2>&1')
    else:
        os.system('git clone '+url+' /usr/share/Terminator > /dev/null 2>&1')
except:
    pass