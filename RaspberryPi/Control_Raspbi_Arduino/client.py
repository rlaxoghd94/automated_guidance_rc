from pynput.keyboard import Key, Listener
from time import sleep
import sys
import io
import base64
import requests
import json
import binascii

delay_time = 0.3
url = 'http://0.0.0.0:8001/control/'
val = 'e'
cnt = 0

def send_server(key):
    global url, val, cnt
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

    print('\n\n\t\tjson: {}'.format(json.dumps(payload)))
    r = requests.post(url, data=json.dumps(payload))
    #parseRequest(r)
    print('\n\n\t\tresponse: {}'.format(r))
    file_f = open('./image_data/%s_%02.d.jpg' % (val, cnt), 'wb')
    file_f.write(r.content)
    file_f.close()
    cnt += 1

def parseRequest(r):
    global cnt
    print('\n\nr: %s\n\n' % r)
    
    #data = json.dumps(r, default=set_default)
    data = json.loads(r.text)

    resultCode = data['resultCode']

    if (resultCode != 200):
        sys.exit(-1)

    img_str = data['data']
    #img_data = base64.b64decode(img_str)
    #img_data = decode_base64(img_str)
    #fh = open('./image_data/val_%02d.jpg' % cnt, 'wb')
    #fh.write(img_data.decode('base64'))
    #fh.close()

    with open('./image_data/val_%02d.jpg' % cnt, 'w') as f:
            f.write(img_str)

    cnt += 1

def decode_base64(data):
    lens = len(data)
    lenx = lens - (lens % 4 if lens % 4 else 4)
    try:
        result = base64.decodestring(data[:lenx])
        return result
    except base64.binascii.Error as err:
        pass

def on_press(key):
    if (key.char == 'a' or key.char == 's' or key.char == 'w' or key.char == 'd' or key.char == 'q'):
            print('Send: %s' % key.char)
            send_server(key.char)
    

with Listener(
    on_press=on_press) as listener:
        listener.join()
