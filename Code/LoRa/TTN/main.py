from network import LoRa
import binascii
import struct

lora = LoRa(mode=LoRa.LORAWAN)

dev_addr = struct.unpack(">l", binascii.unhexlify('26021731'))[0]
nwk_swkey = binascii.unhexlify('CE35CFAC2841D160F067868F7FB4F11A')
app_swkey = binascii.unhexlify('A09040B3228F7477BCAD4F2D3718DD58')

lora.join(activation=LoRa.ABP, auth=(dev_addr, nwk_swkey, app_swkey))

import socket
import time

while True:
    time.sleep(15)                      # wait 15 seconds
    s = socket.socket(socket.AF_LORA, socket.SOCK_RAW)
    #SO_DR (datarate) 5 is only available in LoRa 868Mhz (EU868). Are you in a different region? For US915 it should be 3.
    s.setsockopt(socket.SOL_LORA, socket.SO_DR, 3)

    s.setblocking(False)
    s.send(bytes([1, 2, 3]))
    s.settimeout(5.0) # configure a timeout value of 3 seconds
    try:
       rx_pkt = s.recv(64)   # get the packet received (if any)
       print(rx_pkt)
    except socket.timeout:
      print('Waiting to send new packet')
