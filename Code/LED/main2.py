import pycom
import time
pycom.heartbeat(False)

color = 0x7f0000
print("Color rojo: ",color)

color = 0x7f7f00
print("Color amarillo: ",color)

while (True):
    pycom.rgbled(color) # green
    time.sleep(0.5)
    #print("Color es: ",color)
    color = color - 64
    if (int(color) <= 8323072 ):
        color = 0x7f0000
        break
    
pycom.rgbled(color) # red
