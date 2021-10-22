import sys
import os
import colorama
import string
import getpass
import random
from colorama import Fore
colorama.init()
KEY_LEN = 20
user = getpass.getuser()
def base_str():
    return (string.ascii_letters+string.digits)
keylist = random.choices(base_str(), k=KEY_LEN)
key = ''.join(keylist)
nums = '''
File     : '''+key+'''
Name     : Terminator
Author   : G00Dway
User     : '''+user+'''
Root     : 
System   : 
License  : GNU 3.0 General Public.
CPU, GPU :
TMF-db   : /usr/share/Terminator
META-db  : /usr/var/tmf-meta-inf
ROOT-db  : /root/.tmf
Console  : /usr/bin/tmconsole
Caches   : /usr/share/Terminator/core/cache, /usr/share/Terminator/core/base/scripts/cache, /usr/share/Terminator/core/common/boot/cache
Extract  : /usr/share/Terminator/lib/plugins/meta/extractor.py
Exec     : /usr/share/Terminator/bin/tmconsole/exec.sh
Plugins  : /usr/share/Terminator/lib/plugins
Tested   : Kali Linux, Parrot OS, Debian x64
Services : Not Available
Credits  : No One




------------- END ------------- 
'''

def plugin(cache):
    try:
        os.system('touch '+cache+'/libs/'+key+' > /dev/null 2>&1')
        with open("/usr/share/Terminator/core/base/scripts/cache/libs/"+key, "w") as f:
            f.write(nums)
            f.close()
    except:
        pass
cache = '/usr/share/Terminator/core/base/scripts/cache'
try:
    if os.path.exists(cache):
        pass
    else:
        os.mkdir(cache)

    if os.path.exists(cache+'/libs'):
        pass
    else:
        os.mkdir(cache+'/libs')
except:
    pass
plugin(cache)
