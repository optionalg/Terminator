class Info:
    report = "https://github.com/G00Dway/Terminator/issues"
    git = "https://github.com/G00Dway/Terminator"
    name = "Terminator"
    execution = "tmconsole"
    app_execution = "exec.sh", "/usr/share/Terminator/bin/tmconsole/exec.sh"
    author = "G00Dway"
    install_location = "/usr/share/Terminator"
    tmconsole_location = "/usr/bin/tmconsole"
    setup = "setup.sh"
    remove = "uninstall.sh", "bin.sh"
    tmf_db = "/usr/share/Terminator/database"

class Dir: #s
    home = "/home/"
    root = "/root/"
    usr = "/usr/"
    share = "/usr/share/"
    bin = "/usr/bin/"
    db = "/usr/var/"

class Systems:
    kali = "Kali Linux" # Available, Tested
    kali_vers = ["2021.1", "2021.2", "2021.3", "2020.1", "2020.2", "2020.3", "2019.1", "2019.2", "2019.3"]
    parrot = "Parrot OS" # Available, Tested
    windows = "win32", "win64" # Not Supported, Not Available
    linux = "Linux", "Linux2" # Available, Not Tested
    wifislax = "WifiSlax" # Available, Not Tested