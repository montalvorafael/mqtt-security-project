import paho.mqtt.client as mqtt
import time

def on_message(client, userdata, msg):
    sent = float(msg.payload.decode())
    latency = time.time() - sent
    print(f"[SUBSCRIBER] Latency: {latency:.4f} sec")

client = mqtt.Client()
client.connect("localhost", 1883, 60)
client.subscribe("sensor/temp")
client.on_message = on_message
client.loop_forever()
