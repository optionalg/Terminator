import os
import time
import subprocess
import random
import sys
import colorama
import pickle
from colorama import Fore, Style, Back
import datetime
import getpass
import future
from sys import platform
import socket
from socket import AF_INET, SOCK_STREAM
colorama.init()
# Inside Plugin Database
plugins_ld = 0
removable = {
    'cclean': '/usr/share/Terminator/lib/plugins/global/plugins/tmf.cclean'
}
plugins = {
    'cclean': '/usr/share/Terminator/lib/plugins/global/plugins/tmf.cclean'
}
# Plugin Read
pl_command = []
pl_run_db = []
pl_run = {}
pl = os.listdir('/usr/share/Terminator/lib/plugins/global/plugins')
for i in pl:
    plugins_ld+=1
plg = f'''
Plugins Loaded: {plugins_ld}
Plugins Marketplace
===================

    Plugins
    -------
    Name        : cclean
    Author      : G00Dway
    Description : a plugin to clean database
    File        : tmf.cclean
    Setup, etc. : Support
    =============================================
'''
if pl:
    for i in pl:
        if i in plugins:
            pass
        else:
            try:
                if os.path.exists('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/desc.yaml'):
                    with open('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/desc.yaml', 'r') as plugin_desc:
                        desc = plugin_desc.read()
                        plugin_desc.close()
                    if desc in pl_command:
                        pass
                    else:
                        pl_command.append(desc)
                else:
                    pass
                if os.path.exists('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/cmd.yaml'):
                    with open('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/cmd.yaml', 'r') as plugin_run:
                        run = plugin_run.read()
                        plugin_run.close()
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+f' Unable To Load Plugin "{i}"')
                if os.path.exists('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/all.yaml'):
                    with open('/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/all.yaml', 'r') as plugin_write:
                        name = "??"
                        author = "??"
                        description = "??"
                        for line in plugin_write:
                            if 'name=' in line:
                                name = line
                                name = name.split('name=')
                                name = name[1].split('\n')
                            elif 'author=' in line:
                                author = line
                                author = author.split('author=')
                                author = author[1].split('\n')
                            elif 'desc=' in line:
                                description = line
                                description = description.split('desc=')
                                description = description[1].split('\n')
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+f' Error Loading Plugin "{i}" Dependencies...')
                        removable[name[0]] = '/usr/share/Terminator/lib/plugins/global/plugins/'+i
                        if name[0] in removable:
                            pass
                        else:
                            removable[run] = '/usr/share/Terminator/lib/plugins/global/plugins/'+i
                        plg += f'''
        Name        : {name[0]}
        Author      : {author[0]}
        Description : {description[0]}
        File        : {i}
        Setup, etc. : Doesnt Support
        =============================================
        '''
                        pl_run[run] = '/usr/share/Terminator/lib/plugins/global/plugins/'+i+'/run.py'
                else:
                    pass
                if os.path.exists("/usr/share/Terminator/core/logs/plugins.log"):
                    with open('/usr/share/Terminator/core/logs/plugins.log', 'w') as load_pl:
                        load_pl.write(i) 
                        load_pl.close()
                else:
                    os.system('touch /usr/share/Terminator/core/logs/plugins.log > /dev/null 2>&1')

            except:
                pass
else:
    pass

module_name = ""
payload_name = ""
user = getpass.getuser()
try:
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
    result_pl = 2
    make = os.listdir('/usr/share/Terminator/modules')
    for i in make:
        if "payloads" in i:
            ex_pl = os.listdir('/usr/share/Terminator/modules/'+i)
            for e_pl in ex_pl:
                result_pl+=1
        elif "readme.md" in i:
            pass
        else:
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
plugin_commands = ''''''
try:
    for i in pl_command:
        if 'clean' in i:
            plugin_commands+=i
        else:
            plugin_commands+='\n    '+i
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/lib/plugins/update"):
        updater = Fore.GREEN+"OK"+Fore.RESET
    else:
        updater = Fore.RED+"FATAL"+Fore.RESET
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/VERSION"):
        with open("/usr/share/Terminator/VERSION", "r") as tmf_ver:
            version = tmf_ver.read()
    else:
        print(Fore.RED+'[-]'+Fore.RESET+" Error: Version Could Not Be Detected")
        version = "UNKNOWN"
except:
    pass
build = '11654.stable'
setup_v = '1.6.6'
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
    about                         About framework, etc.
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
    setup <name>                  Setup specified plugin (Only for inside Terminator plugins!)
    remove <name>                 Remove specified plugin

Plugins Installed
=================

    Command                       Description
    -------                       -----------
    {plugin_commands}
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
mdls = '''
#    Module Name                                     Type               Verify          Description
-    ------------                                    -----              -------         ------------
1    module/multi/handler                            Handler            yes             Handler For Payloads
2    module/packet_sniff/http/sniff                  Local              yes             HTTP/HTTPS Packet Sniffer
3    module/blueman/bluetooth_dos/l2ping             Local              yes             Bluetooth Denial Of Service Module
4    module/online_food_delivery/rce/webshell        Web/RCE            yes             RCE, WebShell Upload & Execute Command
5    module/evolution_cms/rce/login_web              Web/RCE            no              CMS RCE, Login & Execute Command
6    module/citadel_web_kit/cred/log                 Web                yes             Citadel Web kit, Credential Harvester Module
7    module/patient_appointment/sys/web              Web/RCE            no              RCE, WebShell Upload & Command Execute
8    module/rental_unit/storage/shell                Web/RCE            no              RCE, WebShell Upload & Reverse TCP    
9    module/online_learn/rce/shell                   Web/RCE            no              RCE, Advanced WebShell Upload & BruteForcer
10   module/port_scan/local/scan                     Local              yes             Port Scanner, Advanced IPY Port Scanner
11   module/apache/apache_web/rce                    Web/RCE            no              Apache Web RCE, Advanced Apache Vulnerability Scanner
12   module/gerapy/log/rce_shell                     Web/RCE            yes             RCE, Login & Upload WebShell
13   module/slr/120/shell_rce                        Web/RCE/CMD        no              RCE, Execute Commands Without Authentication (Router)
'''
search_modules = '''
module/multi/handler
module/packet_sniff/http/sniff
module/blueman/bluetooth_dos/l2ping
module/online_food_delivery/rce/webshell
module/evolution_cms/rce/login_web
module/citadel_web_kit/cred/log    
module/patient_appointment/sys/web             
module/rental_unit/storage/shell                  
module/online_learn/rce/shell                   
module/port_scan/local/scan                     
module/apache/apache_web/rce                    
module/gerapy/log/rce_shell 
module/slr/120/shell_rce
'''
pylds = '''
Payload Name                                    Type             Verify          Description
-------------                                   -----            -------         ------------
payload/poc/redragon_mouse/wr                   Windows          no              Redragon_Mouse Payload (REDRAGON_MOUSE.sys)
payload/win/win_reverse_shell                   Windows          yes             reverse shell Payload (win32, win64)
payload/apk/android_reverse_shell               Android          yes             reverse shell Payload (V.3 - 9)
'''
search_payloads = '''
payload/poc/redragon_mouse/wr                   
payload/win/win_reverse_shell                 
payload/apk/android_reverse_shell
'''
def search(type, name):
    count = 0
    modules_list = '''
'''
    payloads = '''
'''
    try:
        if type == 'module':
            for line in search_modules.split('\n'):
                if name in line:
                    count+=1
                    line4 = line.replace(name, Back.MAGENTA+name+Back.RESET)
                    modules_list+=line4+'\n'
            if count == 0:
                print(Fore.RED+'[-]'+Fore.RESET+' No Results Found.')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+f' Found {count} Results')
                print('---------------------------')
                print(modules_list)
        elif type == 'payload':
            for line2 in search_payloads.split('\n'):
                if name in line2:
                    count+=1
                    line3 = line2.replace(name, Back.MAGENTA+name+Back.RESET)
                    payloads+=line3+'\n'
            if count == 0:
                print(Fore.RED+'[-]'+Fore.RESET+' No Results Found.')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+f' Found {count} Results')
                print('---------------------------')
                print(payloads)
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
try:
    with open("/usr/share/Terminator/core/base/ui/banners/out/banner.txt", "r") as banner_selected:
        banner_load = banner_selected.read()
except Exception:
    pass
tips = ['INFO: After Updating, Terminator Saves '+Fore.GREEN+'old'+Fore.RESET+' Database At: "/usr/var/tmf-meta-inf"!', 'HINT: Terminator Runs Slow? Why Not Try The (Plugin) '+Fore.GREEN+'clean'+Fore.RESET+' Command!', 'INFO: Always Keep Terminator Up-To-Date!', 'HINT: While in Module, You Can Use '+Fore.GREEN+'back'+Fore.RESET+' Command To Exit from Module use!', 'HINT: To Kill Running Handler Jobs, Use '+Fore.GREEN+'jkill <Job ID>'+Fore.RESET, 'HINT: To Interact With Handler Jobs, Use '+Fore.GREEN+'int <Job ID>'+Fore.RESET, 'HINT: You can Change Settings Under "/usr/share/Terminator/core/base/extra/'+Fore.GREEN+'settings.ini'+Fore.RESET+'"', 'HINT: You Can Add Your Own Plugins At: "/usr/share/Terminator/lib/plugins/global/'+Fore.GREEN+'plugins"'+Fore.RESET+' Directory!']
def banner():
    print(banner_load)
    print(f"""
     --=[ Modules loaded: {result} | Payloads loaded: {result_pl}""")
    

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
        elif tmf[0] == 'about':
            try:
                if os.path.exists('/usr/share/Terminator/core/logs/time.log'):
                    with open('/usr/share/Terminator/core/logs/time.log', 'r') as s:
                        update_v = s.readline()
                        s.close()
                else:
                    update_v = 'Unknown'
            except:
                pass
            about = f'''
              About
=================================
Framework          : Terminator Framework Build {build}
Version            : {version}{Fore.RESET}
Setup Version      : {setup_v}
Last Update Check  : {update_v}
Modules Loaded     : {result}
Payloads Loaded    : {result_pl}
Plugins Loaded     : {plugins_ld}
Author             : G00Dway
Organization       : HackNET Community
Country            : Azerbaijan

           Social Links
==================================
Discord            : Join HackNET Community! - {Fore.GREEN}https://discord.gg/cKTkTRW48P{Fore.RESET}
TikTok             : Watch our Latest News! - {Fore.GREEN}HackNET - Azerbaijan (@hacknet_azerbaijan){Fore.RESET}
'''
            print(about)
        elif tmf[0] == 'banner':
            banner()
        elif tmf[0] == 'exit' or tmf[0] == 'quit':
            print(Fore.RED+'[-]'+Fore.RESET+' Terminator Stopped...')
            removeses()
            time.sleep(0.5)
            sys.exit()
        elif tmf[0] == 'update':
            day = datetime.datetime.now()
            now = day.strftime("(%D) At: %H:%M:%S")
            try:
                if os.path.exists("/usr/share/Terminator/core/logs/time.log"):
                    with open("/usr/share/Terminator/core/logs/time.log", "w") as t:
                        t.write(now)
                        t.close()
                else:
                    os.system('touch /usr/share/Terminator/core/logs/time.log > /dev/null 2>&1')
                    with open("/usr/share/Terminator/core/logs/time.log", "w") as t:
                        t.write(now)
                        t.close()
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
        elif tmf[0] == 'use':
            if len(tmf) < 2:
                print(Fore.RED+'[-]'+Fore.RESET+' Please Specify The Module Name')
            else:
                try:
                    if modules == Fore.GREEN+"OK"+Fore.RESET and database == Fore.GREEN+"OK"+Fore.RESET:
                        if tmf[1].isdigit():
                            print(Fore.BLUE+'[*]'+Fore.RESET+f' Loading Module Number {tmf[1]} Assigments...')
                        else:
                            print(Fore.BLUE+'[*]'+Fore.RESET+' Loading Module "'+tmf[1]+'" Assigments...')
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
                        elif tmf[1] == 'module/gerapy/log/rce_shell' or tmf[1] == '12':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/gr.py')
                        elif tmf[1] == 'module/slr/120/shell_rce' or tmf[1] == '13':
                            time.sleep(0.5)
                            os.system('python3 /usr/share/Terminator/lib/data/exploits/slr-c.py')
                        else:
                            if tmf[1].isdigit():
                                print(Fore.RED+'[-]'+Fore.RESET+' Unable To Load Module Number: '+tmf[1])
                                print(Fore.RED+'[-]'+Fore.RESET+' Please Enter a Valid Module Number!')
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Unable To Load Module: "'+tmf[1]+'"')
                                print(Fore.RED+'[-]'+Fore.RESET+' Please Enter a Valid Module Name!')
                        if tmf[1].isdigit():
                            print(Fore.BLUE+'[*]'+Fore.RESET+' Closed Module Number: '+tmf[1])
                        else:
                            print(Fore.BLUE+'[*]'+Fore.RESET+' Closed Module: "'+tmf[1]+'"')
                    else:
                        time.sleep(0.5)
                        print(Fore.RED+'[-]'+Fore.RESET+' Unable To Load Modules!')
                except:
                    pass
        elif tmf[0] == 'plugins':
            print(Fore.BLUE+'[*]'+Fore.RESET+' Loading Plugins...')
            time.sleep(0.2)
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
                                if name == 'cclean':
                                    os.mkdir(dir)
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

                                time.sleep(0.3)
                                print(Fore.YELLOW+'[+]'+Fore.RESET+' Setup For Plugin '+Fore.GREEN+f'{name}'+Fore.RESET+' Completed.')
                                print(Fore.BLUE+'[*]'+Fore.RESET+' Please Restart Terminator To Load All Plugins Correctly!')
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
                    if name_rem in removable:
                        dir_rem = removable[name_rem]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' Removing Plugin '+Fore.GREEN+f'{name_rem}'+Fore.RESET+'...')
                        try:
                            if os.path.exists(dir_rem):
                                if name_rem == 'cclean':
                                    time.sleep(0.3)
                                    os.system('rm -rf '+dir_rem+' > /dev/null 2>&1')
                                else:
                                    os.system('rm -rf '+dir_rem+' > /dev/null 2>&1')

                                print(Fore.YELLOW+'[+]'+Fore.RESET+' Plugin '+Fore.GREEN+f'{name_rem}'+Fore.RESET+' Removed.')
                                print(Fore.BLUE+'[*]'+Fore.RESET+' Please Restart Terminator To Load All Plugins Correctly!')
                            else:
                                print(Fore.RED+'[-]'+Fore.RESET+' Plugin '+Fore.GREEN+f'{name_rem}'+Fore.RESET+' Is Not Installed.')
                        except:
                            pass
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Invalid Plugin: "'+name_rem+'"')
                except:
                    pass
        elif tmf[0] in pl_run:
            key = pl_run[tmf[0]]
            print(Fore.BLUE+'[*]'+Fore.RESET+' Detected Plugin '+Fore.GREEN+''+tmf[0]+''+Fore.RESET+'...')
            print(Fore.BLUE+'[*]'+Fore.RESET+' Running Plugin '+Fore.GREEN+''+tmf[0]+''+Fore.RESET+'...')
            time.sleep(0.3)
            os.system('python3 '+key)
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
