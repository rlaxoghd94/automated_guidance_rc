import picamera
import io
from time import time, sleep, gmtime, strftime
from datetime import datetime, timedelta

def wait(duration):
        sleep(0.1 - int(duration))

with picamera.PiCamera() as camera:
        camera.resolution = (256, 256)
        camera.framerate = 90
        #camera.start_preview()
        sleep(1)

        ts = strftime('%Y%m%d_%H:%M:%S', gmtime())
        
        start = time()
        #camera.capture_sequence(['./testFolder/image%02d.jpg' % i for i in range(40)], use_video_port=True)
        for filename in camera.capture_continuous('./testFolder/image{timestamp:%H:%M:%S.%f}.jpg', use_video_port=True):
                finish = time()
                print('Captured %s at %.2ffps duration: %.2f sec' % (filename, (1 / (finish - start)), (finish - start)))
                wait(finish-start)
                start = time()
        
        print('Captured 40 images at %.2ffps' % (40 / (finish - start)))



