import os
import time
import colorama
from colorama import Fore
import sys
colorama.init()


code = '''
import os
import time
import sys
import colorama
from colorama import Fore
colorama.init()
activities = ['firstrun', 'file_operation', 'dsms']
try:
    with open("/usr/share/Terminator/core/setup/first_run_setup.ini", "r") as f:
        for activity in f:
            if "activity=" in activity:
                if 'firstrun' in activity:
                    print(Fore.BLUE+'[*]'+Fore.RESET+' First Run Detected.')
                    print(Fore.BLUE+'[*]'+Fore.RESET+' Removing UnNeeded Temporary Files...')
                    os.system('rm -rf /usr/share/Terminator/README.md > /dev/null 2>&1')
                    os.system('rm -rf /usr/share/Terminator/setup.sh > /dev/null 2>&1')
                    os.system('rm -rf /usr/share/Terminator/uninstall.sh > /dev/null 2>&1')
except:
    pass
sys.exit()
'''

boot = "/usr/share/Terminator/core/common/boot/boot_helpers/dsms.py"
def setup():
    try:
        if os.path.exists(boot):
            if os.path.exists("/usr/share/Terminator/core/setup/first_run_setup.ini"):
                with open("/usr/share/Terminator/core/setup/first_run_setup.ini", "w") as st:
                    st.write("\n[Setup]")
                    st.write("\nName=Terminator")
                    st.write("\nPath='/usr/share/Terminator'")
                    st.write("\nSetup='/usr/share/Terminator/core/setup'")
                    st.write("\n")
                    st.write("\n[ACTIVITY]")
                    st.write("\nactivity='firstrun'")
                    st.close()
                os.system('touch /usr/share/Terminator/core/setup/use.log > /dev/null 2>&1')
            else:
                os.system('touch /usr/share/Terminator/core/setup/first_run_setup.ini > /dev/null 2>&1')
                setup()
    except:
        pass

setup()
try:
    if os.path.exists("/usr/share/Terminator/core/components"):
        os.system('touch /usr/share/Terminator/core/components/firstrun.py > /dev/null 2>&1')
        with open("/usr/share/Terminator/core/components/firstrun.py", "w") as console:
            console.write(code)
            console.close()
except:
    pass
try:
    if os.path.exists("/usr/share/Terminator/core/setup/cp/services/tmf-broker.service"):
        pass
    else:
        print(Fore.RED+'[-]'+Fore.RESET+' File: "/usr/share/Terminator/core/setup/cp/services/tmf-broker.service" Does NOT Exists')
        print(Fore.RED+'[-]'+Fore.RESET+' Exiting...')
        sys.exit()
except:
    pass
sys.exit()