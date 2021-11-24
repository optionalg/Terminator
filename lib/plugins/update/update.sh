cd /usr/share/Terminator
echo -e "\033[1;34m[*] \033[0mChecking For Latest Updates..."
BRANCH="main"
LAST_UPDATE=`git show --no-notes --format=format:"%H" $BRANCH | head -n 1`
LAST_COMMIT=`git show --no-notes --format=format:"%H" origin/$BRANCH | head -n 1`

git remote update > /dev/null 2>&1
if [ $LAST_COMMIT != $LAST_UPDATE ]; then
        python3 /usr/share/Terminator/lib/plugins/update/update.py
else
        echo -e "\033[1;32m[+] \033[0mNo Updates Available."
fi