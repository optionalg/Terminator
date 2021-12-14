from __future__ import print_function
import optparse
import socket
import concurrent.futures
from socket import *
import sys
from threading import *
import threading
import colorama
from colorama import Fore
if len(sys.argv) < 2:
    sys.exit()


ip = sys.argv[1]
print(Fore.BLUE+'[*]'+Fore.RESET+f' Scanning {ip}')

print_lock = threading.Lock()
def scan(ip, port):
    scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    scanner.settimeout(1)
    try:
        scanner.connect((ip, port))
        scanner.close()
        with print_lock:
            print(Fore.YELLOW+'[+]'+Fore.RESET+f' {ip}: Port {port} Opened')
    except:
        pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
    for port in range(1000):
        executor.submit(scan, ip, port + 1)