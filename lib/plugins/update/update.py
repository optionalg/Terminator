import os
import sys
import time
import colorama
from colorama import Fore
def db():
    print(Fore.BLUE+'[*]'+Fore.RESET+' Updating To Latest Version...')
    url = "https://github.com/G00Dway/Terminator"
    try:
        if os.path.exists("/usr/var/tmf-meta-inf/Terminator-old"):
            os.system('rm -rf /usr/var/tmf-meta-inf/Terminator-old > /dev/null 2>&1')
        else:
            pass
        if os.path.exists("/usr/share/Terminator"):
            os.system('mv /usr/share/Terminator /usr/var/tmf-meta-inf/Terminator-old > /dev/null 2>&1')
            os.system("git clone "+url+" /usr/share/Terminator > /dev/null 2>&1")
            if os.path.exists("/usr/share/Terminator"):
                os.system('rm -rf /usr/bin/tmconsole > /dev/null 2>&1')
                os.system('chmod +x /usr/share/Terminator/bin/tmconsole/tmconsole > /dev/null 2>&1')
                os.system('cp -r /usr/share/Terminator/bin/tmconsole/tmconsole /usr/bin > /dev/null 2>&1')
                os.system('python3 /usr/share/Terminator/bin/version/ver.py')
            else:
                print(Fore.RED+'[-]'+Fore.RESET+' Update Failed, Using Old Database Instead New')
                os.system('mv /usr/var/tmf-meta-inf/Terminator-old /usr/share/Terminator > /dev/null 2>&1')
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Unable To Update, Database Removed Or Corrupted!')
    except:
        pass


db()
try:
    change = []
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Reading Changelogs...')
    with open("/usr/share/Terminator/lib/plugins/update/data/changelog", "r") as f:
        for line in f:
            change.append(line)
            print(Fore.GREEN+'Changelog:'+Fore.RESET+f' {line}')
except:
    pass
sys.exit()