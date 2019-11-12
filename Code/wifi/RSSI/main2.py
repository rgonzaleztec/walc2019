import time
import pycom
import machine
from network import WLAN
wlan = WLAN(mode=WLAN.STA)

#nets = wlan.scan()
#print(nets)
pycom.heartbeat(False)

while True:
    nets = wlan.scan()
    for net in nets:
        if ((net.rssi >= int(-50)) and (net.ssid =="WALC19")):
                print(net.ssid, net.rssi, 1)
                pycom.rgbled(0x007f00) #green
                time.sleep(0.5)
        elif ((net.rssi < int(-50)) and (net.rssi >= int(-60))) and (net.ssid =="WALC19"):
                print(net.ssid, net.rssi, 2)
                pycom.rgbled(0x0000FF) # blue
                time.sleep(0.5)
        elif ((net.rssi < int(-60)) and (net.rssi >= int(-70))) and (net.ssid =="WALC19"):
                print(net.ssid, net.rssi, 3)
                pycom.rgbled(0xE7d40A) # blue
                time.sleep(0.5)
        elif (net.rssi < int(-70)) and (net.ssid =="WALC19"):
                print(net.ssid, net.rssi, 4)
                pycom.rgbled(0xff0000) # blue
                time.sleep(0.5)
