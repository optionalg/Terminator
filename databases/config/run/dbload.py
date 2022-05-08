import subprocess
import socket
import os
import sys
import time
import colorama
import random
from colorama import Fore
colorama.init()
port = random.randint(1000, 5000)
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
if len(sys.argv) < 2:
    sys.exit()

cmd = sys.argv[1]

if cmd == "--start":
    try:
        os.system('touch "/usr/share/Terminator/databases/config/run/start" > /dev/null 2>&1')
        with open("/usr/share/Terminator/databases/config/run/start", "w") as f:
            f.write("load = True")
        s.connect(f"127.0.0.1:{port}")
    except Exception as e:
        print(Fore.RED+'[-]'+Fore.RESET+' Error: Unable connect to database, exiting...')
        print(Fore.RED+'[-]'+Fore.RESET+' Error: '+e)
        sys.exit()
elif cmd == "--stop":
    try:
        with open("/usr/share/Terminator/databases/config/run/start", "w") as f2:
            f2.write("load = False")
        print(Fore.BLUE+'[*]'+Fore.RESET+' Using PKILL...')
        subprocess.call(['pkill', '-e', "'python3 /usr/share/Terminator/databases/config/run/dbload.py --start'"])
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Done.')
    except Exception:
        print(Fore.RED+'[-]'+Fore.RESET+' Database Stopped but Process running.')
        sys.exit()
else:
    sys.exit()
sys.exit()
