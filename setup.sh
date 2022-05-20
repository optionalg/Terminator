echo -e "\033[1;34m[*] \033[0mCleaning APT Cache..."
apt clean > /dev/null 2>&1
apt autoclean > /dev/null 2>&1
echo -e "\033[1;34m[*] \033[0mChecking Python & Dependencies"
apt install python -y > /dev/null 2>&1
apt install python3-pip -y > /dev/null 2>&1
echo -e "\033[1;33m[!] \033[0mTrying To Copy Database Files/Directories First..."
sleep 2
chmod +x databases/bin/tmdb > /dev/null 2>&1
cp -r databases/bin/tmdb /usr/bin > /dev/null 2>&1
echo -e '\033[1;77m[i] \033[0mYou Can Run Database By Typing "tmdb <arg>" In Terminal!'
read -n 1 -r -s -p "Press [Any Key] To Continue Setup..."
echo -e "\033[1;77m[i] \033[0mLoading Main Setup Script..."
python3 core/setup/setup.py
#\033[1;77m[i] \033[0m
#\033[1;77m[?] \033[0m
#\033[1;32m[+] \033[0m
#\033[1;33m[!] \033[0m
#\033[1;31m[-] \033[0m
#\033[1;34m[*] \033[0m