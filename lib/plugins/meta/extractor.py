import os
import sys
import colorama
from colorama import Fore
colorama.init()
try:
    os.system('mkdir /usr/share/Terminator/core/logs/meta > /dev/null 2>&1')
    os.system('mkdir /usr/share/Terminator/core/logs/cache_meta > /dev/null 2>&1')
except:
    pass
try:
    os.system('cp -r /usr/share/Terminator /usr/share/Terminator/core/logs/meta > /dev/null 2>&1')
    os.system('mv /usr/share/Terminator/core/logs/meta/Terminator /usr/share/Terminator/core/logs/meta/Terminator-new > /dev/null 2>&1')
except:
    pass
try:
    os.system('mv /usr/bin/tmconsole /usr/share/Terminator/core/logs/cache_meta > /dev/null 2>&1')
    os.system('chmod +x /usr/share/Terminator/bin/tmconsole/tmconsole > /dev/null 2>&1')
    os.system('cp -r /usr/share/Terminator/bin/tmconsole/tmconsole /usr/bin > /dev/null 2>&1')
except:
    pass
print(Fore.BLUE+'[*]'+Fore.RESET+' Checking PIP Requirements...')
if os.path.exists('/usr/share/Terminator/core/logs/pip-update.log'):
    pass
else:
    os.system('touch /usr/share/Terminator/core/logs/pip-update.log > /dev/null 2>&1')
os.system('bash /usr/share/Terminator/core/setup/pip-install.sh > /usr/share/Terminator/core/logs/pip-update.log')
print(Fore.BLUE+'[*]'+Fore.RESET+' ReEnabling Plugins...')
try:
    if os.path.exists('/usr/share/Terminator/core/base/scripts/cache/libs'):
        log = os.listdir('/usr/share/Terminator/core/base/scripts/cache/libs')
        for i in log:
            with open('/usr/share/Terminator/core/base/scripts/cache/libs/'+i, 'r') as f:
                for line in f:
                    if 'System   : ' in line:
                        if 'Linux' in line:
                            pass
                        else:
                            if os.path.exists('/usr/share/Terminator/core/logs/reenable.log'):
                                pass
                            else:
                                os.system('touch /usr/share/Terminator/core/logs/reenable.log > /dev/null 2>&1')
                            with open('/usr/share/Terminator/core/logs/reenable.log', 'a') as re:
                                re.write(f"FILE: {i}, ERROR: Could not detect system")
                                re.write(f"FILE: {i}, ERROR: Could not detect system version")
                                re.close()
        if os.path.exists('/usr/share/Terminator/core/logs/reenable.log'):
            print(Fore.RED+'[-]'+Fore.RESET+' Unable To ReEnable Some Plugins, Please Read "/usr/share/Terminator/core/logs/reenable.log" For More Information')
        else:
            pass
    else:
        pass
except:
    pass
print(Fore.BLUE+'[*]'+Fore.RESET+' Cleaning Up...')
os.system('rm -rf /usr/share/Terminator/README.md > /dev/null 2>&1')
os.system('rm -rf /usr/share/Terminator/setup.sh > /dev/null 2>&1')
os.system('rm -rf /usr/share/Terminator/uninstall.sh > /dev/null 2>&1')
os.system('rm -rf /usr/share/Terminator/core/logs/logs.log > /dev/null 2>&1')
print(Fore.BLUE+'[*]'+Fore.RESET+' Done.')
sys.exit()