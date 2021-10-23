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
nowdate=datetime.datetime.now()
timerun=nowdate.strftime("%H:%M:%S")
try:
    if user == "root":
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' ROOT Not Detected! Please ReRun Terminator With ROOT Permissions!')
        sys.exit()
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/core/components"):
        c = os.listdir("/usr/share/Terminator/core/components")
    else:
        c = False
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/core/cache"):
        pass
    else:
        os.mkdir("/usr/share/Terminator/core/cache")
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/core/common/boot/cache"):
        boot = True
    else:
        os.mkdir("/usr/share/Terminator/core/common/boot/cache")
except:
    pass
try:
    if os.path.exists("/usr/var/tmf-meta-inf"):
        meta = True
    else:
        meta = False
except:
    pass
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
        sys.stdout.write('\r[*] Starting terminator...|')
        try:
            if os.path.exists("/usr/share/Terminator/modules/handlers"):
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as i:
                    i.write(f"\n[{timerun}] INFO: Loading Persistent Handlers...")
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
                    v.write(f"\n[{timerun}] INFO: Loading Payloads...")
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
            if os.path.exists("/usr/share/Terminator/modules") and os.path.exists("/usr/share/Terminator/lib/plugins"):
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
                    r.write(f"\n[{timerun}] INFO: Plugins Loaded Successfully")
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
                walk2 = os.listdir("/usr/share/Terminator/modules/exploits")
                walk5 = os.listdir("/usr/share/Terminator/modules/other")
                for ld2 in walk2:
                    lo = open("/usr/share/Terminator/core/logs/logs.log", "a")
                    lo.write(f"\n[{timerun}] WARNING: Loading Additional Module {ld2}")

                for ld5 in walk5:
                    l5 = open("/usr/share/Terminator/core/logs/logs.log", "a")
                    l5.write(f"\n[{timerun}] WARNING: Loading Additional Module {ld5}")
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as er:
                    er.write(f"\n[{timerun}] FATAL: Unable To Load Additional Modules")
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
        try:
            if os.path.exists("/usr/share/Terminator/core/components"):
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as core:
                    core.write(f"\n[{timerun}] NOTE: Loading Core Components...")
                    components = True
                    core.close()
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as fail:
                    fail.write(f"\n[{timerun}] FATAL: Unable To Detect And Load Core Components!")
                    fail.close()
        except:
            pass
        sys.stdout.write('\r[*] Starting terminator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] sTarting terminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] stArting terminator...-')
        time.sleep(0.5)
        try:
            if components == True:
                try:
                    to_load = ['builder.py', 'core.py', 'reloader.py', 'req.py', 'make.py']
                    more = {
                        'Name': 'Component Loader',
                        'Components': '/usr/share/Terminator/core/components',
                        'Description': 'Loads UnNeeded, Needed Components',
                        'License': 'No License',
                        'Author': 'G00Dway',
                        'Root': 'Needed'
                    }
                    comp = more['Components']
                    for setup in to_load:
                        try:
                            if os.path.exists(comp+'/'+setup):
                                with open(comp+'/'+setup, "w") as n:
                                    n.write("from core.components import core")
                                with open("/usr/share/Terminator/core/logs/logs.log", "a") as log:
                                    log.write(f"\n[{timerun}] INFO: Loaded Component {setup}")
                            else:
                                with open("/usr/share/Terminator/core/logs/logs.log", "a") as error:
                                    error.write(f"\n[{timerun}] FATAL: Unable To Load Component {setup}")
                                os.system(f'touch {comp}/{setup} > /dev/null 2>&1')
                        except:
                            pass
                except:
                    pass
        except:
            pass
        sys.stdout.write('\r[*] staRting terminator...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starTing terminator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] startIng terminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] startiNg terminator...-')
        time.sleep(0.1)
        sys.stdout.write('\r[*] startinG terminator...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting Terminator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting tErminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting teRminator...-')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terMinator...\\')
        try:
            if meta == True:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as tmf:
                    tmf.write(f'\n[{timerun}] INFO: Found: "/usr/var/tmf-meta-inf"')
                    tmf.close()
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as tmf_fail:
                    tmf_fail.write(f'\n[{timerun}] NOTE: Database "/usr/var/tmf-meta-inf" Does Not Exists, Passing...')
                    tmf_fail.close()
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting termInator...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting termiNator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminAtor...-')
        try:
            os.system('python3 /usr/share/Terminator/core/base/scripts/plugin.py')
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminaTor...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatOr...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatoR.../')
        time.sleep(0.2)
        os.system('python3 /usr/share/Terminator/core/base/tm.py')
        sys.exit()

done = "false"
animate()
