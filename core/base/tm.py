import os
import time
import subprocess
import random
import sys
import colorama
import pickle
from colorama import Fore, Style, Back
import getpass
import future
from sys import platform
import socket
from socket import AF_INET, SOCK_STREAM
colorama.init()
# Plugin Read
pl_command = '''
'''
pl_run = {

}
pl = os.listdir('/usr/share/Terminator/lib/plugins/global/plugins')
if pl:
    for i in pl:
        try:
            if os.path.exists('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/desc.yaml'):
                with open('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/desc.yaml', 'r') as plugin_desc:
                    desc = plugin_desc.read()
                    plugin_desc.close()
                if desc in pl_command:
                    pass
                else:
                    pl_command += desc+'\n'
            else:
                print(Fore.RED+'[-]'+Fore.RESET+f' Unable To Load Plugin "{i}"')
            if os.path.exists('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/cmd.yaml'):
                with open('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/cmd.yaml', 'r') as plugin_run:
                    run = plugin_run.read()
                    plugin_run.close()
                if run == 'clean':
                    pass
                else:
                    pl_run[run] = '/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/run.py'
        except:
            pass
else:
    pass
        


# Plugin Names
cc_verify = ""

# Inside Plugin Database
plugins = {
    'cclean': '/usr/share/Terminator/lib/plugins/global/plugins/tmf.cclean'
}
try:
    if os.path.exists("/usr/share/Terminator/lib/plugins/global/plugins/tmf.cclean"):
        cc_verify = "Installed"
    else:
        cc_verify = "Not Installed"
except:
    pass




plg = f'''
Plugins Marketplace
Plugins: 1
===================

    Plugins
    -------
    Name        : cclean
    Author      : G00Dway
    Description : a plugin to clean database
    File        : tmf.cclean
    Download    : Not Needed
    Plugin      : {cc_verify}
    =============================================
'''
module_name = ""
payload_name = ""
user = getpass.getuser()
try:
    print('')
    error_num = 0
    error_got = []
    with open("/usr/share/Terminator/core/logs/logs.log", "r") as error:
        for line in error:
            if 'FATAL' in line:
                error_num += 1
                error_got.append(line)
        if error_got == []:
            pass
        else:
            print(Fore.RED+'[-]'+Fore.RESET+' Errors Detected In Logs: '+error_num)
            error_num = 1
            for i in error_got:
                print(Fore.RED+'[-]'+Fore.RESET+f' Error ({error_num}): '+i)
                error_num += 1
except:
    pass
try:
    result = 0
    make = os.listdir('/usr/share/Terminator/modules')
    for i in make:
        ex = os.listdir('/usr/share/Terminator/modules/'+i)
        for e in ex:
            result+=1
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
    if os.path.exists("/usr/share/Terminator/lib/plugins/update"):
        updater = Fore.GREEN+"OK"+Fore.RESET
    else:
        updater = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
version = "1.8.5.9"+Fore.LIGHTBLACK_EX+"#stable"
commands = f'''
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

Search Commands
===============
    
    Command                       Description
    -------                       -----------
    search module <name>          Search a module by name
    search payload <name>         Search a payload by name

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
    banner                        Show banner
    update                        Update Terminator framework
    show <>                       Show specified command
    use <module>                  Use specified Module
    set <option> <value>          Set specified option to specified value (Module use only)
    run                           Run the Module (Module use only)
    exit                          Exit from Terminator

Plugin Commands
===============

    Command                       Description
    -------                       -----------
    plugins                       Show all available plugins
    setup <name>                  Setup specified plugin
    remove <name>                 Remove specified plugin

Plugins Installed
=================

    Command                       Description
    -------                       -----------
    {pl_command}
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
#    Module Name                                     Type             Verify          Description
-    ------------                                    -----            -------         ------------
1    module/multi/handler                            Handler          yes             Handler For Payloads
2    module/packet_sniff/http/sniff                  Local            yes             HTTP/HTTPS Packet Sniffer
3    module/blueman/bluetooth_dos/l2ping             Local            no              Bluetooth Denial Of Service Module
4    module/online_food_delivery/rce/webshell        Web/RCE          yes             RCE, WebShell Upload & Execute Command
5    module/evolution_cms/rce/login_web              Web/RCE          no              CMS RCE, Login & Execute Command
6    module/citadel_web_kit/cred/log                 Web              yes             Citadel Web kit, Credential Harvester Module
7    module/patient_appointment/sys/web              Web/RCE          no              RCE, WebShell Uplaod & Command Execute
8    module/rental_unit/storage/shell                Web/RCE          no              RCE, WebShell Upload & Reverse TCP    
9    module/online_learn/rce/shell                   Web/RCE          no              RCE, Advanced WebShell Upload & BruteForcer
10   module/port_scan/local/scan                     Local            yes             Port Scanner, Advanced IPY Port Scanner
11   module/apache/apache_web/rce                    Web/RCE          no              Apache Web RCE, Advanced Apache Vulnerability Scanner
'''
pylds = '''
Payload Name                                    Type             Verify          Description
-------------                                   -----            -------         ------------
payload/poc/redragon_mouse/wr                   Windows          no              Redragon_Mouse Payload (REDRAGON_MOUSE.sys)
payload/win/win_reverse_shell                   Windows          yes             reverse shell Payload (win32, win64)
payload/apk/android_reverse_shell               Android          yes             reverse shell Payload (V.3 - 9)
'''
def search(type, name):
    count = 0
    modules_list = '''
#    Module Name                                     Type             Verify          Description
-    ------------                                    -----            -------         ------------
'''
    payloads = '''
Payload Name                                    Type             Verify          Description
-------------                                   -----            -------         ------------
'''
    try:
        if type == 'module':
            for line in mdls.split('\n'):
                if name in line:
                    count+=1
                    modules_list+=line+'\n'
            print(modules_list)
            if count == 0:
                print(Fore.RED+'[-]'+Fore.RESET+' No Results Found.')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+f' Found {count} Results')
        elif type == 'payload':
            for line2 in pylds.split('\n'):
                if name in line2:
                    count+=1
                    payloads+=line2+'\n'
            print(payloads)
            if count == 0:
                print(Fore.RED+'[-]'+Fore.RESET+' No Results Found.')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+f' Found {count} Results')
        else:
            pass
    except:
        pass
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
tips = ['INFO: After Updating, Terminator Saves '+Fore.GREEN+'old'+Fore.RESET+' Database At: "/usr/var/tmf-meta-inf"!', 'HINT: Terminator Runs Slow? Why Not Try The '+Fore.GREEN+'clean'+Fore.RESET+' Command!', 'INFO: Always Keep Terminator Up-To-Date!', 'HINT: While in Module, You Can Use '+Fore.GREEN+'back'+Fore.RESET+' Command To Exit from Module use!', 'HINT: To Kill Running Handler Jobs, Use '+Fore.GREEN+'jkill <Job ID>'+Fore.RESET, 'HINT: To Interact With Handler Jobs, Use '+Fore.GREEN+'int <Job ID>'+Fore.RESET, 'HINT: You can Change Settings Under "/usr/share/Terminator/core/base/extra/'+Fore.GREEN+'settings.ini'+Fore.RESET+'"', 'HINT: You Can Add Your Own Plugins At: '+Fore.GREEN+'"/usr/share/Terminator/lib/plugins/global/plugins"'+Fore.RESET+' Directory!']
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
      <[ Version           {version} '''+Fore.RESET+f''']
      <[ Modules Loaded                {result} ]
''')
banner()
print(random.choice(tips))
print('')
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
            try:
                if os.path.exists("/usr/share/Terminator/lib/plugins/global/plugins/tmf.cclean"):
                    print(Fore.BLUE+'[*]'+Fore.RESET+' Cleaning Database...')
                    time.sleep(0.2)
                    os.system('python3 /usr/share/Terminator/lib/plugins/global/plugins/tmf.cclean/run.py')
                    print(Fore.BLUE+'[*]'+Fore.RESET+' Completed.')
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Unknown Command: "'+tmf[0]+'"')
            except:
                pass
        elif tmf[0] == 'clear':
            os.system('clear')
        elif tmf[0] == 'banner':
            banner()
        elif tmf[0] in pl_run:
            key = pl_run[tmf[0]]
            print(Fore.BLUE+'[*]'+Fore.RESET+' Running Plugin '+Fore.GREEN+''+tmf[0]+''+Fore.RESET+'...')
            time.sleep(0.3)
            os.system('python3 '+key)
        elif tmf[0] == 'exit' or tmf[0] == 'quit':
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
        elif tmf[0] == 'search':
            if len(tmf) < 3:
                print(Fore.RED+'[-]'+Fore.RESET+' Usage: search <type> <name>')
                print(Fore.RED+'[-]'+Fore.RESET+' Valid Types: ("module", "payload")')
            else:
                try:
                    if tmf[1] == 'module':
                        if tmf[2] == '':
                            print(Fore.RED+'[-]'+Fore.RESET+' Please Enter a Module Name!')
                        else:
                            module_name = tmf[2]
                            search('module', module_name)
                    elif tmf[1] == 'payload':
                        if tmf[2] == '':
                            print(Fore.RED+'[-]'+Fore.RESET+' Please Enter a Payload Name!')
                        else:
                            payload_name = tmf[2]
                            search('payload', payload_name)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Valid Types: ("module", "payload")')
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
                        if tmf[1] == 'multi/handler' or tmf[1] == 'module/multi/handler' or tmf[1] == '1':
                            time.sleep(0.7)
                            print(Fore.BLUE+'[*]'+Fore.RESET+' Set Default Payload: "payload/win/win_reverse_shell"')
                            os.system('python3 /usr/share/Terminator/lib/data/handlers/handler.py')
                        elif tmf[1] == 'module/online_food_delivery/rce/webshell' or tmf[1] == '4':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/foodrce.py')
                        elif tmf[1] == 'module/evolution_cms/rce/login_web' or tmf[1] == '5':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/evo.py')
                        elif tmf[1] == 'module/citadel_web_kit/cred/log' or tmf[1] == '6':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/citadel_web.py')
                        elif tmf[1] == 'module/packet_sniff/http/sniff' or tmf[1] == '2':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/other/http.py')
                        elif tmf[1] == 'module/patient_appointment/sys/web' or tmf[1] == '7':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/arey.py')
                        elif tmf[1] == 'module/rental_unit/storage/shell' or tmf[1] == '8':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/unit.py')
                        elif tmf[1] == 'module/blueman/bluetooth_dos/l2ping' or tmf[1] == '3':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/other/blueman.py')
                        elif tmf[1] == 'module/online_learn/rce/shell' or tmf[1] == '9':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/online.py')
                        elif tmf[1] == 'module/port_scan/local/scan' or tmf[1] == '10':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/other/port.py')
                        elif tmf[1] == 'module/apache/apache_web/rce' or tmf[1] == '11':
                            time.sleep(0.3)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/ap.py')
                        else:
                            print(Fore.RED+'[-]'+Fore.RESET+' Invalid Module Number/Name: "'+tmf[1]+'"')
                    else:
                        time.sleep(0.5)
                        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Load Modules!')
                except:
                    pass
        elif tmf[0] == 'plugins':
            print(plg)
        elif tmf[0] == 'setup':
            if len(tmf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Usage: setup <name>')
            else:
                try:
                    name = tmf[1]
                    if name in plugins:
                        dir = plugins[name]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' Setting Up Plugin '+Fore.GREEN+f'{name}'+Fore.RESET+'...')
                        time.sleep(0.5)
                        try:
                            if os.path.exists(dir):
                                print(Fore.RED+'[-]'+Fore.RESET+' Plugin '+Fore.GREEN+f'{name}'+Fore.RESET+' Already Setup.')
                            else:
                                os.mkdir(dir)
                                if name == 'cclean':
                                    global cc_verify
                                    cc_verify = "Installed"
                                    os.system('cp -r /usr/share/Terminator/core/base/extra/scripts/cln.py '+dir+' > /dev/null 2>&1')
                                    os.system('mv '+dir+'/cln.py '+dir+'/run.py > /dev/null 2>&1')
                                    os.system('touch '+dir+'/desc.yaml > /dev/null 2>&1')
                                    os.system('touch '+dir+'/cmd.yaml > /dev/null 2>&1')
                                    with open(dir+'/desc.yaml', 'w') as f:
                                        f.write('clean                         Clean database logs, cache')
                                        f.close()
                                    with open(dir+'/cmd.yaml', 'w') as f2:
                                        f2.write('clean')
                                        f2.close()
                                else:
                                    os.system('python3 '+dir+'/setup.py')
                                time.sleep(0.3)
                                print(Fore.YELLOW+'[+]'+Fore.RESET+' Setup For Plugin '+Fore.GREEN+f'{name}'+Fore.RESET+' Completed.')
                        except:
                            pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Plugin: "'+name+'"')
                except:
                    pass
        elif tmf[0] == 'remove':
            if len(tmf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Usage: remove <name>')
            else:
                try:
                    name_rem = tmf[1]
                    if name_rem in plugins:
                        dir = plugins[name_rem]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' Removing Plugin '+Fore.GREEN+f'{name}'+Fore.RESET+'...')
                        try:
                            if os.path.exists(dir):
                                if name_rem == 'cclean':
                                    global cc_verify
                                    os.system('rm -rf '+dir+' > /dev/null 2>&1')
                                    cc_verify = "Not Installed"
                                else:
                                    time.sleep(0.5)
                                    os.system('python3 '+dir+'/remove.py')
                                print(Fore.YELLOW+'[+]'+Fore.RESET+' Plugin '+Fore.GREEN+f'{name}'+Fore.RESET+' Removed.')
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Plugin '+Fore.GREEN+f'{name}'+Fore.RESET+' Is Not Installed.')
                        except:
                            pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Plugin: "'+name+'"')
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
