import json
import requests
from time import time, sleep, gmtime, strftime

def fetch_image(counter):
    file_name = 'image%s.jpg' % counter
    data = {'file_name': file_name, 'file_format': '.jpg'}
    files = {'files': open('./temp.JPG', 'rb')}
    r_data = [data, files];

    return r_data

def parse_response(r):
    if str( r.content, 'utf-8') == '200':
        return True
    else:
        return False

def wait(duration):
    if (duration <= 0.1):
        sleep( 0.1 - int(duration))
    elif (duration > 0.1 and duration <= 0.2):
        sleep( 0.2 - int(duration))


url = "http://0.0.0.0:8000/upload/snapshot/{}"
status = True
counter = 0

while(status):
    start = time()
    r_data = fetch_image(counter)
    print('\t\trequest at: ' + url.format(r_data[0].get('file_name')))
    r = requests.post(url.format(r_data[0].get('file_name')), files=r_data[1])
    
    finish = time()
    duration = finish - start
    print(str(r.content, 'utf-8') + ' duration= %s' % duration)
    
    status = parse_response(r)
    wait(duration)
    counter += 1

