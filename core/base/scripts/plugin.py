import sys
import os
import colorama
import string
import random
from colorama import Fore
colorama.init()
KEY_LEN = 20
def base_str():
    return (string.ascii_letters+string.digits)
keylist = random.choices(base_str(), k=KEY_LEN)
key = ''.join(keylist)

def plugin(cache):
    try:
        os.system('touch '+cache+'/libs/'+key+' > /dev/null 2>&1')
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
