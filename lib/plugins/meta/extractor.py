import os
import time
import colorama
import sys
import random
from colorama import Fore
colorama.init()
class ext:
    def conf(dir):
        def extract(dirext):
            try:
                if os.path.exists(dirext):
                    if os.path.exists("/usr/var/tmf-meta-inf") and os.path.exists("/usr/var/tmf-meta-inf/extr") and os.path.exists("/usr/var/tmf-meta-inf/plugins"):
                        os.system(f'cp -r {dirext} /usr/var/tmf-meta-inf/extr > /dev/null 2>&1')
                        extr = os.listdir("/usr/var/tmf-meta-inf/extr")
                        plugins = os.listdir("/usr/var/tmf-meta-inf/plugins")
                        print(Fore.BLUE+'[*]'+Fore.RESET+f' Copyed {dirext} To "/usr/var/tmf-meta-inf/extr"')
                        for tr in extr:
                            print(Fore.YELLOW+'[+]'+Fore.RESET+f' Available Files: /usr/var/tmf-meta-inf/extr/{tr}')
                    else:
                        os.mkdir("/usr/var/tmf-meta-inf")
                        os.mkdir("/usr/var/tmf-meta-inf/extr")
                        os.mkdir("/usr/var/tmf-meta-inf/lib")
                        os.mkdir("/usr/var/tmf-meta-inf/plugins")
                        extract(dirext)
            except:
                pass
        try:
            if os.path.exists(dir):
                print(Fore.BLUE+'[*]'+Fore.RESET+' Working On Directory...')
                extract(dir)
            else:
                print(Fore.RED+'[-]'+Fore.RESET+' Error: The Directory Doesnt Exist')
                sys.exit()
        except:
            pass
