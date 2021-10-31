echo -e "\033[1;34m[*] \033[0mPlease Wait..."
apt clean > /dev/null 2>&1
apt autoremove -y > /dev/null 2>&1
echo -e "\033[1;34m[*] \033[0mChecking Python3..."
apt install python -y > /dev/null 2>&1
apt install python3-pip -y > /dev/null 2>&1
python3 core/setup/setup.py
#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m