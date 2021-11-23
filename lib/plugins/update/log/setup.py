import os
import time
import sys
import colorama
from colorama import Fore
import random
os.system('cd /usr/share/Terminator')
def db():
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

def update():
    file = "changelog"
    try:
        if os.path.exists("/usr/share/Terminator/lib/plugins/update/log/changelog"):
            os.system('rm -rf /usr/share/Terminator/lib/plugins/update/log/changelog > /dev/null 2>&1')
            os.system('cd /usr/share/Terminator/lib/plugins/update/log')
            os.system('fetcher --url="https://github.com/G00Dway/Terminator/blob/main/lib/plugins/update/log/changelog"')
            try:
                if os.path.exists("/usr/share/Terminator/lib/plugins/update/log/changelog"):
                    pass
                else:
                    os.system('git checkout origin/master -- /usr/share/Terminator/lib/plugins/update/log/changelog')
                try:
                    if os.path.exists("/usr/share/Terminator/lib/plugins/update/log/changelog"):
                        pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESES+' Unable To Check And Update Files, Using GIT Method...')
                        db()
                except:
                    pass
                try:
                    with open("/usr/share/Terminator/lib/plugins/update/log/changelog", "r") as f:
                        get = f.read()
                        f.close()

                    if get == '[+] No Updates Available.':
                        print(get)
                    else:
                        print(get)
                        upd = input(Fore.BLUE+'[*]'+Fore.RESET+' Do You Want To Update? (Y/n): ')
                        if upd == 'y' or upd == 'Y' or upd == 'yes':
                            print(Fore.BLUE+'[*]'+Fore.RESET+' Updating Terminator Framework...')
                            db()
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Update Interrupted...')
                except:
                    pass
            except:
                pass
    except:
        pass


update()
sys.exit()