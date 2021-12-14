import socket
import os
import threading
import sys
import datetime
import colorama
from colorama import Fore
if len(sys.argv) < 2:
    sys.exit()

target = sys.argv[1]
time = datetime.datetime.now()
now = time.strftime("%H:%M:%S")

print(Fore.BLUE+'[*]'+Fore.RESET+' Scanning Device: '+target)
print(Fore.BLUE+'[*]'+Fore.RESET+' Started At: '+now)

ports = []

def scan(port):
    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    socket.setdefaulttimeout(1)
    try:
        connection.connect(target, port)
        connection.close()
        print(Fore.YELLOW+'[+]'+Fore.RESET+f' {target}: Port {port} Is Open')
        ports.append(port)
    except Exception:
        pass

scanned = 1
for port in range(1, 65500):
    thread = threading.Thread(target=scan, kwargs={'port':scanned})
    scanned += 1
    thread.start()

print(Fore.BLUE+'[*]'+Fore.RESET+f' {scanned} Ports Were Scanned.')