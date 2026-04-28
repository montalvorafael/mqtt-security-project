import paho.mqtt.client as mqtt
import time

client = mqtt.Client()
client.connect("localhost", 1883, 60)

while True:
    msg = str(time.time())
    client.publish("sensor/temp", msg)
    print("[PUBLISHER] Sent message")
    time.sleep(1)
