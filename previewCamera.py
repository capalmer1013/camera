import picamera

camera = picamera.PiCamera()

camera.brightness = 70
camera.contrast = 50
#camera.ISO = 800

camera.start_preview()
