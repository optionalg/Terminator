import os
import time
import subprocess
import random
import sys
import colorama
from colorama import Fore, Style
import getpass
import future
from sys import platform
import socket
from socket import AF_INET, SOCK_STREAM
colorama.init()
os.system('clear')
user = getpass.getuser()
try:
    many = os.listdir("/usr/share/Terminator/modules/exploits")
    many2 = os.listdir("/usr/share/Terminator/modules/handlers")
    many3 = os.listdir("/usr/share/Terminator/modules/other")
    many4 = os.listdir("/usr/share/Terminator/modules/payloads")
    number_files = len(many)
    number_files2 = len(many2)
    number_files3 = len(many3)
    number_files4 = len(many4)
    result = number_files+number_files2+number_files3+number_files4
except:
    pass
try:
    if user == "root":
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' ROOT Not Detected! Please ReRun Terminator With ROOT Permissions!')
        sys.exit()
except:
    pass
def removeses():
    try:
        if os.path.exists("/usr/share/Terminator/core/session"):
            os.system('rm -rf /usr/share/Terminator/core/session > /dev/null 2>&1')
        else:
            pass
    except:
        pass
try:
    with open("/usr/share/Terminator/bin/version/ver.yaml", "r") as yr:
        ver = yr.read()
        yr.close()
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/lib/plugins/update"):
        updater = Fore.GREEN+"OK"+Fore.RESET
    else:
        updater = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
version = "1.8.4"+Fore.LIGHTYELLOW_EX+"#dev"
commands = '''
Global Commands
===============

    Command                       Description
    -------                       -----------
    help                          Show available commands
    clear                         Clear terminal window
    back                          Go back to main

Update Commands
===============

    Command                       Description
    -------                       -----------
    update                        Update Terminator framework

Show Commands
=============

    Command                       Description
    -------                       -----------
    show modules                  Show all available Modules
    show payloads                 Show all available Payloads
    show logs                     Show database activity (Logs)

Job Commands
============

    Command                       Description
    -------                       -----------
    jobs                          Show available running Jobs (Max. Jobs 1)
    int <Job ID>                  Interact with Job
    jkill <Job ID>                Kill Job

Core Commands
=============

    Command                       Description
    -------                       -----------
    help                          Show available commands
    clear                         Clear terminal window
    clean                         Clean database logs, cache
    banner                        Show banner
    update                        Update Terminator framework (Dont checks for updates)
    show <>                       Show specified command
    use <module>                  Use specified Module
    set <option> <value>          Set specified option to specified value (Module use only)
    run                           Run the Module (Module use only)
    exit                          Exit from Terminator
'''
showcommands = '''
Show Commands
=============

    Command                       Description
    -------                       -----------
    show modules                  Show all available Modules
    show payloads                 Show all available Payloads
    show logs                     Show database activity (Logs)
'''
update_info = '''
Update Commands
===============

    Command                       Description
    -------                       -----------
    update                        Update everything
    update console                Update console only
    update database               Update database only
'''
mdls = '''
Module Name                                     Type             Verify          Description
------------                                    -----            -------         ------------
module/multi/handler                            Handler          yes             Handler For Payloads
module/packet_sniff/http/sniff                  Local            yes             HTTP Packet Sniffer, Pass/Email/Login/Other
module/blueman/bluetooth_dos/l2ping             Local            no              Bluetooth Denial Of Service
module/online_food_delivery/rce/webshell        Web              yes             RCE, WebShell Upload & Connect
module/evolution_cms/rce/login_web              Web              no              RCE Cms, Login & Execute Code
module/citadel_web_kit/cred/log                 Web              yes             Citadel Web kit, Credential Harvester
module/patient_appointment/sys/web              Web              no              RCE, Patient Appointment System
module/rental_unit/storage/shell                Web              no              RCE, Storage Unit Rental Management             
'''
pylds = '''
Payload Name                                    Type             Verify          Description
-------------                                   -----            -------         ------------
payload/poc/redragon_mouse/wr                   Windows          no              Redragon_Mouse Payload (REDRAGON_MOUSE.sys)
payload/win/win_reverse_shell                   Windows          yes             reverse shell Payload (win32, win64)
payload/apk/android_reverse_shell               Android          yes             reverse shell Payload (V.3 - 9)
'''
try:
    if os.path.exists("/usr/share/Terminator/lib/db/dbrun.py") and os.path.exists("/usr/share/Terminator/lib/data"):
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
try:
    if updater == Fore.GREEN+"OK"+Fore.RESET and database == Fore.GREEN+"OK"+Fore.RESET and core == Fore.GREEN+"OK"+Fore.RESET and modules == Fore.GREEN+"OK"+Fore.RESET and console == Fore.GREEN+"OK"+Fore.RESET:
        database_run = Fore.GREEN+"OK"+Fore.RESET
    else:
        database_run = Fore.GREEN+"FATAL"+Fore.RESET
except:
    pass
tips = ['HINT: After Updating, Terminator Saves '+Fore.GREEN+'Old'+Fore.RESET+' Database At: "/usr/var/tmf-meta-inf"!', 'HINT: Terminator Runs Slow? Why Not Try The '+Fore.GREEN+'clean'+Fore.RESET+' Command!', 'HINT: Always Keep Terminator Up-To-Date!', 'HINT: Use '+Fore.GREEN+'back'+Fore.RESET+' Command To Go Back To Main Menu!', 'HINT: To Kill Running Handler Jobs, Use '+Fore.GREEN+'jkill <Job ID>'+Fore.RESET, 'HINT: To Interact With Handler Jobs, Use '+Fore.GREEN+'int <Job ID>'+Fore.RESET]
def banner():
    print(f'''
 _____                   _             _             
|_   _|                 (_)           | |            
  | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
  | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
  \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_| [ HackNet Community ]

+ -- -=[ Terminator Framework             ]
      <[ Database                      {database_run} ]
      <[ Version                {version} '''+Fore.RESET+f''']
      <[ Modules Loaded                 {result} ]
''')
banner()
print(random.choice(tips))
def main():
    try:
        tmf = input('\033[4mtmf\033[0m > ').strip(" ")
    except KeyboardInterrupt:
        print('')
        print(Fore.RED+'[-]'+Fore.RESET+' Terminator Stopped...')
        removeses()
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
        elif tmf[0] == 'clean':
            print(Fore.BLUE+'[*]'+Fore.RESET+' Cleaning Database...')
            cache = os.listdir("/usr/share/Terminator/core/base/scripts/cache/libs")
            root_files = os.listdir("/root/.tmf")
            logs = "/usr/share/Terminator/core/logs/logs.log"
            for clr in cache:
                os.system('rm -rf /usr/share/Terminator/core/base/scripts/cache/libs/'+clr+' > /dev/null 2>&1')
            os.system('rm -rf '+logs+' > /dev/null 2>&1')
            for clean_root in root_files:
                os.system('rm -rf /root/.tmf/'+clean_root+' > /dev/null 2>&1')
            print(Fore.YELLOW+'[+]'+Fore.RESET+' Cleanup Completed!')
        elif tmf[0] == 'clear':
            os.system('clear')
        elif tmf[0] == 'banner':
            banner()
        elif tmf[0] == 'exit':
            print(Fore.RED+'[-]'+Fore.RESET+' Terminator Stopped...')
            removeses()
            time.sleep(0.5)
            sys.exit()
        elif tmf[0] == 'update':
            try:
                if os.path.exists("/usr/share/Terminator/lib/plugins/update"):
                    os.system('python3 /usr/share/Terminator/lib/plugins/update/install.py')
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Update File Was Removed Or Corrupted!')
            except:
                pass
        elif tmf[0] == 'jobs':
            try:
                if os.path.exists("/usr/share/Terminator/core/session") and os.path.exists("/usr/share/Terminator/core/session/session.yaml"):
                    with open("/usr/share/Terminator/core/session/session.yaml", "r") as host:
                        ip = host.readline()
                        hostname = host.readline()
                        SLHOST = host.readline()
                        SLPORT = host.readline()
                        host.close()
                    job = f'''
Running Jobs
============
Max Jobs. 1

    Job ID
    ------
    1

    Client IP Address        
    -----------------
    {ip}

    Client HostName
    ---------------
    {hostname}

    Server IP Address
    -----------------
    {SLHOST}

    Server Port
    -----------
    {SLPORT}
'''
                else:
                    job = '''
Running Jobs
============
Max Jobs. 1

    Job ID 
    ------

    Client IP Address
    -----------------

    Client HostName
    ---------------

    Server IP Address
    -----------------

    Server Port
    -----------
'''
            except:
                pass
            print(job)
        elif tmf[0] == 'int':
            if len(tmf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Interact With Session Usage: int <Job ID>')
            else:
                try:
                    if tmf[1] == '1':
                        try:
                            if os.path.exists("/usr/share/Terminator/core/session/session.yaml"):
                                print(Fore.BLUE+'[*]'+Fore.RESET+' Interacting With Session 1...')
                                os.system(f'python3 /usr/share/Terminator/core/helpers/int.py {SLHOST}')
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Error Unable To Interact!')
                        except:
                            pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Number: "'+tmf[1]+'"')
                except:
                    pass
        elif tmf[0] == 'jkill':
            if len(tmf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please Specify Job To Kill')
            else:
                try:
                    if tmf[1] == '1':
                        try:
                            if os.path.exists("/usr/share/Terminator/core/session/session.yaml"):
                                print(Fore.RED+'[-]'+Fore.RESET+' Killed Job: 1')
                                os.system('rm -rf /usr/share/Terminator/core/session > /dev/null 2>&1')
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Unable To Kill Session 1, Session Not Exists')
                        except:
                            pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Number: "'+tmf[1]+'"')
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
                    elif tmf[1] == 'payloads':
                        print(pylds)
                    else:
                        print(showcommands)
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Command For Show: "'+tmf[1]+'"')
                except:
                    pass
        elif tmf[0] == 'set':
            print(Fore.RED+'[-]'+Fore.RESET+' This Command Is Module Use Only!')
        elif tmf[0] == 'use':
            if len(tmf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please Specify The Module Name')
            else:
                try:
                    if modules == Fore.GREEN+"OK"+Fore.RESET and database == Fore.GREEN+"OK"+Fore.RESET:
                        if tmf[1] == 'multi/handler' or tmf[1] == 'module/multi/handler':
                            time.sleep(0.7)
                            print(Fore.BLUE+'[*]'+Fore.RESET+' Set Default Payload: "payload/win/win_reverse_shell"')
                            os.system('python3 /usr/share/Terminator/lib/data/handlers/handler.py')
                        elif tmf[1] == 'module/online_food_delivery/rce/webshell':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/foodrce.py')
                        elif tmf[1] == 'module/evolution_cms/rce/login_web':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/evo.py')
                        elif tmf[1] == 'module/citadel_web_kit/cred/log':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/citadel_web.py')
                        elif tmf[1] == 'module/packet_sniff/http/sniff':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/other/http.py')
                        elif tmf[1] == 'module/patient_appointment/sys/web':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/arey.py')
                        elif tmf[1] == 'module/rental_unit/storage/shell':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/unit.py')
                        elif tmf[1] == 'module/blueman/bluetooth_dos/l2ping':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/other/blueman.py')
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Invalid Module: "'+tmf[1]+'"')
                    else:
                        time.sleep(0.5)
                        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Load Modules!')
                except:
                    pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Unknown Command: "'+tmf[0]+'"')
        try:
            tmf = input('\033[4mtmf\033[0m > ').strip(" ")
        except KeyboardInterrupt:
            print('')
            print(Fore.RED+'[-]'+Fore.RESET+' Terminator Stopped...')
            removeses()
            time.sleep(0.5)
            exit()
        tmf = tmf.split()

if __name__ == "__main__":
    main()
