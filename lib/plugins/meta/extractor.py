import os
import sys
import colorama
from colorama import Fore
import random
import string
import time
colorama.init()
url = "https://www.exploit-db.com/download/50420"
url2 = "https://www.exploit-db.com/download/50382"
url3 = "https://www.exploit-db.com/download/50379"
try:
    if os.path.exists("/usr/share/Terminator/bin/version/plugin-cache"):
        plugins = True
    else:
        os.mkdir("/usr/share/Terminator/bin/version/plugin-cache")
except:
    pass
def check():
    url1_cache = "50420.pl"
    url2_cache = "50382.pl"
    url3_cache = "50379.pl"
    try:
        if os.path.exists("/usr/share/Terminator/bin/version/plugin-cache/"+url1_cache):
            good = True
        else:
            print(Fore.BLUE+'[*]'+Fore.RESET+' Installing "50420.pl" Plugin Module...')
            os.system('wget '+url+' -O /usr/share/Terminator/bin/version/plugin-cache/'+url1_cache+' > /dev/null 2>&1')
        if os.path.exists("/usr/share/Terminator/bin/version/plugin-cache/"+url2_cache):
            good1 = True
        else:
            print(Fore.BLUE+'[*]'+Fore.RESET+' Installing "50382.pl" Plugin Module...')
            os.system('wget '+url2+' -O /usr/share/Terminator/bin/version/plugin-cache/'+url2_cache+' > /dev/null 2>&1')
        if os.path.exists("/usr/share/Terminator/bin/version/plugin-cache/"+url3_cache):
            good2 = True
        else:
            print(Fore.BLUE+'[*]'+Fore.RESET+' Installing "50379.pl" Plugin Module...')
            os.system('wget '+url3+' -O /usr/share/Terminator/bin/version/plugin-cache/'+url3_cache+' > /dev/null 2>&1')
        try:
            if good == True and good1 == True and good2 == True:
                time.sleep(0.6)
                print(Fore.YELLOW+'[+]'+Fore.RESET+' All Good...')
                time.sleep(0.1)
                print(Fore.BLUE+'[*]'+Fore.RESET+' PreConfiguring Database...')
                try:
                    if os.path.exists("/usr/var/tmf-meta-inf"):
                        os.system('rm -rf /usr/var/tmf-meta-inf > /dev/null 2>&1')
                        os.mkdir("/usr/var/tmf-meta-inf")
                        os.mkdir("/usr/var/tmf-meta-inf/lib")
                        os.mkdir("/usr/var/tmf-meta-inf/db")
                        os.mkdir("/usr/var/tmf-meta-inf/data")
                    else:
                        os.mkdir("/usr/var/tmf-meta-inf")
                        os.mkdir("/usr/var/tmf-meta-inf/lib")
                        os.mkdir("/usr/var/tmf-meta-inf/db")
                        os.mkdir("/usr/var/tmf-meta-inf/data")
                except:
                    pass
                time.sleep(0.1)
                sys.exit()
            else:
                os.system('python3 /usr/share/Terminator/lib/plugins/meta/extractor.py')
                sys.exit()
        except:
            pass
    except:
        pass

check()
