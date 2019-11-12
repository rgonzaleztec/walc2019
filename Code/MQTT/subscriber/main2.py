from network import WLAN
from mqtt import MQTTClient
from machine import idle
import time
import pycom

wifi_ssid = "AndroidRojo"
wifi_passwd = ""
broker_addr = "192.168.43.76"
MYDEVID = "__A DEVICE ID__"
valor = 0.0


def settimeout(duration):
   pass

def on_message(topic, msg):
    print("topic is: " + str(topic))
    print("msg is: " + str(msg))
    valor = float(msg)
    if (valor < float(200)):
        pycom.rgbled(0x7f0000)
    else:
        pycom.rgbled(0x0000ff)


wlan = WLAN(mode=WLAN.STA)
nets = wlan.scan()
for net in nets:
    if net.ssid == wifi_ssid:
        print("Network " + wifi_ssid + " found!")
        wlan.connect(net.ssid, auth=(net.sec, wifi_passwd), timeout=5000)
        while not wlan.isconnected():
            #machine.idle() # save power while waiting
            idle() # save power while waiting
        print("WLAN connection succeeded!")
        print (wlan.ifconfig())
        break

client = MQTTClient(MYDEVID, broker_addr, 1883)
if not client.connect():
    print ("Connected to broker: " + broker_addr)

client.set_callback(on_message)
client.subscribe("iotwalc/grupo04/LightIntensity/#")

print("Checking messages ...")

pycom.heartbeat(False)

while 1:
    client.check_msg()
