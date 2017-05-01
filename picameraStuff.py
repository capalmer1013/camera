import picamera

camera = picamera.PiCamera()

# take a picture
camera.capture('image.jpg')
# horizontal / vertical flip
camera.hflip = True
camera.vflip = True

# preview
camera.start_preview()
#camera.stop_preview()
# ctrl-D to terminate python session
