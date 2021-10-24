import os
import colorama
from colorama import Fore
import sys
import time
import random
colorama.init()
try:
    if os.path.exists("/usr/share/Terminator/bin/version/plugin-cache"):
        pass
    else:
        os.mkdir("/usr/share/Terminator/bin/version/plugin-cache")
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/lib/plugins/meta/extractor.py"):
        print(Fore.BLUE+'[*]'+Fore.RESET+' Extracting Files...')
        time.sleep(0.1)
        print(Fore.BLUE+'[*]'+Fore.RESET+' Reloading Plugins....')
        time.sleep(0.2)
        os.system('python3 /usr/share/Terminator/lib/plugins/meta/extractor.py')
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Please Restart Terminator To Setup Changes!')
        sys.exit()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Start Extractor!')
        sys.exit()
except:
    pass
