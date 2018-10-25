from flask import Flask, request, jsonify, make_response, send_file
import json
import picamera
import io
import serial
from time import sleep, time

app = Flask( __name__ )
#ser = serial.Serial('/dev/ttyACM0', 9600)

cnt = -1
@app.route('/control/', methods=['POST'])
def control():
    global cnt, ser
    if request.method == 'POST':
        print('\n\t\t' + str(request.data, 'utf-8') + '\n')
        d = json.loads(str(request.data, 'utf-8'))
        print(d['key'].encode())

        # TODO: SEND SERIAL SIGNAL HERE
 #       ser.write(str.encode(d['key']+'\n'))

        with picamera.PiCamera() as camera:
            camera.resolution=(256, 256)
            camera.framerate=60
            f = 'temp_file.jpg'
            camera.capture(f, format='jpeg', use_video_port=True)
            #val_f = open(f, 'r').read()
            #var = base64.b64encode(str(val_f).encode())
            #var = base64.encodestring(open( f, 'rb' ).read())
        #rtn_payload = make_json_response(200, val_f)
        #rtn_payload.headers['content-type'] = 'application/json'
        #print('\n\tjson.load: %s\n' % rtn_payload)
        #return rtn_payload
        try:
            cnt += 1
            return send_file('./temp_file.jpg', attachment_filename='%s_%02d.jpg' % (d['key'], cnt), mimetype='image/png')
        except Exception as e:
            print(str(e))
            return str(e)

def make_json_response(status_code, image_str):
        #response = jsonify( {
        #    'resultCode': status_code,
        #    'data': image_str,
        #})
        #response.status_code = status_code
        
        response = json.dumps( {
            'resultCode': status_code,
            'data': image_str
        })
        
        return make_response(response, 200)

if __name__ == '__main__':
    app.run( host='0.0.0.0', port=8001, debug=True )

#stream = io.BytesIO()
#with picamera.PiCamera() as camera:
#        camera.resolution(256, 256)
#        camera.framerate = 90
#        sleep(1)

# TODO: need to implement 1 req: 1 response function HERE
