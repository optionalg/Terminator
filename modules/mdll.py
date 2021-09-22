import os
import time
import colorama
import sys
from colorama import Fore
colorama.init()
try:
    if os.path.exists("/usr/share/Terminator/modules"):
        mod = True
    else:
        mod = False
except:
    pass
if mod == True:
    pass
else:
    sys.exit()