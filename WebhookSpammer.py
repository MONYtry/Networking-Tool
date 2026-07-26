import requests
from concurrent.futures import ThreadPoolExecutor
import time


print("Webhook - Settings")
WEBHOOK_URL = "https://discord.com/api/webhooks/1442989111807049929/rxXCiaojjQOU3sXT1vXmloQCSAkOiy-N_xvYZIu7a6LPxJh9ZeR8qztem6aT_soysXcw"
MESSAGE = input("Message: ")
REPEAT = int(input("REPEAT: "))

print("Webhook - Style")
USERNAME = input("Username: ")
PROFILE_URL = "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFYgWzP8SP-RtYpoy3p9ss4mbLqp86OBTJVk1bIt-_lA&s=10"#input("URL Profile: ")
sended = 0
def sendWebhook():
    global sended
    sended += 1

    print(f"Sended: [#{sended}]")
    # Als Json Formatieren
    data = {
        
        "username": USERNAME    ,
        "avatar_url": PROFILE_URL,
        "embeds": [{
            "color": 0xFF000,
            "title": "G0T FUCKED",
            "description": MESSAGE,
            "footer": 
            {
                "text": "THIS SERVER WAS FUCKED BY M0#Y \n\n https://discord.gg/ATDec6x6N2"
            },
            "image":
            {
                "url": "https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQFfSy1tIhLLbN9oJocGdRHDsZYf-1Lmt03OSrwyT5CBg&s=10"
            }
        }]
    }
    response = requests.post(WEBHOOK_URL, json=data)
    if response.status_code == 204:
        print("Succsess")
        

    elif response.status_code in(429,404):
        retry = response.json()["retry_after"]
        print(f"Rate Limit! Warte {retry} Sekunden...")
        time.sleep(retry)
        requests.post(WEBHOOK_URL, json=data)

    else:
        print(response.status_code) 
    
for i in range(REPEAT):
    sendWebhook()
