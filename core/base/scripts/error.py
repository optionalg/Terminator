import os
import time
import colorama
import future
import requests
import sys
from colorama import Fore
colorama.init()
def tmf(error):
    print(Fore.RED+'[-]'+Fore.RESET+' Trying To Fix Corrupted Files...')
    try:
        if os.path.exists(error):
            fix = True
        else:
            os.system('rm -rf '+error+' > /dev/null 2>&1')
            os.mkdir(error)
        if fix == True:
            print(Fore.YELLOW+'[+]'+Fore.RESET+' Completed, Please ReRun Terminator.')
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Some Files Of Terminator Are Corrupted, Please ReInstall Terminator.')
    except:
        pass
    sys.exit()

if len(sys.argv) < 2:
    sys.exit()

type = sys.argv[1]

if type == 'db':
    pass
elif type == 'error':
    tmf(type)

url = "https://github.com/G00Dway/Terminator"
def fix(dir):
    print(Fore.RED+'[-]'+Fore.RESET+' ...')
    print(Fore.RED+'[-]'+Fore.RESET+' Trying To ReInstall Database...')
    try:
        if os.path.exists(dir):
            os.system('rm -rf '+dir+' > /dev/null 2>&1')
        else:
            pass
    except:
        pass
    os.system('git clone '+url+' /usr/share/Terminator > /dev/null 2>&1')
    print(Fore.YELLOW+'[+]'+Fore.RESET+' ReInstall Completed, Please ReRun Terminator.')
    sys.exit()

dir = "/usr/share/Terminator"
cache = "/usr/share/Terminator/core/base/scripts/cache"
file = 0
try:
    if os.path.exists(dir):
        path = True
    else:
        fix(dir)
except:
    pass

if path == True:
    sys.exit()
