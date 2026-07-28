###################
# NETWORKING TOOL #
#  MADE BY MONY   #
# github/MONYtry  #
###################


import os
import subprocess
import socket
from datetime import datetime
from concurrent.futures import ThreadPoolExecutor
import time
import psutil
import ssl

# Colors [ANSI FORMAT]
RED = "\033[31m"
GREEN = "\033[32m"
BLUE = "\033[34m"
RESET = "\033[0m"

IPs_toCheck = ["8.8.8.8","192.168.1.1"]
open_ports = []

# ============== TYPE TEXT ANIMATION ============== #
def type_text(text,speed):
    for char in text:
        print(char,end="", flush=True)
        time.sleep(speed)
    print()


# ============== CLEAR CONSOLE ============== #
def clearConsole():
    os.system("cls")

# ============== HEADER ============== #
# HAHAH bitte ignoriert dieses Kiddo "FSOCIETY" xD
def header():
    clearConsole()
    type_text(RED + f"""
                                                                                                ⠀⠀⠀⠀⠀⢀⣠⣴⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣤⣀⠀⠀
                                                                                                    ⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀
                                                                                                    ⠀⢸⣟⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⠀
                                                                                                    ⠀⣿⡿⣿⡟⠛⠛⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⠛⠛⢻⣿⣿⠀
                                                                                                    ⠀⣿⡿⠋⠉⠑⠒⠤⣉⠻⢿⣿⣿⡿⠋⠀⠀⠀⠁⠐⠳⢹⡇
                                                                                                    ⠀⣿⣷⣶⣦⣄⡀⠀⠀⠉⠺⡿⠿⠃⠀⠀⠀⣠⣴⣶⣶⣾⡇
                                                                                                    ⠀⣿⣿⣿⣿⣿⣿⣦⡀⠀⠀⣴⣇⠀⠀⣰⡿⠿⠿⢿⣿⢛⡇
                                                                                                    ⠀⣡⡌⠁⠀⠀⠀⠈⠉⠀⠈⣿⣷⠀⠀⠁⠀⠀⠀⠀⣠⣌⣿
                                                                                                    ⠀⢿⣿⣿⣶⣦⣴⣶⣾⣰⠄⣿⣿⠠⣸⣶⣶⣶⣶⣿⣿⣿⡇
                                                                                                    ⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⠃⣿⣿⠐⣿⢿⣿⣿⣟⣋⣠⡔⠀
                                                                                                    ⠀⠸⡀⠉⠉⣉⣍⣭⠹⢿⠁⣿⣿⡇⠿⠆⣭⣉⡉⠉⡁⢰⠀
                                                                                                    ⠀⠀⢷⡀⢀⠈⠻⠿⠶⠄⠀⠈⠉⠀⠠⠾⠿⠟⠁⠐⢠⠇⠀
                                                                                                    ⠀⠀⠈⢷⡀⠐⢤⣤⣀⡀⠀⠴⠷⠄⠀⣠⣤⡤⠌⠠⠋⠀⠀
                                                                                                    ⠀⠀⠀⠀⠱⣷⡄⢦⣍⣙⠛⠒⠒⠒⣉⣩⣤⠆⢔⠃⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⡀⠈⠛⣆⢻⣿⡇⠀⡄⠸⣿⡿⠣⡎⠀⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⣇⠀⠀⠈⠻⣿⣇⠀⠀⢸⣿⡤⠋⠀⢀⡆⠀⠀⠀
                                                                                                    ⠀⠀⠀⢘⣿⣦⣀⠀⠀⠈⠙⠀⠀⠟⠉⠀⠀⣠⣾⡿⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⣿⣿⣿⣷⣤⡀⠀⠀⠀⠀⣀⣴⣿⣿⣿⡏⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⠗⠀⠀⠺⣿⣿⣿⣿⣿⠃⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠈⣿⣿⣿⡟⠁⠀⠀⠀⠀⠈⢿⣿⣿⡿⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠀⠈⣿⠟⢠⣦⠀⠀⠀⠀⣴⡄⠻⣿⠃⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠀⢡⡌⣰⣿⣿⡇⠀⠀⢸⣿⣧⣆⢁⠆⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠀⠀⣿⣿⣿⡟⠀⠀⠀⠀⢻⣿⣿⣿⠀⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠀⠀⢻⣿⣿⠁⠀⠀⠀⠀⠈⣿⣿⡏⠀⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠀⠀⠈⣿⣟⠀⠀⠀⠀⠀⠀⣿⣿⠁⠀⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠀⠀⠀⠸⡇⠀⠀⠀⠀⠀⠀⢹⠇⠀⠀⠀⠀⠀⠀
                                                                                                    ⠀⠀⠀⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠘⠀⠀⠀⠀⠀⠀⠀
                                                                            
                                                                                    
                                                                                        ⠀⠀⠀⠀⠀⣿⡿⠿⠿⠀⣼⡿⠿⣿⡆⢠⣿⠿⢿⣷⠀⣼⡿⠿⣿⡆⢸⣿⠀⣿⡿⠿⠿⠀⠾⢿⣿⠿⠇⠘⣿⡄⣰⡿⠁⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⣿⣧⣤⡄⠀⢿⣧⣤⣤⡁⢨⣿⠀⢀⣿⠀⣿⡇⠀⠀⠁⢸⣿⠀⣿⣧⣤⡄⠀⠀⢸⣿⠀⠀⠀⠘⢿⣿⠁⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⣿⡏⠁⠁⠀⣤⣍⣈⣿⡇⢸⣿⣀⣀⣿⠀⣿⣇⣀⣤⡄⢸⣿⠀⣿⣇⣉⣀⠀⠀⢸⣿⠀⠀⠀⠀⢸⣯⠀⠀⠀⠀⠀⠀⠀
                                                                                        ⠀⠀⠀⠀⠀⠛⠃⠀⠀⠀⠙⠛⠛⠛⠁⠀⠛⠛⠛⠋⠀⠘⠛⠛⠛⠁⠘⠛⠀⠛⠛⠛⠛⠀⠀⠘⠛⠀⠀⠀⠀⠘⠋⠀
                                                                
                                                                                    
                                                    :::.    :::.           `::                              :::                              ::::::::::::   ...         ...      :::     
                                                    `;;;;,  `;;;            ;;                              ;;; .;;, ;;,                     ;;;;;;;;''''.;;;;;;;.   .;;;;;;;.   ;;;     
                                                    [[[[[. '[[,cc[[[cc.=[[[[[[.'[[, [[, [[',ccc,  =,,[[== [[[[[/'     [ccccc,   ,ccc,           [[    ,[[     \[[,,[[     \[[, [[[     
                                                    $$$ "Y$c$$$$$___--'   $$     Y$ $$$ $P$$$"c$$$`$$$"``_$$$$,    $$$$$$$"$$$ $$$cc$$$         $$    $$$,     $$$$$$,     $$$ $$'     
                                                    888    Y8888b    ,o,  88,     "88"888 888   88 888   "888"88o, 888888  Y88o888   888        88,   "888,_ _,88P"888,_ _,88Po88oo,.__
                                                    MMM     YM "YUMMMMP"  MMM      "M "M"  "YUMMP  "MM,   MMM "MMP"MMMMMM  "MMM "YUM" MP        MMM     "YMMMMMP"   "YMMMMMP" "YUMMM
                                                                                                                                    MMM                                               
                                                                                                                                ,c.   ###                                               
                                                                                                                                \M###MMU                                                
                                                                                                                                        
                                                                                                                         
          """,0.00000005)



# ============== CURRENT TIME ============== #
def currentTime():
    return datetime.now().strftime("%H:%M:%S")

timeStamp = f"{RESET}[{currentTime()}]{BLUE} Info: {RESET}"


# ============== OPEN PORTS ============== #
def checkOpenPorts():
    
    # Array Clear
    open_ports.clear()

    target = input("Target IPv4/Domain: ")
    maxPortChecks = int(input("Ports to check: "))
    
    # Max ports to check
    ports = range(0, maxPortChecks)

    print(f"Scan läuft auf {target}...")

    def scan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(1)

        print(f"{timeStamp}Checking Port: [#{port}]")

        result = s.connect_ex((target, port))
        if result == 0:
            print(f"{RESET} [+] Port {BLUE}{port} {RESET}open")
            open_ports.append(port)
            

        s.close()

    # Erstellt MAXIMUM 200 Threads 
    with ThreadPoolExecutor(max_workers=200) as executor:
        for port in ports:
            # Für jeden Port yoloooo
            executor.submit(scan,port)

    clearConsole()
    
    if len(open_ports) > 0:
        type_text(f"Open Ports: {open_ports}",0.03)
        
        # Erstellt MAXIMUM 200 Threads 
        for port in open_ports:
        
            fulladress = f"{target}:{port}"
            
            get_service_banner(target,port)
            #get_http_banner(target,port)
            #get_ftp_banner(target,port)
            
            print(f"{timeStamp}{fulladress}")
    input(f"{timeStamp}Exit...")



def get_http_banner(host, port):
    try:
        # Erstellt Verbindung zwischen User und Server
        s = socket.socket()
        s.settimeout(1)
        # Verbindet sich
        s.connect((host, port))
        
        # Sendet Command zum Website aufmachen
        s.send(b"GET / HTTP/1.1\r\nHost: " + host.encode() + b"\r\n\r\n")
        answer = s.recv(1024)
        s.close()

        shortAnswer = answer.decode(errors="ignore")
        status = shortAnswer.split("\n")[0]
        print("Status: ",status)

    except Exception as e:
        print("Fehler",e)

   

def get_service_banner(host, port):

    s = socket.socket()
    s.settimeout(3)
    
    try:
        s.connect((host, port))

        banner = s.recv(1024).decode(errors="ignore")

        print("Banner:", banner)

        if banner.startswith("SSH"):
            print("SSH Server gefunden")

        elif "ESMTP" in banner:
            print("SMTP Mailserver gefunden")

        elif banner.startswith("220"):
            print("FTP möglich")

        else:
            print("Unbekannter Dienst")
        s.close()

    except Exception as e:
        print("Keine Banner Antwort")




def ftp_login():
    
    # Login Input
    host = input("IPv4 / Domain")
    port = input("Port: ")
    username = input("Username: ")
    password = input("Password: ")

    # Verbindung herstellen
    s = socket.socket()
    # 5 Sekunden warten
    s.settimeout(5)

    try:
        # Verbindung
        s.connect((host, port))
        
        # Begrüßung holen
        print(s.recv(1024).decode(errors="ignore"))

        # TLS starten
        s.send(b"AUTH TLS\r\n")
        print(s.recv(1024).decode(errors="ignore"))

        # TLS aktivieren
        # TLS = Transport Layer Security
        context = ssl._create_unverified_context()

        s = context.wrap_socket(
            s,
            server_hostname=host
        )

        # Benutzer
        s.send(f"USER {username}\r\n".encode())
        print(s.recv(1024).decode(errors="ignore"))

        # Passwort
        s.send(f"PASS {password}\r\n".encode())

        login = s.recv(1024).decode(errors="ignore")

        print(login)
        s.send(b"PBSZ 0\r\n")
        print(s.recv(1024).decode())

        s.send(b"PROT P\r\n")
        print(s.recv(1024).decode())

        s.send(b"PWD\r\n")
        print(s.recv(1024).decode())
        if login.startswith("230"):
            print(f"{GREEN}Erfolgreich eingeloggt")            
            
            s.send(b"HELP\r\n")
            while True:
                data = s.recv(4096).decode(errors="ignore")
                print(data)

                if "214 " in data:
                    break

        elif login.startswith("530"):
            print(f"{RED}Login fehlgeschlagen")

        else:
            print(f"{BLUE}Unbekannte Antwort")


    except TimeoutError:
        print("Timeout")

    except Exception as e:
        print("Fehler:", e)

    finally:
        s.close()



# ============== CHECK PING ============== #
def checkPing():
    ip = input("Target IPv4: ")
    #for ip in IPs_toCheck:
        
        # -n 4 = 4 Pings senden 
        # > nul = Output verstecken
        # Einfachster Weg nen Command von CMD abzusenden!
        # request = os.system("systeminfo")
        # 0 = funktioniert 1 = fehler
        # os.system("ipconfig")
    type_text(f"{timeStamp}Starting Ping at: {ip}",0.003)
    result = os.system(f"ping -n 4 {ip} > nul")
        
    if result == 0:
        print(f"{timeStamp}UP {ip} Ping successful")
    else:
        print(f"{timeStamp}DOWN {ip} Ping error")
    
    #OPTIONS
    print("\n")
    type_text("OPTIONS",0.0003)
    type_text("1. Main Menu",0.0003)
    
    choice = input("Select: ")  
    
    if choice == "1":
        clearConsole()
        header()
        menu()
        return
    else:
        return
        


# ============== MAIN MENU ============== #
def menu():
    header()
    print(f"{RESET}1. Check Ping")
    print(f"{RESET}2. Check Open Ports")
    print(f"{RESET}3. View Port Infomations")
    print(f"{RESET}4. Login FTP")
    print(f"{RESET}5. View Usage")
    print(f"{RESET}6. System Infos")

    choice = input("Chose Option: ")

    if choice == "1":
        clearConsole()
        header()
        checkPing()
    elif choice == "2":
        clearConsole()
        header()
        checkOpenPorts()
    elif choice == "3":
        clearConsole()
        get_service_banner()
    elif choice == "4":
        clearConsole()
        ftp_login()
    elif choice == "5":
        clearConsole()
        liveStats()
    elif choice == "6":
        clearConsole()
        systemInfo()


# ============== USAGE COMPONENTS ============== #
def liveStats():
    while True:
        clearConsole()
        ram = round(psutil.virtual_memory().total/(1024**3),1)
        cpu = psutil.cpu_percent()
        type_text(f"RAM usage: {ram}GB",0.03)
        type_text(f"CPU usage: {cpu}%",0.03)
        time.sleep(1)

def systemInfo():
    print("Options")
    print("1. Important")
    print("2. All Infomations")
    choice = input("Choice: ")
    if choice == "1":
        clearConsole()
        header()

        sysInfo = subprocess.check_output("systeminfo", text=True,encoding="utf-8",errors="ignore")
        for line in sysInfo.splitlines():
            if "Betriebssystemname" in line:
                print(line)
            if "Hostname" in line:
                print(line)
            if "Registrierter Benutzer" in line:
                print(line)
    elif choice == "2":
        clearConsole()
        header()
        sysInfo = os.system("systeminfo")
        
        
menu()
