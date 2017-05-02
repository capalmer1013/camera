from flask import Flask
from flask_cors import CORS
import picamera
import os
import moveServo
import time

os.environ['TZ'] = 'America/New_York'

htmlTemplate = """
<!DOCTYPE html>
<html>
<body>
<h2>%s</h2>
<img src="image.jpg">
<br/>
<input type="range" min="0" max="100" value="0" onchange="showValue(this.value)" />
<span id="range">0</span>
<button type="button" onclick="updateButton()">Update</button>

<script type="text/javascript">
function updateButton()
{
    var a = document.getElementById("range").innerHTML;
      var xhttp = new XMLHttpRequest({mozSystem: true});
      console.log(a)
      console.log("http://capalmer1013.co.uk:5000/moveCamera/"+a)
      xhttp.open("GET", "http://capalmer1013.co.uk:5000/moveCamera/"+a, false);
      xhttp.send();
      setTimeout(function(){ location.reload(true); }, 2000);
}
function showValue(newValue)
{
    document.getElementById("range").innerHTML=newValue;
}
setInterval(function(){location.reload(true)}, 10000);
</script>
</body>
</html>
"""
app = Flask(__name__)

CORS(app)

@app.route("/")
def test():
    return "test"

@app.route("/test")
def test2():
    return "test2 success"
    
@app.route("/<angle>")
@app.route("/moveCamera/<angle>")
def moveCamera(angle=0):
    angle = int(angle)
    moveServo.setAngle(abs(100-(angle*20+500)))
    camera = picamera.PiCamera()
    try:
        camera.vflip = True
        camera.hflip = True
        
        camera.iso = 800
        camera.brightness = 70
        camera.contrast = 50
        currentTime = time.strftime("%X, %x", time.localtime())
        with open("/var/www/html/pic/index.html", "w+") as htmlOut:
            htmlOut.write(htmlTemplate % (currentTime))
            
        camera.capture('/var/www/html/pic/image.jpg')
    except:
        return "failure to chooch"

    camera.close()
    return "updated picture"

# add a route to check the timestamp of last picture
if __name__ == "__main__":
	app.run(host="0.0.0.0")

