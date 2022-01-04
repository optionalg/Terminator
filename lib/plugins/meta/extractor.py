import os
import sys
import colorama
from colorama import Fore
import random
import string
import time
colorama.init()
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
        if os.path.exists("/usr/share/Terminator"):
            if os.path.exists("/usr/share/Terminator/core/logs/meta"):
                if os.path.exists('/usr/share/Terminator/core/logs/meta/Terminator.zip'):
                    os.system('rm -rf /usr/share/Terminator/core/logs/meta/Terminator.zip > /dev/null 2>&1')
                    install()
                else:
                    os.system('cp -r /usr/share/Terminator /usr/share/Terminator/core/logs/meta > /dev/null 2>&1')
                    os.system('mv /usr/share/Terminator/core/logs/meta/Terminator /usr/share/Terminator/core/logs/meta/Terminator.zip > /dev/null 2>&1')
            else:
                os.mkdir('/usr/share/Terminator/core/logs/meta')
                install()
        if os.path.exists("/usr/share/Terminator/core/logs/cache_meta"):
            os.system('rm -rf /usr/share/Terminator/core/logs/cache_meta')
            os.mkdir('/usr/share/Terminator/core/logs/cache_meta')
            extr()
        else:
            os.mkdir('/usr/share/Terminator/core/logs/cache_meta')
            extr()
    except:
        pass

install()
sys.exit()