# run file
import os
import time
import sys
import colorama
from colorama import Fore
colorama.init()
def clean():
    cache = os.listdir("/usr/share/Terminator/core/base/scripts/cache/libs")
    root_files = os.listdir("/root/.tmf")
    logs = "/usr/share/Terminator/core/logs/logs.log"
    for clr in cache:
        os.system('rm -rf /usr/share/Terminator/core/base/scripts/cache/libs/'+clr+' > /dev/null 2>&1')
    os.system('rm -rf '+logs+' > /dev/null 2>&1')
    for clean_root in root_files:
        os.system('rm -rf /root/.tmf/'+clean_root+' > /dev/null 2>&1')


clean()