import os
import time
import colorama
import sys
import random
from colorama import Fore
colorama.init()
if len(sys.argv) < 3:
    sys.exit()

def module(dir):
    try:
        dr = os.listdir(dir)
        for mod in dr:
            try:
                if os.path.exists('/usr/var/tmf-meta-inf/extr/'+mod):
                    pass
                else:
                    os.system('cp -r '+dir+'/'+mod+' /usr/var/tmf-meta-inf/extr > /dev/null 2>&1')
            except:
                pass
    except:
        pass
    sys.exit()

def core(dir):
    print('')

def boot(dir):
    print('')

dir = sys.argv[1]
type = sys.argv[2]

def conf(dir):
    def extract(dirext):
            try:
                if os.path.exists(dirext):
                    if os.path.exists("/usr/var/tmf-meta-inf") and os.path.exists("/usr/var/tmf-meta-inf/extr") and os.path.exists("/usr/var/tmf-meta-inf/plugins"):
                        try:
                            if os.path.exists("/usr/share/Terminator/core/base/extra"):
                                try:
                                    if type == 'modules':
                                        module(dirext)
                                    elif type == 'core':
                                        core(dirext)
                                    elif type == 'boot':
                                        boot(dirext)
                                except:
                                    pass
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Got Error: "Directory /usr/share/Terminator/core/base/extra not found."')
                                sys.exit()
                        except:
                            pass
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
            print(Fore.RED+'[-]'+Fore.RESET+ ' Error: Unable To Extract Required, Updated Files...')
            sys.exit()
    except:
        pass



conf(dir)