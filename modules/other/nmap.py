import nmap
import re
import sys
import colorama
from colorama import Fore
import os
colorama.init()
if len(sys.argv) < 3:
    sys.exit()

ip_add_entered = sys.argv[1]
port_range = sys.argv[2]


ip_add_pattern = re.compile("^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$")

port_range_pattern = re.compile("([0-9]+)-([0-9]+)")

port_min = 0
port_max = 65535
open_ports = []
while True:
    if ip_add_pattern.search(ip_add_entered):
        print(Fore.BLUE+"[*]"+Fore.RESET+f" {ip_add_entered} Is a Valid IP Address")
        break

while True:
    port_range_valid = port_range_pattern.search(port_range.replace(" ",""))
    if port_range_valid:
        port_min = int(port_range_valid.group(1))
        port_max = int(port_range_valid.group(2))
        break

nm = nmap.PortScanner()
print(Fore.YELLOW+'[+]'+Fore.RESET+f' Scanning {ip_add_entered}')
for port in range(port_min, port_max + 1):
    try:
        result = nm.scan(ip_add_entered, str(port))
        port_status = (result['scan'][ip_add_entered]['tcp'][port]['state'])
        print(Fore.BLUE+"[*]"+Fore.RESET+f" {ip_add_entered}: Port {port} Is {port_status}")
    except:
        print(Fore.RED+"[-]"+Fore.RESET+f" {ip_add_entered}: Cannot Scan Port {port}.")
        
