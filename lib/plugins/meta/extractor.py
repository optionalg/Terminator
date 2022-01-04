import os
import sys
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
sys.exit()