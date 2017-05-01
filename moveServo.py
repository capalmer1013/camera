import pigpio
import time
import os

os.system("sudo pigpiod")
s = pigpio.pi()

# if fails call sudo pigpiod

def setAngle(angle, timeout=1.0):
    s.set_servo_pulsewidth(17, angle)
    time.sleep(timeout)
    s.set_servo_pulsewidth(17, 0)

