import os
import time
import colorama
import sys
import subprocess
from colorama import Fore
colorama.init()
INTERFACE="eth0"
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
    tmf = input('\033[4mtmf\033[0m-('+Fore.RED+'packet_sniff/http/sniff'+Fore.RESET+') > ').strip(" ")
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
Module ('''+Fore.RED+'''packet_sniff/http/sniff'''+Fore.RESET+''') Options:

      Option          Rank              Description                               Current Value
      --------        ------            -------------                             ---------------
      INTERFACE       Required          Interface To Sniff (Default: eth0)        '''+INTERFACE+'''

Module About:

      Module Title : HTTP Packet Sniffer
      Author       : G00Dway
      Version      : 1.233

Module Details:

      Detail 1     : Sniffs Credentials Like - Pass/Emails/Logins/Cookies/etc..
      Detail 2     : Shows All Captured HTTP Packets

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
                if tmf[1] == 'INTERFACE' or tmf[1] == 'interface':
                    INTERFACE=tmf[2]
                    print(Fore.BLUE+'[*]'+Fore.RESET+' INTERFACE ==> '+INTERFACE)
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
            except:
                pass
    elif tmf[0] == 'run':
        if INTERFACE == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Please Set Options First!')
        else:
            try:
                os.system('python3 /usr/share/Terminator/modules/other/sniffer.py -i '+INTERFACE)
                print(Fore.BLUE+'[*]'+Fore.RESET+' Module Execution Completed.')
            except Exception:
                pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unknown Command: "'+tmf[0]+'"')
    try:
        tmf = input('\033[4mtmf\033[0m-('+Fore.RED+'packet_sniff/http/sniff'+Fore.RESET+') > ').strip(" ")
    except KeyboardInterrupt:
        exit()
    tmf = tmf.split()
