#!/usr/bin/python
import os

HOST = "lisimetro@ietsis.dynu.net:"
PORT = "1022"
LOCAL_PATH = "/home/pi/lisimetro/image/"
SERVER_PATH = "/home/lisimetro/image"


def copyImage(name):
    os.system("scp -P " + PORT + " " + LOCAL_PATH + name + " " + HOST + SERVER_PATH)
    os.system("rm " + LOCAL_PATH + name)
    #os.system("mv " + LOCAL_PATH + name + " " + HOST + PORT + SERVER_PATH + name)
    print("Done!")
