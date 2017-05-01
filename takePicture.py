import picamera
import time
from fractions import Fraction

camera = picamera.PiCamera()

#camera.framerate = Fraction(1, 6)
#camera.shutter_speed = 6000000
#camera.exposure_mode = 'off'

camera.iso = 800
camera.ISO = 400


camera.vflip = True
camera.hflip = True
camera.brightness = 70
#time.sleep(10)
camera.contrast = 50
camera.capture('image.jpg')
