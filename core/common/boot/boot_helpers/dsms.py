import time
import os
import time 
import sys
import colorama
import subprocess
import future
import pickle
import datetime
import getpass
from colorama import Fore
colorama.init()
time.sleep(3)
user=getpass.getuser()
nowdate=datetime.datetime.now()
timerun=nowdate.strftime("(%D) - %H:%M:%S")
args = []
auto_upd = False
clean_db = False
try:
    if os.path.exists("/usr/share/Terminator/core/setup/use.log"):
        os.system('python3 /usr/share/Terminator/core/components/firstrun.py')
        os.system('rm -rf /usr/share/Terminator/core/setup/use.log > /dev/null 2>&1')
    else:
        pass
except:
    pass
def add_args():
    try:
        base = ["auto_update_check", "clean_database_startup"]
        if os.path.exists("/usr/share/Terminator/core/base/extra/settings.ini"):
            with open("/usr/share/Terminator/core/base/extra/settings.ini", "r") as settings:
                for setting in settings:
                    if "auto_update_check" in setting:
                        if "True" in setting:
                            global auto_upd
                            auto_upd = True
                        else:
                            pass
                    if "clean_database_startup" in setting:
                        if "True" in setting:
                            global clean_db
                            clean_db = True
                        else:
                            pass
        else:
            pass

    except:
        pass
def console():
    if auto_upd == True:
        try:
            if os.path.exists("/usr/share/Terminator/lib/plugins/update/update.sh"):
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as update:
                    update.write(f'\n[{timerun}] INFO: Wrote Update Result As "/usr/share/Terminator/core/logs/auto_update.log"')
                    update.close()
                os.system('bash /usr/share/Terminator/lib/plugins/update/update.sh > /usr/share/Terminator/core/logs/auto_update.log')
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as update:
                    update.write(f"\n[{timerun}] FATAL: Unable To Start Update File, Update File Corrupted Or Removed!")
                    update.close()
        except:
            pass
    if clean_db == True:
        try:
            if os.path.exists("/usr/share/Terminator/core/base/extra/scripts/cln.py"):
                os.system('python3 /usr/share/Terminator/core/base/extra/scripts/cln.py')
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as clean:
                    clean.write(f"\n[{timerun}] INFO: Database Successfully Cleaned")
                    clean.close()
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as clean:
                    clean.write(f"\n[{timerun}] FATAL: Unable To Start Cleaner And Clean Database!")
                    clean.close()
        except:
            pass
try:
    if user == "root":
        root = True
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' ROOT Not Detected! Please ReRun Terminator With ROOT Permissions!')
        exit()
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
add_args()
console()
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
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as handler:
                    handler.write(f"\n[{timerun}] FATAL: Unable To Load Persistent Handlers")
                    handler.close()
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] sTarting terminator.../')
        time.sleep(0.1)
        sys.stdout.write('\r[*] stArting terminator...-')
        try:
            if os.path.exists("/usr/share/Terminator/modules/payloads"):
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as v:
                    v.write(f"\n[{timerun}] INFO: Loading Payloads...")
                    v.close()
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as payload:
                    payload.write(f"\n[{timerun}] FATAL: Unable To Load Payloads")
                    payload.close()
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
                    u.write(f"\n[{timerun}] FATAL: Unable To Import Python Packages")
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
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as i:
                    i.write(f"\n[{timerun}] INFO: Loading Plugins...")
                    i.close()

                with open("/usr/share/Terminator/core/logs/logs.log", "a") as r:
                    r.write(f"\n[{timerun}] INFO: Plugins Loaded Successfully")
                    r.close()
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as y:
                    y.write(f"\n[{timerun}] FATAL: Unable To Load Plugins & Modules")
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
            if os.path.exists("/usr/share/Terminator/core/base/extra/scripts/loaded.dat"):
                os.system('rm -rf /usr/share/Terminator/core/base/extra/scripts/loaded.dat > /dev/null 2>&1')
                os.system('touch /usr/share/Terminator/core/base/extra/scripts/loaded.dat > /dev/null 2>&1')
            else:
                os.system('touch /usr/share/Terminator/core/base/extra/scripts/loaded.dat > /dev/null 2>&1')
            if os.path.exists("/usr/share/Terminator/modules"):
                l = os.listdir("/usr/share/Terminator/modules")
                for i in l:
                    a = os.listdir("/usr/share/Terminator/modules/"+i)
                    for load in a:
                        with open("/usr/share/Terminator/core/logs/logs.log", "a") as write_log:
                            write_log.write(f"\n[{timerun}] NOTE: Loading Additional Module {load}")
                            write_log.close()
            else:
                with open("/usr/share/Terminator/core/logs/logs.log", "a") as fail:
                    fail.write(f"\n[{timerun}] FATAL: Unable To Load Modules Database")
                    fail.close()
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
                                    n.write("# This is the core component of Terminator for errors, Removing this file does not affects to Terminator")
                                    n.close()
                                with open("/usr/share/Terminator/core/logs/logs.log", "a") as log:
                                    log.write(f"\n[{timerun}] INFO: Loaded Component {setup}")
                                    log.close()
                            else:
                                with open("/usr/share/Terminator/core/logs/logs.log", "a") as p:
                                    p.write(f"\n[{timerun}] NOTE: Setting Up Component {setup}")
                                    p.close()
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
                    tmf.write(f'\n[{timerun}] INFO: Found Database: "/usr/var/tmf-meta-inf"')
                    tmf.write(f'\n[{timerun}] INFO: Scanning Database: "/usr/var/tmf-meta-inf"')
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
            with open("/usr/share/Terminator/core/logs/logs.log", "a") as plugin_load:
                plugin_load.write(f"\n[{timerun}] NOTE: Starting Cache Plugin...")
                plugin_load.close()
            os.system('python3 /usr/share/Terminator/core/base/scripts/plugin.py')
        except:
            pass
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminaTor...\\')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatOr...|')
        time.sleep(0.1)
        sys.stdout.write('\r[*] starting terminatoR.../\n')
        time.sleep(0.2)
        os.system('python3 /usr/share/Terminator/core/base/tm.py')
        break


done = "false"
animate()
sys.exit()
