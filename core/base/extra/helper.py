import argparse
import os
import time
import colorama
from colorama import Fore
memory = memoryview()
db = "/usr/share/Terminator"
try:
    print('')
    error_got = []
    with open("/usr/share/Terminator/core/logs/logs.log", "r") as error:
        for line in error:
            if 'FATAL' in line:
                error_got.append(line)
                print(Fore.RED+"[-]"+Fore.RESET+" Got Error In Logs: "+line)
except:
    pass