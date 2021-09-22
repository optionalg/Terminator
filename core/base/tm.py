import os
import time
import subprocess
import random
import sys
import colorama
from colorama import Fore
import paramiko
import getpass
import future
from sys import platform
import socket
from socket import AF_INET, SOCK_STREAM
colorama.init()
os.system('clear')
user = getpass.getuser()
try:
    if os.path.exists("/usr/share/Terminator/lib/plugins/update"):
        updater = Fore.GREEN+"OK"+Fore.RESET
    else:
        updater = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
version = "V.0.1.1"
commands = '''
Core Commands For "update"
==========================

    Command                       Description
    -------                       -----------
    update                        Update everything
    update console                Update console only
    update database               Update database only

Core Commands For "show"
========================

    Command                       Description
    -------                       -----------
    show modules                  Show all available Modules
    show logs                     Show database activity (Logs)

Global Commands
===============

    Command                       Description
    -------                       -----------
    help                          Show available commands
    clear                         Clear terminal window
    back                          Go back to main

Core Commands
=============

    Command                       Description
    -------                       -----------
    help                          Show available commands
    clear                         Clear terminal window
    update                        Update Terminator framework (Dont checks for updates)
    show <>                       Show specified command
    use <module>                  Use specified Module
    set <option> <value>          Set specified option to specified value (Module use only)
    run                           Run the Module (Module use only)
    exit                          Exit from Terminator
'''
showcommands = '''
Core Commands For "show"
========================

    Command                       Description
    -------                       -----------
    show modules                  Show all available Modules
    show logs                     Show database activity (Logs)
'''
mdls = '''
Name                                                                  Description
-------                                                               --------------
module/online_food_delivery/rce/webshell                              Uploads WebShell To Vulnerable FOOD Delivery Websites And Executes Remote Code
'''
try:
    if os.path.exists("/usr/share/Terminator/lib/db/dbrun.py"):
        database = Fore.GREEN+"OK"+Fore.RESET
    else:
        database = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator") and os.path.exists("/usr/share/Terminator/core"):
        core = Fore.GREEN+"OK"+Fore.RESET
    else:
        core = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/modules"):
        modules = Fore.GREEN+"OK"+Fore.RESET
    else:
        modules = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
try:
    if os.path.exists("/usr/bin/tmconsole") or os.path.exists("/usr/share/Terminator/bin/tmconsole/tmconsole"):
        console = Fore.GREEN+"OK"+Fore.RESET
    else:
        console = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
system = ""
usr = "/usr/share/Terminator"
def banner():
    print(f'''
 _____                   _             _             
|_   _|                 (_)           | |            
  | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
  | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
  \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_| Crash Everything!

Authors   ---=[ G00Dway ]
CodeName  ---=[ FUD-Sec ]
--------------------------
Core     --[ {core} ]
Modules  --[ {modules} ]
Console  --[ {console} ]
Database --[ {database} ]
Updater  --[ {updater} ]

Welcome To Terminator Framework! '''+Fore.YELLOW+f'''{version}'''+Fore.RESET+'''
=========================================
''')
banner()
def main():
    try:
        tmf = input('\033[4mtmf\033[0m > ').strip(" ")
    except KeyboardInterrupt:
        print(Fore.RED+'[-]'+Fore.RESET+' Terminator Stopped...')
        time.sleep(0.5)
        exit()
    tmf = tmf.split()
    while True:
        if tmf == []:
            pass
        elif tmf[0] == 'help' or tmf[0] == '?':
            print(commands)
        elif tmf[0] == 'back':
            pass
        elif tmf[0] == 'clear':
            os.system('clear')
        elif tmf[0] == 'exit':
            print(Fore.RED+'[-]'+Fore.RESET+' Terminator Stopped...')
            time.sleep(0.5)
            sys.exit()
        elif tmf[0] == 'update':
            if len(tmf) < 2:
                os.system('python3 /usr/share/Terminator/lib/plugins/update/updater.py')
            else:
                try:
                    if tmf[1] == 'console':
                        os.system('python3 /usr/share/Terminator/lib/plugins/update/updatercon.py')
                    elif tmf[1] == 'database':
                        os.system('python3 /usr/share/Terminator/lib/plugins/update/updatedb.py')
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Command For "update": "'+tmf[1]+'"')
                except:
                    pass
        elif tmf[0] == 'show':
            if len(tmf) < 2:
                print(showcommands)
            else:
                try:
                    if tmf[1] == '-h':
                        print(showcommands)
                    elif tmf[1] == 'logs':
                        os.system('vim /usr/share/Terminator/core/logs/logs.log')
                    elif tmf[1] == 'modules':
                        print(mdls)
                    else:
                        print(showcommands)
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Command For "show": "'+tmf[1]+'"')
                except:
                    pass
        elif tmf[0] == 'set':
            print(Fore.RED+'[-]'+Fore.RESET+' This Command Is Module Use Only!')
        elif tmf[0] == 'use':
            if len(tmf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please Specify The Module Name')
            else:
                try:
                    if modules == Fore.GREEN+"OK"+Fore.RESET:
                        if tmf[1] == 'module/online_food_delivery/rce/webshell':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/foodrce.py')
                    else:
                        time.sleep(0.5)
                        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Load Module: "module/online_food_delivery/rce/webshell"')
                except:
                    pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Unknown Command: "'+tmf[0]+'"')
        try:
            tmf = input('\033[4mtmf\033[0m > ').strip(" ")
        except KeyboardInterrupt:
            print(Fore.RED+'[-]'+Fore.RESET+' Terminator Stopped...')
            time.sleep(0.5)
            exit()
        tmf = tmf.split()

if __name__ == "__main__":
    main()
