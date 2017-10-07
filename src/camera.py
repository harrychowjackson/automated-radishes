import time
import picamera
import os
import io
import sys
from datetime import datetime

class Webcam(object):
    def __init__(self):
        self.saveDir = '/home/pi/Desktop/camera/'
        self.image_format = '.jpg'

    def record_video(self, seconds=20, framerate=60, preview=True, format='h264'):
        camera = picamera.PiCamera(framerate=framerate)
        stream = picamera.PiCameraCircularIO(camera, seconds=seconds)
        if preview is True:
            camera.start_preview()
            camera.start_recording(stream, format=format)
            time.sleep(seconds)
            camera.stop_recording()
            camera.stop_preview()
        else:
            camera.start_recording(stream, format=format)
            time.sleep(seconds)
            camera.stop_recording()
        camera.close()
        for frame in stream.frames:
            if frame.header:
                stream.seek(frame.position)
                break
        with io.open(self.saveDir + 'video.h256', 'wb') as output:
            data = stream.read1()
            while data:
                output.write(data)
                data = stream.read1()

    def timelapse_photos(self, image_name='', append_time=True, interval=10, length_of_time=31536000):
        camera = picamera.PiCamera()
        iterations = int(length_of_time / interval)
        try:
            if append_time is True:
                for i in range(iterations):
                    camera.capture(self.saveDir + str(datetime.now()) + image_name + str(i) + self.image_format)
                    time.sleep(interval)
            else:
                for i in range(iterations):
                    camera.capture(self.saveDir + image_name + str(i) + self.image_format)
                    time.sleep(interval)
        finally:
            camera.close()

    def take_photo(self, image_name='', append_time=True):
        camera = picamera.PiCamera()
        try:
            if append_time is True:
                camera.capture(self.saveDir + str(datetime.now()) + image_name + str(i) + self.image_format)
                time.sleep(interval)
            else:
                camera.capture(self.saveDir + image_name + str(i) + self.image_format)
                time.sleep(interval)
        finally:
            camera.close()

cam = Webcam()
#cam.timelapse_photos(interval=5, image_name='test', length_of_time=60)
cam.record_video(seconds=10, preview=True)
