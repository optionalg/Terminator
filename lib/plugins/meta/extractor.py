import os
import sys
import colorama
from colorama import Fore
import random
import string
import time
colorama.init()
try:
    os.mkdir('/usr/share/Terminator/core/logs/meta')
    os.mkdir('/usr/share/Terminator/core/logs/cache_meta')
except:
    pass
def extr():
    try:
        os.system('mv /usr/bin/tmconsole /usr/share/Terminator/core/logs/cache_meta > /dev/null 2>&1')
        os.system('chmod +x /usr/share/Terminator/bin/tmconsole/tmconsole > /dev/null 2>&1')
        os.system('cp -r /usr/share/Terminator/bin/tmconsole/tmconsole /usr/bin > /dev/null 2>&1')
        os.system('python3 /usr/share/Terminator/bin/version/ver.py')
    except:
        pass


def install():
    try:
        os.system('cp -r /usr/share/Terminator /usr/share/Terminator/core/logs/meta > /dev/null 2>&1')
        os.system('mv /usr/share/Terminator/core/logs/meta/Terminator /usr/share/Terminator/core/logs/meta/Terminator.zip > /dev/null 2>&1')
        extr()
    except:
        pass

install()
sys.exit()