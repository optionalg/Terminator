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
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Extracting Updated Files...')
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Extractor Not Found!')
        sys.exit()
except:
    pass