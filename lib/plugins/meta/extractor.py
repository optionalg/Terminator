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
        types = 'exploits'
        types1 = 'handlers'
        types2 = 'other'
        types3 = 'payloads'
        dr = os.listdir(dir+'/'+types)
        dr1 = os.listdir(dir+'/'+types1)
        dr2 = os.listdir(dir+'/'+types2)
        dr3 = os.listdir(dir+'/'+types3)
        for mod in dr:
            try:
                if os.path.exists('/usr/var/tmf-meta-inf/extr/'+mod):
                    pass
                else:
                    os.system('cp -r '+dir+'/'+types+'/'+mod+' /usr/var/tmf-meta-inf/extr > /dev/null 2>&1')
            except:
                pass
        for mod2 in dr1:
            try:
                if os.path.exists('/usr/var/tmf-meta-inf/extr/'+mod2):
                    pass
                else:
                    os.system('cp -r '+dir+'/'+types1+'/'+mod2+' /usr/var/tmf-meta-inf/extr > /dev/null 2>&1')
            except:
                pass
        for mod3 in dr2:
            try:
                if os.path.exists('/usr/var/tmf-meta-inf/extr/'+mod3):
                    pass
                else:
                    os.system('cp -r '+dir+'/'+types2+'/'+mod3+' /usr/var/tmf-meta-inf/extr > /dev/null 2>&1')
            except:
                pass
        for mod4 in dr3:
            try:
                if os.path.exists('/usr/var/tmf-meta-inf/extr/'+mod4):
                    pass
                else:
                    os.system('cp -r '+dir+'/'+types3+'/'+mod4+' /usr/var/tmf-meta-inf/extr > /dev/null 2>&1')
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
