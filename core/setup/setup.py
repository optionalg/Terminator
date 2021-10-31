import os
import time
import random
import datetime
import colorama
import string
import sys
from colorama import Fore, Style
colorama.init()
date=datetime.datetime.now()
now=date.strftime("%H:%M:%S")
done = "false"
def banner():
    print('''
 _____                   _             _             
|_   _|                 (_)           | |            
  | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
  | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
  \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_| [ By G00Dway ]
                                                     
Welcome To Terminator Framework Installer!
==========================================

About Terminator
-----------------
Terminator Framework is a Explotation Framework With RCE, etc. 
for Testing YOUR Own Devices For Any Vulnerabilies

Bugs, Reports
-----------------
If You Found Any Bugs In Setup, Please Report Them At: https://github.com/G00Dway/Terminator/issues
''')
os.system('clear')
time.sleep(0.1)
banner()
print('')
time.sleep(1)
enter = input("To Proceed With Installation Press [ENTER] Key To Continue... ")
def check():
    while done == "false":
        print('\n')
        sys.stdout.write(f'\r[{now}] Checking Terminator Files...                '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' [Working]...')
        time.sleep(0.7)
        try:
            if os.path.exists("core/setup/cp/cp.py"):
                sys.stdout.write(f'\r[{now}] Checking Terminator Files...                 '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.GREEN+'OK'+Fore.RESET+']...\n')
            else:
                sys.stdout.write(f'\r[{now}] Checking Terminator Files...                 '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.RED+'FAIL'+Fore.RESET+']...\n')
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write(f'\r[{now}] Checking Dependiences...                    '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' [Working]...')
        time.sleep(0.1)
        try:
            if os.path.exists("/usr/bin/python") and os.path.exists("/usr/bin/python3") and os.path.exists("/usr/bin/msfvenom") and os.path.exists("/usr/bin/msfconsole"):
                sys.stdout.write(f'\r[{now}] Checking Dependiences...            '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.GREEN+'OK'+Fore.RESET+']...\n')
            else:
                sys.stdout.write(f'\r[{now}] Checking Dependiences...            '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.BLUE+'Installing'+Fore.RESET+']...\n')
                os.system('bash core/setup/install.sh')
        except:
            pass
        sys.stdout.write(f'\r[{now}] Building Database...                        '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' [Working]...')
        os.system("python3 core/setup/cp/cp.py")
        os.system('mkdir /usr/var/tmf-meta-inf > /dev/null 2>&1')
        time.sleep(0.3)
        try:
            if os.path.exists("/usr/share/Terminator"):
                sys.stdout.write(f'\r[{now}] Building Database...                        '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.GREEN+'OK'+Fore.RESET+']...\n')
            else:
                sys.stdout.write(f'\r[{now}] Building Database...                        '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.RED+'FAIL'+Fore.RESET+']...\n')
        except:
            pass
        sys.stdout.write(f'\r[{now}] Copying Console Files...                    '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' [Working]...')
        time.sleep(1)
        try:
            os.system('chmod +x bin/tmconsole/tmconsole')
            os.system('chmod +x bin/tmconsole/exec.sh')
            os.system('cp -r bin/tmconsole/tmconsole /usr/bin')
        except:
            pass
        print('\n')
        print(f'Finished At [{now}]')
        print('')
        print(f'Installation Completed! Your Can Now Start Terminator By Typing "tmconsole" In Terminal!')
        print(f"NOTE: Make Sure All Setup Has ["+Fore.GREEN+"OK"+Fore.RESET+"]!")
        break

check()
