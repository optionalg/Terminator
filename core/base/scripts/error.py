import os
import time
import colorama
import future
import requests
import sys
from colorama import Fore
colorama.init()
def tmf(error):
    print(Fore.RED+'[-]'+Fore.RESET+' Trying To Fix Corrupted File...')
    try:
        if os.path.exists(error):
            directory_name = error
            def read():
                with open(error, 'r') as error_var:
                    _file = error_var.read()
                print(Fore.BLUE+'[*]'+Fore.RESET+' File Code:')
                time.sleep(0.5)
                print(_file)
            read()
            os.system('rm -rf '+error+' > /dev/null 2>&1')
            print(Fore.BLUE+'[*]'+Fore.RESET+' Downloading Clean Version Of The File From GIT...')
            git_wget = "https://github.com/G00Dway/Terminator/main/"+directory_name
            os.system("wget "+git_wget+" -O "+directory_name)
            read()
            print(Fore.YELLOW+'[+]'+Fore.RESET+" Completed.")
        else:
            os.mkdir("touch "+error+" > /dev/null 2>&1")
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Completed, Please ReRun Terminator.')
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
