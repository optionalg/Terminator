echo -e "\033[1;34m[*] \033[0mStarting Uninstallation Script..."
sleep 1
echo -e "\033[1;77m[?] \033[0mDo You Want To Uninstall The MAIN Database? (Y/n): "
read $MAIN
if [[ $MAIN != 'y' && $MAIN != 'Y' ]]; then
  bash /usr/share/Terminator/bin/bin.sh > /dev/null 2>&1
  bash bin/bin.sh > /dev/null 2>&1
  echo -e "\033[1;32m[+] \033[0mMain Database Removed."
else
  echo -e "\033[1;34m[*] \033[0mMain Database Passed."
fi
echo -e "\033[1;77m[?] \033[0mDo You Want To Uninstall The Database? (Y/n): "
read $DAB
if [[ $DAB != 'y' && $DAB != 'Y' ]]; then
  rm -rf /usr/bin/tmdb > /dev/null 2>&1
  echo -e "\033[1;32m[+] \033[0mDatabase Removed."
else
  echo -e "\033[1;31m[-] \033[0mYou MAY Receive Errors If You Didnt Passed MAIN Database Uninstallation."
  echo -e "\033[1;34m[*] \033[0mDatabase Passed."
fi
echo -e "\033[1;32m[+] \033[0mUninstallation Script Finished."
sleep 1