import os
import sys
import time
import colorama
from colorama import Fore, Style
def db():
    try:
        def download():
            os.system('wget https://raw.githubusercontent.com/G00Dway/Terminator/main/VERSION -O /usr/share/Terminator/core/logs/btop.log > /dev/null 2>&1')
        if os.path.exists("/usr/share/Terminator/core/logs/btop.log"):
            os.system('rm -rf /usr/share/Terminator/core/logs/btop.log > /dev/null 2>&1')
            download()
        else:
            download()
        with open("/usr/share/Terminator/VERSION", 'r') as version:
            ver = version.read()
        with open("/usr/share/Terminator/core/logs/btop.log", 'r') as to_ver:
            ver_to = to_ver.read()
    except:
        pass
    print(Fore.BLUE+'[*]'+Fore.RESET+' Current Version: '+ver)
    print(Fore.YELLOW+'[+]'+Fore.RESET+' Update Version: '+ver_to)
    update_framework = input(Fore.CYAN+'[?]'+Fore.RESET+' Do You Want To Continue? (Default "Y"): ').strip(" ")
    symbols = "yyesYESY"
    if update_framework in symbols:
        pass
    elif update_framework == "" or update_framework == " ":
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Update Interrupted...')
        sys.exit()
    print(Fore.BLUE+'[*]'+Fore.RESET+' Downloading Update...')
    url = "https://github.com/G00Dway/Terminator"
    try:
        if os.path.exists("/usr/var/tmf-meta-inf/Terminator-old"):
            os.system('rm -rf /usr/var/tmf-meta-inf/Terminator-old > /dev/null 2>&1')
        else:
            pass
        if os.path.exists("/usr/share/Terminator"):
            try:
                if os.path.exists('/usr/share/Terminator/core/logs/time.log'):
                    os.system('mv /usr/share/Terminator/core/logs/time.log /usr/var/tmf-meta-inf/time.log > /dev/null 2>&1')
                else:
                    pass
            except:
                pass
            os.system('mv /usr/share/Terminator /usr/var/tmf-meta-inf/Terminator-old > /dev/null 2>&1')
            print(Fore.BLUE+'[*]'+Fore.RESET+' Creating Backup Files...')
            os.system("git clone "+url+" /usr/share/Terminator > /dev/null 2>&1")
            print(Fore.BLUE+'[*]'+Fore.RESET+' Installing Update...')
            if os.path.exists("/usr/share/Terminator"):
                os.mkdir('/usr/share/Terminator/core/logs')
                try:
                    if os.path.exists('/usr/var/tmf-meta-inf/time.log'):
                        os.system("mv /usr/var/tmf-meta-inf/time.log /usr/share/Terminator/core/logs/time.log > /dev/null 2>&1")
                    else:
                        pass
                except:
                    pass
                os.system('python3 /usr/share/Terminator/bin/version/ver.py')
            else:
                print(Fore.RED+'[-]'+Fore.RESET+' Update Failed, Using Old Database Instead New')
                os.system('mv /usr/var/tmf-meta-inf/Terminator-old /usr/share/Terminator > /dev/null 2>&1')
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Unable To Update, Database Removed Or Corrupted!')
    except:
        pass


db()
sys.exit()