import picamera
import io
import requests
import json
from time import time, sleep, gmtime, strftime
from datetime import datetime, timedelta

def send_image(stream):
    global counter
    file_name = 'image%02d.jpg' % counter
    counter += 1
    data = {'file_name': file_name, 'file_format': '.jpg'}
    files = {'files': stream}
    r_data = [data, files]
    r = requests.post(url.format(r_data[0].get('file_name')), files=r_data[1])
    return parse_response(r)


def parse_response(r):
    if str( r.content, 'utf-8' ) == '200':
        return True
    else:
        return False

def wait(duration):
        print('\t\t[+ duration] %.2f' % duration)
        if (duration <= 0.1):
            sleep( 0.1 - int(duration) )

url = "http://203.252.160.76:8000/upload/snapshot/{}"
status = True
counter = 0

with picamera.PiCamera() as camera:
    camera.resolution = (256, 256)
    camera.framerate = 30
    camera.start_preview()
    sleep(1)

    ts = strftime('%Y%m%d_%H:%M:%S', gmtime())

    start = time()
    stream = io.BytesIO()
    # continously captures image until interrupted
    for filename in camera.capture_continuous( stream, format='jpeg', use_video_port=True):
        # truncate the stream to the current position
        # just in case prior iterations output a longer image
        #stream.truncate()
        stream.seek(0)
        if (send_image(stream) == False):
            break
        else :
            stream.seek(0)
            stream.truncate()
        finish = time()
        print('Captured %s at %.2ffps duration: %.2f sec' % (filename, (1 / (finish - start)), (finish - start)))
        wait(finish-start)
        start = time()
