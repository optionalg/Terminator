import os
import colorama
from colorama import Fore
import sys
import time
colorama.init()
try:
    with open('/usr/share/Terminator/bin/version/ver.yaml', 'r') as f:
        version = f.read()
        f.close()
except:
    pass
print(Fore.MAGENTA+'[!]'+Fore.RESET+f' Updated To Version: {version}')
sys.exit()