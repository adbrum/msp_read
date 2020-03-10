#!/usr/bin/python
import os

HOST = "lisimetro@ietsis.dynu.net:"
PORT = "22"
LOCAL_PATH = "/home/pi/lisimetro/image/"
SERVER_PATH = "/home/lisimetro/image"



def copyImage():
    print("scp -P "+ PORT + " " + LOCAL_PATH + "*.jpg " + HOST + SERVER_PATH)
    os.system("scp -r -P " + PORT + " " + LOCAL_PATH + "*.* " + HOST + SERVER_PATH)
    os.system("rm " + LOCAL_PATH + "*.*")
    print("Done!")

def main():
    copyImage()


if __name__ == "__main__":
    main()

