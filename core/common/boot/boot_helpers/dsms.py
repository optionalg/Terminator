import time
import os
import time 
import sys
import colorama
import subprocess
from sys import stdout
import future
import datetime
import getpass
from colorama import Fore
colorama.init()
time.sleep(2)
user=getpass.getuser()
timerun=datetime.datetime.now()
try:
    if os.path.exists("/root/.tmf"):
        os.system('rm -rf /root/.tmf > /dev/null 2>&1')
        os.mkdir("/root/.tmf")
    else:
        os.mkdir("/root/.tmf")
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/core/logs"):
        pass
    else:
        os.mkdir("/usr/share/Terminator/core/logs")
        os.system('touch /usr/share/Terminator/core/logs/logs.log')
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator"):
        ter = True
    else:
        pass
except:
    pass
done = 'false'
def animate():
    while done == 'false':
        try:
            if os.path.exists("/usr/share/Terminator/core/logs/logs.log"):
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as t:
                    t.write(f"\n[{timerun}] ----------------- START CORE -----------------")
                    t.close()
            else:
                pass
        except:
            pass
        sys.stdout.write('\r[*] Starting terminator...|')
        try:
            if os.path.exists("/usr/share/Terminator/modules/handlers"):
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as i:
                    i.write(f"\n[{timerun}] NOTE: Loading Handler Version: 1.2554")
                    i.close()
            else:
                pass
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] sTarting terminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] stArting terminator...-')
        try:
            if os.path.exists("/usr/share/Terminator/core/logs/logs.log"):
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as v:
                    v.write(f"\n[{timerun}] NOTE: Loading Terminator Framework Started")
                    v.close()
            else:
                os.mkdir("/usr/share/Terminator/core/logs")
                os.system('touch /usr/share/Terminator/core/logs/logs.log')
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] staRting terminator...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starTing terminator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] startIng terminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] startiNg terminator...-')
        time.sleep(0.3)
        sys.stdout.write('\r[*] startinG terminator...\\')
        try:
            import colorama
            import scapy
            import future
            import subprocess
            import flask
        except ImportError:
            try:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as u:
                    u.write(f"\n[{timerun}] FATAL: Some Imports Maybe Not Imported!")
                    u.close()
            except:
                pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting Terminator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting tErminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting teRminator...-')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terMinator...\\')
        time.sleep(0.2)
        sys.stdout.write('\r[*] starting termInator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting termiNator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminAtor...-')
        time.sleep(0.1)
        try:
            if os.path.exists("/usr/share/Terminator"):
                md = True
            else:
                pass
        except:
            pass
        sys.stdout.write('\r[*] starting terminaTor...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatOr...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatoR.../')
        try:
            with open("/usr/share/Terminator/core/common/usr.yaml", "w") as f:
                f.write("User="+user)
                f.close()
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] Starting terminator...-')
        time.sleep(0.1)
        sys.stdout.write('\r[*] sTarting terminator...\\')
        try:
            if md == True:
                pass
            else:
                print(Fore.RED+'[-]'+Fore.RESET+' FATAL: Unable To Load Terminator Framework!')
                sys.exit()
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] stArting terminator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] staRting terminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starTing terminator...-')
        time.sleep(0.1)
        sys.stdout.write('\r[*] startIng terminator...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] startiNg terminator...|')
        time.sleep(0.2)
        sys.stdout.write('\r[*] startinG terminator.../')
        try:
            if os.path.exists("/usr/share/Terminator/modules"):
                mod = True
            else:
                pass
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting Terminator...-')
        try:
            if os.path.exists("/usr/share/Terminator/core/logs"):
                pass
            else:
                os.mkdir("/usr/share/Terminator/core/logs")
                os.system('touch /usr/share/Terminator/core/logs/logs.log')
        except:
            pass
        time.sleep(0.6)
        try:
            if mod == True:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as r:
                    r.write(f"\n[{timerun}] NOTE: Modules Loaded Successfully")
                    r.close()
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as y:
                    y.write(f"\n[{timerun}] FATAL: Unable To Load Modules")
                    y.close()
        except:
            pass
        sys.stdout.write('\r[*] starting tErminator...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting teRminator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terMinator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting termInator...-')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting termiNator...\\')
        try:
            if os.path.exists("/usr/share/Terminator/modules"):
                walk = os.listdir("/usr/share/Terminator/modules")
                walk2 = os.listdir("/usr/share/Terminator/modules/exploits")
                walk3 = os.listdir("/usr/share/Terminator/modules/handlers")
                walk4 = os.listdir("/usr/share/Terminator/modules/payloads")
                for ld in walk:
                    load = open("/usr/share/Terminator/core/logs/logs.log", "a")
                    load.write(f"\n[{timerun}] WARNING: Loading ADDITIONAL Module: {ld}")

                for ld2 in walk2:
                    lo = open("/usr/share/Terminator/core/logs/logs.log", "a")
                    lo.write(f"\n[{timerun}] WARNING: Loading ADDITIONAL Module: exploits/{ld2}")

                for ld3 in walk3:
                    lu = open("/usr/share/Terminator/core/logs/logs.log", "a")
                    lu.write(f"\n[{timerun}] WARNING: Loading ADDITIONAL Module: handlers/{ld3}")

                for ld4 in walk4:
                    lt = open("/usr/share/Terminator/core/logs/logs.log", "a")
                    lt.write(f"\n[{timerun}] WARNING: Loading ADDITIONAL Module: payloads/{ld4}")
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as er:
                    er.write(f"\n[{timerun}] FATAL: Unable To Load ADDITIONAL Modules")
                    er.close()
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminAtor...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminaTor.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatOr...-')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatoR...\\')
        time.sleep(0.3)
        os.system('python3 /usr/share/Terminator/core/base/tm.py')
        sys.exit()

done = "false"
animate()
