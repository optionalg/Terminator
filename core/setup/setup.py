import os
import time
import random
import datetime
import colorama
import string
import sys
from sys import platform
from colorama import Fore, Style
colorama.init()
date=datetime.datetime.now()
now=date.strftime("%H:%M:%S")
done = "false"
if platform == "win32" or platform == "win64":
    print(Fore.BLUE+'[*]'+Fore.RESET+' For Error Codes Please Visit: https://github.com/G00Dway/Terminator/wiki/error_codes')
    print(Fore.RED+'[-]'+Fore.RESET+' ERROR CODE: 0xtmf999')
    sys.exit()
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
try:
    enter = input("To Proceed With Installation Press [ENTER] Key To Continue... ")
except:
    sys.exit()
def check():
    while done == "false":
        print('\n')
        sys.stdout.write(f'\r[{now}] Checking Terminator Files...                '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' [Working]')
        time.sleep(0.7)
        try:
            if os.path.exists("core/setup/cp/cp.py"):
                sys.stdout.write(f'\r[{now}] Checking Terminator Files...                      '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.GREEN+'OK'+Fore.RESET+']\n')
            else:
                sys.stdout.write(f'\r[{now}] Checking Terminator Files...                      '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.RED+'FAIL'+Fore.RESET+']\n')
                print(Fore.BLUE+'[*]'+Fore.RESET+' For Error Codes Please Visit: https://github.com/G00Dway/Terminator/wiki/error_codes')
                print(Fore.RED+'[-]'+Fore.RESET+' ERROR CODE: 0xtmf799')
                sys.exit()
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write(f'\r[{now}] Checking Dependiences...                     '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' [Working]')
        time.sleep(0.4)
        try:
            if os.path.exists("/usr/bin/python") and os.path.exists("/usr/bin/python3") and os.path.exists("/usr/bin/msfvenom") and os.path.exists("/usr/bin/msfconsole") and os.path.exists("/usr/bin/zenity") and os.path.exists("/usr/bin/xterm") and os.path.exists("/usr/bin/npm"):
                sys.stdout.write(f'\r[{now}] Checking Dependiences...                          '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.GREEN+'OK'+Fore.RESET+']\n')
            else:
                sys.stdout.write(f'\r[{now}] Checking Dependiences...                          '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.BLUE+'Installing...'+Fore.RESET+']\n')
                os.system('bash core/setup/install.sh')
        except:
            pass
        print(Fore.BLUE+'[*]'+Fore.RESET+' Installing PIP Packages...')
        os.system('bash core/setup/pip-install.sh')
        sys.stdout.write(f'\r[{now}] Building Database...                         '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' [Working]')
        os.system("python3 core/setup/cp/cp.py")
        os.system('mkdir /usr/var/tmf-meta-inf > /dev/null 2>&1')
        time.sleep(0.3)
        try:
            if os.path.exists("/usr/share/Terminator"):
                sys.stdout.write(f'\r[{now}] Building Database...                              '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.GREEN+'OK'+Fore.RESET+']\n')
            else:
                sys.stdout.write(f'\r[{now}] Building Database...                              '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.RED+'FAIL'+Fore.RESET+']\n')
                print(Fore.RED+'[!]'+Fore.RESET+' Unable To Build Database, Stopping...')
                time.sleep(0.6)
                sys.exit()
        except:
            pass
        sys.stdout.write(f'\r[{now}] Copying Console Files...                          '+Style.BRIGHT+'STATUS:'+Style.RESET_ALL+' ['+Fore.GREEN+'OK'+Fore.RESET+']')
        time.sleep(1)
        try:
            os.system('chmod +x bin/tmconsole/tmconsole')
            os.system('chmod +x bin/tmconsole/exec.sh')
            os.system('cp -r bin/tmconsole/tmconsole /usr/bin')
        except:
            pass
        os.system('touch /usr/share/Terminator/core/setup/first_setup.txt > /dev/null 2>&1')
        print('\n'+Fore.BLUE+'[*]'+Fore.RESET+' Finishing Setup...')
        os.system('python3 /usr/share/Terminator/core/setup/firstrun.py')
        os.system('python3 /usr/share/Terminator/core/setup/console.py')
        time.sleep(0.5)
        print('\n')
        print(f'Finished At [{now}]')
        print('')
        print(f'Installation Completed! Your Can Now Start Terminator By Typing "tmconsole" In Terminal!')
        print(f"NOTE: Make Sure All Setup Has ["+Fore.GREEN+"OK"+Fore.RESET+"]!")
        break

check()
