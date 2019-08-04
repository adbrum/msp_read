#!/usr/bin/env python
from picamera import PiCamera
from time import sleep
import datetime
from copyimage import copyImage


PATH = "/home/pi/lisimetro/image/"
PHOTO = "%Y-%m-%d_%H-%M-%S_%f"


def takePhoto():

    camera = PiCamera()
    name_photo = datetime.datetime.now().strftime(PHOTO) + ".jpg"
    #print(name_photo)
    try:
        camera.capture(PATH + name_photo)
        sleep(5)
        copyImage(name_photo)
    except Exception as e:
        print("type error: " + str(e))


def main():
    takePhoto()


if __name__ == "__main__":
    main()
