import os
import sys
import colorama
from colorama import Fore
colorama.init()
if len(sys.argv) < 5:
    sys.exit()

ip = sys.argv[1]
hostname = sys.argv[2]
host = sys.argv[3]
port = sys.argv[4]
try:
    if os.path.exists("/usr/share/Terminator/core/session"):
        os.system('touch /usr/share/Terminator/core/session/session.yaml')
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' Error While Backgrounding Process')
        sys.exit()
    with open("/usr/share/Terminator/core/session/session.yaml", "w") as f:
        f.write(ip)
        f.write("\n"+hostname)
        f.write("\n"+host)
        f.write("\n"+port)
        f.close()
except:
    pass
sys.exit()