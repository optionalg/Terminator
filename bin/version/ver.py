import os
import colorama
from colorama import Fore
import sys
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
        os.system('python3 /usr/share/Terminator/lib/plugins/meta/extractor.py')
        print(Fore.RED+'[-]'+Fore.RESET+' You Should Restart Framework To Setup Updated Changes')
        sys.exit()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Start Extractor!')
        sys.exit()
except:
    pass
