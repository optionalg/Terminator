echo -e "\033[1;34m[*] \033[0mInitiliazing..."
apt clean > /dev/null 2>&1
apt autoremove -y > /dev/null 2>&1
clear
echo -e "\033[1;34m[*] \033[0mInstalling Requirements..."
apt install ruby perl metasploit-framework xterm zenity python python3-pip gem git -y > /dev/null 2>&1
pip3 install colorama scapy pysocks imports future paramiko flask > /dev/null 2>&1
pip3 install bs4 > /dev/null 2>&1
echo -e "\033[1;34m[*] \033[0mCopying Additional Files > /usr/share..."
python3 cp/cp.py
echo -e "\033[1;34m[*] \033[0mCopying tmconsole > /usr/bin..."
cp -r bin/tmconsole/tmconsole /usr/bin > /dev/null 2>&1
chmod +x /usr/bin/tmconsole
echo -e "\033[1;34m[*] \033[0mCleaning Up..."
echo -e "\033[1;34m[*] \033[0mSetup Finished!"
echo
echo -e "\033[1;32m[+] \033[0mTo Start Terminator Just Type '\033[1;32mtmconsole\033[0m' In Terminal!"
#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m