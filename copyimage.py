#!/usr/bin/python
#import os

HOST = "lisimetro@94.62.172.88:"
PORT = "1022"
LOCAL_PATH = "~/image/"
SERVER_PATH = "~/image/"


def copyImage(name):
    print("scp -P " + PORT + " " + SERVER_PATH + name + " " + HOST + LOCAL_PATH)
