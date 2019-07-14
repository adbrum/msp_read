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

    keys = ["ID", "STA", "SHA", "SLA", "STS1", "STS2",
            "STS3", "SHS1", "SHS2", "SHS3", "SPL", "SPR", "SVB"]
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
        "SVB": new_dict["SVB"][2] + "." + new_dict["SVB"][3:],
        "STA": new_dict["STA"][2] + "." + new_dict["SVB"][3:],
        "SHA": new_dict["SHA"][3:4] + "." + new_dict["SVB"][5:],
        "SLA": new_dict["SLA"][2:],
        "SPL": new_dict["SPL"][1:2] + "." + new_dict["SVB"][3:],
        "SPR": new_dict["SPR"][2] + "." + new_dict["SVB"][3:],
        "STS1": new_dict["STS1"][3:4] + "." + new_dict["SVB"][5:],
        "STS2": new_dict["STS2"][2:3] + "." + new_dict["SVB"][4:],
        "STS3": new_dict["STS3"][2:3] + "." + new_dict["SVB"][4:],
        "SHS1": new_dict["SHS1"][2:3] + "." + new_dict["SVB"][4:],
        "SHS2": new_dict["SHS2"][2:3] + "." + new_dict["SVB"][4:],
        "SHS3": new_dict["SHS3"][2:3] + "." + new_dict["SVB"][4:]
    }

    data = json.dumps(data, ensure_ascii=True)
    print("JSON DUMP =", data)
    broker = "94.62.172.88"
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
    print('prepare shutdown')
    os.system("shutdown now")


def main():
    ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
    while True:
        # using ser.readline() assumes each line contains a single reading
        # sent using Serial.println()
        reading = ser.readline().decode("utf-8")
        mqtt(reading)


if __name__ == "__main__":
    main()
