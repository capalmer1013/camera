import socket
import time
import picamera

camera = picamera.PiCamera()
camera.resolution = (640, 480)
camera.framerate = 24

sock = socket.socket()
sock.connect(('0.0.0.0', 8000))
sock.listen(0)

connection = sock.accept()[0].makefile('wb')

try:
    camera.start_recording(connection, format='h264')
    camera.wait_recording(60)
    camera.stop_recording()
finally:
    connection.close()
    sock.close()
