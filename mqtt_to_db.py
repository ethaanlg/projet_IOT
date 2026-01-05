import json
import paho.mqtt.client as mqtt
from db import save_measurement

MQTT_SERVER = "test.mosquitto.org"
MQTT_PORT   = 1883
MQTT_TOPIC  = "esilv/bme680/ethan"

def on_connect(client, userdata, flags, rc):
    print("Connecté au broker, code:", rc)
    client.subscribe(MQTT_TOPIC)

def on_message(client, userdata, msg):
    print("Message reçu:", msg.payload)
    data = json.loads(msg.payload.decode())
    temp  = data.get("temp")
    hum   = data.get("hum")
    press = data.get("press")
    save_measurement(temp, hum, press)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message

client.connect(MQTT_SERVER, MQTT_PORT, 60)
client.loop_forever()
