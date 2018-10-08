from flask import Flask, request
import json
import picamera
from time import sleep, time

app = Flask( __name__ )

@app.route('/control/', methods=['POST'])
def control():
    if request.method == 'POST':
        print('\n\t\t' + str(request.data, 'utf-8') + '\n')
        d = json.loads(str(request.data, 'utf-8'))
        print(d['key'])
        return '200'
       
if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8001, debug=True )


with picamera.PiCamera() as camera:
        camera.resolution(256, 256)
        camera.framerate = 90
        sleep(1)

        start = time()
        stream = io.BytesIO()
# TODO: need to implement 1 req: 1 response function HERE
