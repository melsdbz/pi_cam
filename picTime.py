import time
import datetime
import os
from picamera import PiCamera

#paths for pictures
path1 = "/var/www/pi_cam/static/"
path2 = "/var/www/pi_cam/timelapse_pics/"

def deleteCurrent(path1):
    if "current.jpg" in os.listdir(path1):
        os.remove(path1+"current.jpg")

def takepic(camera, path1, path2):
    x = datetime.datetime.now()
    y = x.strftime("%y-%m-%d-%H%M")
    camera.start_preview()
    time.sleep(2)
    camera.capture(path2+y+".jpg")
    time.sleep(2)
    camera.capture(path1+"current.jpg")

#create camera
camera = PiCamera()
camera.resolution = (2800, 2100)

#delete current photo
deleteCurrent(path1)

#take new pictures and put one in timelapse pics and one in the current folder
takepic(camera, path1, path2)

