import time
import paho.mqtt.client as paho
import serial
import re
import json
import os
from datetime import datetime
from camera import takePhoto


# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = "/dev/ttyS0"
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600


def mqtt(data):

    try:
        takePhoto()
    except Exception as e:
        print("type error: " + str(e) + " problem with camera!")

    keys = ["ID", "STA", "SHA", "SL_1", "SL_2", "STS1", "STS2", "STS3", "SHS1", "SHS2", "SHS3", "SVB", "SPL", "SPR"]
    values = re.split("\s+", data)
    values = [x for x in values if x]  # remove null items
    new_dict = dict(zip(keys, values))
    new_dict["TIME"] = str(datetime.now())
    print("received message =", new_dict)
    topic = "LISIMETRO"
    print("TOPIC: ", topic)
    data = {
        "ID": new_dict["ID"],
        "TIME": new_dict["TIME"],
        "SVB": new_dict["SVB"],
        "STA": new_dict["STA"],
        "SHA": new_dict["SHA"],
        "SL_1": new_dict["SL_1"],
	"SL_2": new_dict["SL_2"],
        "SPL": new_dict["SPL"],
        "SPR": new_dict["SPR"],
        "STS1": new_dict["STS1"],
        "STS2": new_dict["STS2"],
        "STS3": new_dict["STS3"],
        "SHS1": new_dict["SHS1"],
        "SHS2": new_dict["SHS2"],
        "SHS3": new_dict["SHS3"]
    }

    data = json.dumps(data, ensure_ascii=True)
    print("JSON DUMP =", data)
    #broker = "94.62.172.88"
    broker = "ietsis.dynu.net"
    # reading is a string...do whatever you want from here
    client = paho.Client("client-001")
    print("connecting to broker ", broker)
    client.connect(broker, 1883, 60)  # connect
    client.loop_start()  # start loop to process received messages
    client.subscribe(topic)  # subscribe
    client.publish(topic, data)  # publish
    time.sleep(4)
    client.disconnect()  # disconnect
    client.loop_stop()  # stop loop
#    print('prepare shutdown')
#    os.system("sudo shutdown -h now")


def main():
    print("A espera de dados")
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println()
        reading = ser.readline().decode("utf-8")
        mqtt(reading)


if __name__ == "__main__":
   main()

