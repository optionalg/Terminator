import os
import colorama
from colorama import Fore
import sys
import time
colorama.init()
modules = "/usr/share/Terminator/modules"
try:
    if os.path.exists("/usr/share/Terminator/lib/plugins/meta/extractor.py"):
        os.system('python3 /usr/share/Terminator/lib/plugins/meta/extractor.py '+modules+' modules')
        print(Fore.BLUE+'[*]'+Fore.RESET+' Extracting Updated Files...')
        time.sleep(0.7)
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Update Completed.')
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Restart Terminator To Setup Changes')
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Extractor Not Found!')
        sys.exit()
except:
    pass