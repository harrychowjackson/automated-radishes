"""
camera.py - Webcam API for the FUTURE.
Radish'n'bots, LLC
  modified : 1/27/2020
"""
import time
try:
  import picamera
except ImportError:
  print(str(ImportError))
  import cv2 as picamera
import os
import io
import sys
import cv2
import datetime

## Global declarations or something.
_EPOCH = datetime.datetime(1970,1,1)
_RESOLUTIONS = {
  '1080p': {
    'width': 1920,
    'height': 1080
    },
  '720p': {
    'width': 1280,
    'height': 720
    }
  }
_FORMATS = {
    'image': ['png', 'jpg'],
    'video': ['mp4']
    }
_DEFAULT = {
  'video_format': 'mp4',
  'image_format': 'png',
  'resolution': '1080p'
  }


## Local functions.
def _get_time_now(time_format='utc'):
  """
  Thanks Jon.  (;
  :in: time_format (str) ['utc','epoch']
  :out: timestamp (str)
  """
  if time_format == 'utc' or time_format == 'label':
    return datetime.datetime.utcnow().strftime("%Y%m%d_%H%M%S")
  elif time_format == 'epoch' or time_format == 'timestamp':
    td = datetime.datetime.utcnow() - _EPOCH
    return str(td.total_seconds()).replace('.','_')
  else:
    # NOTE: Failure to specify an appropriate time_format will cost
    #         you one layer of recursion! YOU HAVE BEEN WARNED.  ) 0 o .
    return _get_time_now(time_format='epoch')

def _verify_cv2_port(port_index):
  """
  Check a port index through CV2.
  :in: port_index (int) cv2-friendly port to check
  :out: available (bool) is device ready for communication?
  """
  available = False
  cam = cv2.VideoCapture(port_index)
  if cam and cam.isOpened():
    available = True
  cam.release()
  return available


# TODO: Import from Device class.
class Camera(object):
  def __init__(
      self, device_address,
      serial_number='', device_type='usb_camera'):
    ## TODO: Integrate below into generic Device class.
    self.device_address = str(device_address)   # Save device address as a string.
    self.base_data_path = './'
    setup_info = {
        'serial_number': serial_number,
        'device_type': device_type
        }
    # Fill in the blanks.
    self.info = self._query_info(setup_info)
    self.info['device_id']= self._get_device_id()
    ##

  def _query_info(self, old_info={}):
    """
    Chat up the device to find where it lives as well
      as how to get into its front door.
    :in: old_info {dict} - any old metadata 'bout the device.
    :out: info {dict}
    """
    info = {
        'serial_number': '1',
        'device_type': 'usb_camera',
        'image_format': 'png',
        'device_address': self.device_address,
        'resolution': '720p',
        'framerate': 15
        }
    info.update(old_info)
    return info

  def _get_device_id(self):
    """
    Hunt down the device ID.
    :out: serial_number (str)
    """
    unique_ids = [
        self.info['device_type'],
        self.info['serial_number'],
        self.info['device_address'].replace('/','_')]
    return '-'.join(unique_ids)


  def set_up(self):
    """
    Verify device properly connected:
      1. Verify that address of device specifies a valid OpenCV index.
    """
    available = False
    available = _verify_cv2_port(int(self.device_address))
    if not available:
      print(''.join([
        'ERROR   : Unable to communicate with camera source ',
        self.device_address,'!']))
      raise IOError

  def set_data_path(self, path_base):
    """
    Set the base of the output path for data flow.
    :in: path_base (str)
    """
    if os.path.isdir(path_base):
      self.base_data_path = path_base
    else:
      print(''.join([
        'WARNING : Cannot set path base to ',
        str(path_base), '; directory does not exist! Using next deepest...']))

  def take_picture(self, label='test'):
    """
    Camera specific method!
    """
    ## Get resolution.
    try:
      resolution = self.info['resolution']
      frame_w = _RESOLUTIONS[resolution]['width']
      frame_h = _RESOLUTIONS[resolution]['height']
    except:
      print(''.join([
      'WARNING : Resolution ', self.info['resolution'],
      ' unsupported; default to ', _DEFAULT['resolution'],'.']))
      resolution = _DEFAULT['resolution']
      frame_w = _RESOLUTIONS[resolution]['width']
      frame_h = _RESOLUTIONS[resolution]['height']

    ## Get image format.
    image_format = self.info['image_format']
    if not image_format in _FORMATS['image']:
      print(''.join([
      'WARNING : Picture format ', self.info['image_format'],
      ' unsupported; default to ', _DEFAULT['image_format'],'.']))
      image_format = _DEFAULT['image_format']

    ## Generate image label.
    timestamp = _get_time_now('timestamp')
    image_label = '.'.join([
      '-'.join([
        self.base_data_path+timestamp,
        str(self.device_address),
        label]),
      image_format])
    
    ## Take a pic.
    cam = cv2.VideoCapture(int(self.device_address))
    ret, frame = cam.read()
    cv2.imwrite(image_label, frame)
    cam.release()

    ## Verify that file exists.
    # TODO
    
  def clean_up(self):
    """
    Take out the trash.
    """
    return
  

class Webcam(object):
    def __init__(self,camera_type='PiCamera'):
        self.saveDir = '/home/pi/Desktop/camera/'
        self.image_format = '.jpg'
        self.camera_type = camera_type

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
                    camera.capture(self.saveDir + str(datetime.datetime.now()) + image_name + str(i) + self.image_format)
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
                camera.capture(self.saveDir + str(datetime.datetime.now()) + image_name + str(i) + self.image_format)
                time.sleep(interval)
            else:
                camera.capture(self.saveDir + image_name + str(i) + self.image_format)
                time.sleep(interval)
        finally:
            camera.close()


def _get_available_camera_indices():
  index_max = 8
  available_indices = []
  for index in range(0,index_max,1):
    cam = cv2.VideoCapture(index)
    if cam and cam.isOpened():
      available_indices.append(index)
    cam.release()
  return available_indices

def test_camera():
  # Set up.
  base_dc_dir = './test_data/'
  if not os.path.isdir(base_dc_dir):
    os.mkdir(base_dc_dir)
  # Find each available camera.
  available_camera_indices = _get_available_camera_indices()
  device_address = max(available_camera_indices)

  # Test the camera.
  cam = Camera(device_address)
  cam.set_up()
  cam.set_data_path(base_dc_dir)
  time.sleep(10)
  cam.take_picture()
  time.sleep(5)
  cam.take_picture('yellow_oyster')
  cam.clean_up()

if __name__ == '__main__':
  test_camera()

#cam = Webcam()
#cam.timelapse_photos(interval=5, image_name='test', length_of_time=60)
#cam.record_video(seconds=10, preview=True)
