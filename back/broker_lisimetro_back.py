import time
import paho.mqtt.client as paho
import serial
import re
import json

# this port address is for the serial tx/rx pins on the GPIO header
SERIAL_PORT = "/dev/ttyS0"
# be sure to set this to the same rate used on the Arduino
SERIAL_RATE = 9600

def mqtt(data):
        keys = ["ID", "STA", "SHA", "SLA", "STS1", "STS2", "STS3", "SHS1", "SHS2", "SHS3", "SPL", "SPR", "SVB"]
        values = re.split("\s+", data)
        values = [x for x in values if x] #remove itens nulos
        #print("KEYS: ", keys)
        #print("VALUES: ", values)
        new_dict = dict(zip(keys, values))
        print("received message =", new_dict)
        topic = "LIS_ID: " + new_dict["ID"]
        print("TOPIC: ", topic)
        data = json.dumps(new_dict, ensure_ascii=False)
        #print("JSON DUMP =", data)
        #data = json.loads(str(data))
        #print("JSON LOADS =", data)
        broker="94.62.172.88"
        # reading is a string...do whatever you want from here
        # print(reading)
        client= paho.Client("client-001") #create client object client1.on_publish = on_publish #assign function to callback client1.connect(broker,port) #establish connection client1.publish("house/bulb1","on")
        print("connecting to broker ", broker)
        client.connect(broker) #connect
        client.loop_start() #start loop to process received messages
        #print("subscribing ")
        client.subscribe(topic) #subscribe
        #time.sleep(2)
        #print("publishing ")
        client.publish(topic, "{\"" + topic +"\"" + ":"+ data.replace("\"", "\"") + "}") #publish
        time.sleep(4)
        client.disconnect() #disconnect
        client.loop_stop() #stop loop

def main():
        ser = serial.Serial(SERIAL_PORT, SERIAL_RATE)
        while True:
                # using ser.readline() assumes each line contains a single reading
                # sent using Serial.println()
                reading = ser.readline().decode("utf-8")
                mqtt(reading)
                
if __name__ == "__main__":
        main()
