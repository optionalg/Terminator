import sys
import pathlib
import time
import colorama
from colorama import Fore
import subprocess
import os
import random
from subprocess import *
colorama.init()
help_menu = '''
Terminator Framework Database Commands
======================================

        Command                 Description
        -------                 -----------
        tmdb start              Start the database
        tmdb stop               Stop the database
        tmdb status             Check status of the database
'''
if len(sys.argv) < 2:
    print(help_menu)
    sys.exit()

cmd = sys.argv[1]

try:
    if os.path.exists("/usr/share/Terminator/databases/config/logs"):
        pass
    else:
        os.mkdir("/usr/share/Terminator/databases/config/logs")
except:
    print(Fore.RED+'[-]'+Fore.RESET+' Unable to Create database...')
    sys.exit()
try:
    if cmd == "start":
        try:
            if os.path.exists("/usr/share/Terminator/databases/config/run/start"):
                with open("/usr/share/Terminator/databases/config/run/start", "r") as f_2:
                    get = f_2.read()
                if get == 'load = True':
                    print(Fore.YELLOW+'[+]'+Fore.RESET+' Database Already Running')
                    sys.exit()
                elif get == 'load = False':
                    pass
            else:
                pass
        except:
            pass
        print(Fore.BLUE+'[*]'+Fore.RESET+' Starting Database')
        time.sleep(2)
        try:
            subprocess.call(['python3', '/usr/share/Terminator/databases/config/run/dbload.py', '--start'])
        except Exception:
            print(Fore.RED+'[-]'+Fore.RESET+' Unable To Start Database')
            sys.exit()
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Database Started')
    elif cmd == "stop":
        try:
            if os.path.exists("/usr/share/Terminator/databases/config/run/start"):
                with open("/usr/share/Terminator/databases/config/run/start", "r") as f:
                    get = f.read()
                if get == 'load = True':
                    print(Fore.BLUE+'[*]'+Fore.RESET+' Stopping Database')
                elif get == 'load = False':
                    print(Fore.YELLOW+'[+]'+Fore.RESET+' Database Already Stopped')
                    sys.exit()
            else:
                print(Fore.YELLOW+'[+]'+Fore.RESET+' Database Already Stopped')
                sys.exit()
        except:
            pass
        time.sleep(2)
        try:
            subprocess.call(['python3', '/usr/share/Terminator/databases/config/run/dbload.py', '--stop'])
        except Exception:
            print(Fore.RED+'[-]'+Fore.RESET+' Unable To Stop Database')
            sys.exit()
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Database Stopped')
    elif cmd == "status":
        try:
            if os.path.exists("/usr/share/Terminator/databases/config/run/start"):
                print(Fore.BLUE+'[*]'+Fore.RESET+' Database Is Running')
            else:
                print(Fore.RED+'[-]'+Fore.RESET+' Database Is NOT Running')
        except:
            pass
	elif cmd == 'help':
		print(help_menu)
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unrecognized Command: "'+cmd+'"')
except:
    pass
