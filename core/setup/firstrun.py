from genericpath import exists
import os
import time
import datetime
import colorama
import string
import sys
from colorama import Fore
colorama.init()
date = datetime.datetime.now()
now = date.strftime("%H:%M:%S")
logs = "/usr/share/Terminator/core/setup/setup_logs.log"
try:
    if os.path.exists(logs):
        flag = True
    else:
        os.system('touch /usr/share/Terminator/core/setup/setup_logs.log > /dev/null 2>&1')
except:
    pass

def write_to(file):
    files = os.listdir("/usr/share/Terminator/core/setup")
    try:
        if os.path.exists(file):
            pass
        else:
            if flag == True:
                pass
            else:
                os.system('touch /usr/share/Terminator/core/setup/setup_logs.log > /dev/null 2>&1')
        with open(file, "a") as f:
            f.write(f"\n[{now}] core[i]: setup log has created at '/usr/share/Terminator/core/setup/setup_logs.log'")
            f.write(f"\n[{now}] core[i]: dependiences installed.")
            f.write(f"\n[{now}] core[i]: got 'bash_install.log'")
            f.write(f"\n[{now}] core[i]: reading 'bash_install.log'...")
            for l in files:
                if os.path.exists("/usr/share/Terminator/core/setup/"+l):
                    f.write(f"\n[{now}] core[i]: path exists [ '/usr/share/Terminator/core/setup/{l}' ]")
                else:
                    f.write(f"\n[{now}] core[e]: path does not exists [ '/usr/share/Terminator/core/setup/{l}' ]")
    except:
        pass
    sys.exit()




write_to(logs)