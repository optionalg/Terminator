import os
import time
import colorama
import sys
import subprocess
from colorama import Fore
colorama.init()
IP_ADDR=""
PORT_RANGE=""
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
    tmf = input('\033[4mtmf\033[0m-('+Fore.RED+'port_scan/local/scan'+Fore.RESET+') > ').strip(" ")
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
Module ('''+Fore.RED+'''port_scan/local/scan'''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------
      IP_ADDR         Required          IP Address Of Device               '''+IP_ADDR+'''
      PORT_RANGE      Required          Port Range (E.g <int>-<int>)       '''+PORT_RANGE+'''

Module About:

      Module Title : Port Scanner
      Author       : G00Dway
      Version      : 0.2

Module Details:

      This Module Has No Details.
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
                if tmf[1] == 'IP_ADDR' or tmf[1] == 'ip_addr':
                    IP_ADDR=tmf[2]
                    print(Fore.BLUE+'[*]'+Fore.RESET+' IP_ADDR ==> '+IP_ADDR)
                elif tmf[1] == 'PORT_RANGE' or tmf[1] == 'port_range':
                    PORT_RANGE=tmf[2]
                    print(Fore.BLUE+'[*]'+Fore.RESET+' PORT_RANGE ==> '+PORT_RANGE)
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
            except:
                pass
    elif tmf[0] == 'run':
        if IP_ADDR == "" or PORT_RANGE == "":
            print(Fore.RED+'[-]'+Fore.RESET+' Please Set Options First!')
        else:
            try:
                os.system('python3 /usr/share/Terminator/modules/other/nmap.py '+IP_ADDR+' '+PORT_RANGE)
                print(Fore.BLUE+'[*]'+Fore.RESET+' Module Execution Completed.')
            except Exception:
                pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unknown Command: "'+tmf[0]+'"')
    try:
        tmf = input('\033[4mtmf\033[0m-('+Fore.RED+'port_scan/local/scan'+Fore.RESET+') > ').strip(" ")
    except KeyboardInterrupt:
        exit()
    tmf = tmf.split()
