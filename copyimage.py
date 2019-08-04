#!/usr/bin/python
#import os

HOST = "lisimetro@ietsis.dynu.net:"
PORT = "1022"
LOCAL_PATH = "/home/pi/lisimetro/image"
SERVER_PATH = "/home/lisimetro/image"


def copyImage(name):
    print("scp -P " + PORT + " " + LOCAL_PATH + name + " " + HOST + SERVER_PATH)
