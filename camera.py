#!/usr/bin/env python
from picamera import PiCamera
from time import sleep
import datetime
from copyimage import copyImage


PATH = "/home/pi/lisimetro/image/"


def takePhoto():

    camera = PiCamera()
    #name_photo = datetime.datetime.now().strftime('%Y-%m-%d_%H_%M_%S_%f.jpg')
    name_photo = datetime.datetime.now().strftime('%Y%m%d%H%M%S.jpg')
    sleep(5)
    try:
        camera.resolution = (3200, 2400) # 3200 x 2400 = 7.680 MegaPixels/ #1024 x 768 = 0.786 MegaPixels
        camera.capture(PATH + " " + name_photo)
        copyImage()
        sleep(2)
    except Exception as e:
        print("type error: " + str(e))

def main():
    takePhoto()


if __name__ == "__main__":
    main()
