import os
import sys
import time
import colorama
from colorama import Fore
import random
colorama.init()
try:
    with open("/usr/share/Terminator/VERSION", "r") as f:
        version = f.read()
except Exception:
    pass
banners = [f"""
 _____                   _             _             
|_   _|                 (_)           | |            
  | | ___ _ __ _ __ ___  _ _ __   __ _| |_ ___  _ __ 
  | |/ _ \ '__| '_ ` _ \| | '_ \ / _` | __/ _ \| '__|
  | |  __/ |  | | | | | | | | | | (_| | || (_) | |   
  \_/\___|_|  |_| |_| |_|_|_| |_|\__,_|\__\___/|_|
                 Break Every System!


+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}""", f"""
                      ,____
                      |---.\\
              ___     |    `      TERMINATOR
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|         REAP THE REWARDS
           / \_| |/ \ |
          /      \/\( |            
          |   /  |` ) |           Hurray!...
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}""", f'''
{Fore.GREEN}Malware load success
CODE 7X04U8{Fore.RED}
WRITING...
WRITING...
WRITING...
WRITING...
WRITING...
OH NO!
{Fore.RESET}
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOTOOOOMOOOOOOOFOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOTTTTOOoOOOMMOO?oOOFFO?OFFO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''

\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..                                     
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Explore The Systems...\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''
                                                                                                    
TTTTTTTTTTTTTTTTTTTTTTTMMMMMMMM               MMMMMMMMFFFFFFFFFFFFFFFFFFFFFF
T:::::::::::::::::::::TM:::::::M             M:::::::MF::::::::::::::::::::F
T:::::::::::::::::::::TM::::::::M           M::::::::MF::::::::::::::::::::F
T:::::TT:::::::TT:::::TM:::::::::M         M:::::::::MFF::::::FFFFFFFFF::::F
TTTTTT  T:::::T  TTTTTTM::::::::::M       M::::::::::M  F:::::F       FFFFFF
        T:::::T        M:::::::::::M     M:::::::::::M  F:::::F             
        T:::::T        M:::::::M::::M   M::::M:::::::M  F::::::FFFFFFFFFF   
        T:::::T        M::::::M M::::M M::::M M::::::M  F:::::::::::::::F   
        T:::::T        M::::::M  M::::M::::M  M::::::M  F:::::::::::::::F   
        T:::::T        M::::::M   M:::::::M   M::::::M  F::::::FFFFFFFFFF   
        T:::::T        M::::::M    M:::::M    M::::::M  F:::::F             
        T:::::T        M::::::M     MMMMM     M::::::M  F:::::F             
      TT:::::::TT      M::::::M               M::::::MFF:::::::FF           
      T:::::::::T      M::::::M               M::::::MF::::::::FF           
      T:::::::::T      M::::::M               M::::::MF::::::::FF           
      TTTTTTTTTTT      MMMMMMMM   Terminator  MMMMMMMMFFFFFFFFFFF         

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''
 We look for it...
      _____.__                      __            __   
    _/ ____\  | _____     ____    _/  |____  ____/  |_
    \   __\|  | \__  \   / ___\   \   __\  \/  /\   __\
     |  |  |  |__/ __ \_/ /_/  >   |  |  >    <  |  |  
     |__|  |____(____  /\___  / /\ |__| /__/\_ \ |__|  
                     \//_____/  \/            \/     
                                                 ...and we always find it

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RED}''', f'''

                      ..:::::::::..
                  ..:::aad8888888baa:::..
              .::::d:?88888888888?::8b::::.
            .:::d8888:?88888888??a888888b:::.
          .:::d8888888a8888888aa8888888888b:::.
         ::::dP::::::::88888888888::::::::Yb::::
        ::::dP:::::::::Y888888888P:::::::::Yb::::
       ::::d8:::::::::::Y8888888P:::::::::::8b::::
      .::::88::::::::::::Y88888P::::::::::::88::::.
      :::::Y8baaaaaaaaaa88P:T:Y88aaaaaaaaaad8P:::::
      :::::::Y88888888888P::|::Y88888888888P:::::::
      ::::::::::::::::888:::|:::888::::::::::::::::
      `:::::::::::::::8888888888888b::::::::::::::'
       :::::::T:::::::88888888888888::::M:::::::::
        :::::::::::::d88888888888888:::::::::::::
         ::::::::::::88::88::88:::88::::::::::::
          `::::::::::88::88::88:::88::::::::::'
            `::::::::88::88::P::::88::::::::'
              `::::::88::88:::::::88::::::'
                 ``:::::::::F:::::::::''
                      ``:::::::::'' 
{Fore.RESET}
+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''
     ____.-.____
    [___________]
   (d|||||||||||b)
    `|||||||||||`
     |||||||||||
     |||||||||||
     |||||||||||
     |||||||||||
     `"""""""""`  /recycle/bin/sh

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RED}''', f'''

                          `:oDFo:`
                       ./ymM0dayMmy/.
                    -+dHJ5aGFyZGVyIQ==+-
                `:sm⏣~~Destroy.No.Data~~s:`
             -+h2~~Maintain.No.Persistence~~h+-
          `:odNo2~~Above.All.Else.Do.No.Harm~~Ndo:`
      ./etc/shadow.0days-Data'%20OR%201=1--.No.0MN8'/.
   -++SecKCoin++e.AMd`       `.-://///+hbove.913.ElsMNh+- 
  -~/.ssh/id_rsa.Des-                  `htN01UserWroteMe!-
  :dopeAW.No<nano>o                     :is:TЯiKC.sudo-.A:
  :we're.all.alike'`                     The.PFYroy.No.D7:
  :PLACEDRINKHERE!:                      yxp_cmdshell.Ab0:
  :(TMF)> exec pwd                       :Ns.BOB&ALICEes7:
  :---srwxrwx:-.`                        `MS146.52.No.Per:
  :<script>.Ac816/                        sENbove3101.404:
  :NT_AUTHORITY.Do                        `T:/shSYSTEM-.N:
  :09.14.2011.raid                       /STFU|wall.No.Pr:
  :hevnsntSurb025N.                      dNVRGOING2GIVUUP:
  :#OUTHOUSE-  -s:                       /corykennedyData:
  :$nmap -oS                              SSo.6178306Ence:
  :Awsm.da:                            /shMTl#beats3o.No.:
  :Ring0:                             `dDestRoyREXKC3ta/M:
  :23d:                               sSETEC.ASTRONOMYist:
   /-                        /yo-    .ence.N:()[ TMF|: & ];:
                             `:Shall.We.Play.A.Game?tron/
                             ```-ooy.if1ghtf0r+ehUser5`
                           ..th3.H1V3.U2VjRFNN.jMh+.`
                          `MjM~~WE.ARE.se~~MMjMs
                           +~KANSAS.CITY's~-`
                            J~HACKERS~./.`
                            .esc:wq!:`
                             +++ATH`
{Fore.RESET}
+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''

  PPPPP   IIIIIII   N    N
  P   PP     I      NN   N   IDENTIFICATION
  P   PP     I      N N  N
  PPPPP      I      N  N N      PROGRAM
  P          I      N   NN
  P       IIIIIII   N    N

      Strike a key when ready ...
+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.YELLOW}''', f'''

    01011001011011110111010100100000011100
    10011001010110000101101100011011000111
    10010010000001101000011000010111011001
    10010TTTTTTTTTTT11MMM001FFFFFFFF0100000
    01101101011101010110001101101000001000
    00011101000110100101101101011001010010
    00000110111101101110001000000111100101
    10111101110101011100100010000001101000
    01100001011011100110010001110011001000
    00001110100010110100101001001000000101
    01000110100001100001011011100110101101
    11001100100000011001100110111101110010
    00100000011101010111001101101001011011
    10011001110010000001110100011010000110
    01010010000001010011011011110110001101
    10100101100001011011000010110101000101
    01101110011001110110100101101110011001
    01011001010111001000100000010101000110
    11110110111101101100011010110110100101
    11010000100000001010100110100001110101
{Fore.RESET}
+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''
I have no girlfriend... so..
But ik these...

  Cyber security girls... 
                         .-" `.
                         ;:":  ""--..
                .-+. ,gpd$L\:._      ""-._
               /  //;$SS$$$$SS$$t--.      "-._
             .'  `.//SS$P^"""TS$$S. "-.       "-, 
           .'    _ "-S^"      TS$$Sb   "-.       `.
         .'    .':S$Y      _.. SS$$Sb-'   "-.      ;
       .'    .'  SS$;,=-.  ._.`:S$$SS;       j     ;
     .'    .'   :SS$$.-'        SS$$SS\     /     /
   .'     /     SS$$S;    -     SS$$SS ;   /     /
 .'      /   ._dSS$$SS   .--.  :SS$$$S\;  /     /
/       /     :SS$$SS$b. `--'  $$SS$$S ) /     /
\      :      ;SS$$SS$$SS.___.'$$SS$$Sb /     / 
 \      "-.   SS$$SS$$$SS      $$SS$$SS';    / 
  `.       "-dSS$$SS$$SS:;     :$$SSSP      / 
    `.              "^S^':     '^TSS'      /
                                              ...are perfect!
                                    
+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''

    .o88o.                               o8o                .
    888 `"                               `"'              .o8
   o888oo   .oooo.o  .ooooo.   .ooooo.  oooo   .ooooo.  .o888oo oooo    ooo
    888    d88(  "8 d88' `88b d88' `"Y8 `888  d88' `88b   888    `88.  .8'
    888    `"Y88b.  888   888 888        888  888ooo888   888     `88..8'
    888    o.  )88b 888   888 888   .o8  888  888    .o   888 .    `888'
   o888o   8""888P' `Y8bod8P' `Y8bod8P' o888o `Y8bod8P'   "888"      d8'
                                                                .o...P'
                                                                `TMF'

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''', f'''

       _____,,;;;`;       ;';;;,,_____
    ,~(  )  , )~~\|  TMF  |/~~( ,  (  )~;
    ' / / --`--,             .--'-- \ \ `
     /  \    | '             ` |    /  \

+ -- --=[ {Fore.YELLOW}Terminator Framework {version} {Fore.RESET}''']
banner_selected = random.choice(banners)
try:
    with open("/usr/share/Terminator/core/base/ui/banners/out/banner.txt", "w") as f:
        f.write(banner_selected)
except Exception:
    pass
sys.exit()
