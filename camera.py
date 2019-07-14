#!/usr/bin/env python
from picamera import PiCamera
from time import sleep
import datetime
from copyimage import copyImage
import os.path

PATH = "/home/pi/lisimetro/image/"


def takePhoto():

    camera = PiCamera()
    name_photo = datetime.datetime.now().strftime('%Y-%m-%d_%H:%M:%S.%f.jpg')
    sleep(5)
    try:
        camera.capture(PATH + " " + name_photo)
        copyImage(name_photo)
        sleep(2)
    except Exception as e:
        print("type error: " + str(e))


def main():
    takePhotos()


if __name__ == "__main__":
    main()
