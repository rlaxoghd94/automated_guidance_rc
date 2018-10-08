from pynput.keyboard import Key, Listener
from time import sleep
import sys
import requests
import json
delay_time = 0.3
url = 'http://0.0.0.0:8001/control/'

def send_server(key):
    global url
    val = 'e'
    if (key == 'a'):
            val = 'LEFT'
    elif (key == 's'):
            val = 'STOP'
    elif (key == 'd'):
            val = 'RIGHT'
    elif (key == 'w'):
            val = 'FORWARD'
    elif (key == 'q'):
            val = 'QUIT'
   
    payload = {
        'key': val
    }

    r = requests.post(url, data=json.dumps(payload))


def on_press(key):
    if (key.char == 'a' or key.char == 's' or key.char == 'w' or key.char == 'd' or key.char == 'q'):
            print('Send: %s' % key.char)
            send_server(key.char)
    

with Listener(
    on_press=on_press) as listener:
        listener.join()
