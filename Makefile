help:
        echo -e "
Terminator Framework Installation
===================================

Command                     Description
-------                     -----------
make install                Start install script
make uninstall              Start uninstall script
"

install:
		bash setup.sh
	
uninstall:
		bash uninstall.sh