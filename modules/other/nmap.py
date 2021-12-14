from __future__ import print_function
import optparse
from socket import *
from threading import *
import colorama
from colorama import Fore
screenLock = Semaphore(value=1)
def connScan(tgtHost, tgtPort):
    try:
        connSkt = socket(AF_INET, SOCK_STREAM)
        connSkt.connect((tgtHost, tgtPort))
        connSkt.send("ip")
        results = connSkt.recv(1024)
        screenLock.acquire()
        print(Fore.YELLOW+"[+]"+Fore.RESET+" %d/TCP Open" % (tgtPort))
        print(Fore.YELLOW+"[+]"+Fore.RESET+"" + str(results))
    except:
        screenLock.acquire()
        print(Fore.RED+"[-]"+Fore.RESET+" %d/TCP Closed" % tgtPort)
    finally:
        screenLock.release()
        connSkt.close()
def portScan(tgtHost, tgtPorts):
    try:
        tgtIP = gethostbyname(tgtHost)
    except:
        print(Fore.RED+"[-]"+Fore.RESET+" Cannot Resolve '%s': Unknown Host" % tgtHost)
        return
    try:
        tgtName = gethostbyaddr(tgtIP)
        print(Fore.YELLOW+"[+]"+Fore.RESET+" Scan Results For: " + tgtName[0])
    except:
        print(Fore.YELLOW+"[+]"+Fore.RESET+" Scan Results For: " + tgtIP)
    setdefaulttimeout(1)
    for tgtPort in tgtPorts:
       t = Thread(target=connScan, args=(tgtHost, int(tgtPort.strip())))
       t.start()
def main():
    parser = optparse.OptionParser(('usage %prog -H <target host> -p <target port(s) separated by space>'))
    parser.add_option("-H", dest="tgtHost", type="string", help="specify target host")
    parser.add_option("-p", dest="tgtPort", type="string", help="specify target port(s) separated by space")
    (options, args) = parser.parse_args()
    tgtHost = str(options.tgtHost).strip()
    tgtPorts = [s.strip() for s in str(options.tgtPort).split(',')]
    if (tgtHost == None) | (tgtPorts[0] == None):
        print(parser.usage)
        exit(0)
    portScan(tgtHost, tgtPorts)
if __name__ == "__main__":
    main()