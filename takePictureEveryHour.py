import time
import picamera
import os
from fractions import Fraction

os.environ['TZ'] = 'America/New_York'

htmlTemplate = """
<!DOCTYPE html>
<html>
<body>

<h2>%s</h2>
<img src="image.jpg">

</body>
</html>
"""
while True:
    camera = picamera.PiCamera()
    try:
        camera.vflip = True
        camera.hflip = True
    
        hour = time.localtime()[3]
        camera.iso = 800
        camera.brightness = 70
        camera.contrast = 50
        currentTime = time.strftime("%X, %x", time.localtime())
        print "taking picture", currentTime
        with open("/var/www/html/pic/index.html", "w+") as htmlOut:
            htmlOut.write(htmlTemplate % (currentTime))

        camera.capture('/var/www/html/pic/image.jpg')
    
    except:
        pass

    camera.close()
    time.sleep(1800)
