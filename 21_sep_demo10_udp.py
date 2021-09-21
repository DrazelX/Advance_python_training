# UDP client

import socket

msgfromclient = "hello udp server"

bytesTosend = str.encode(msgfromclient)

serverAddressPort = ('127.0.0.1', 20001)

buffersize = 1024

UDPCLIENTSOCKET=socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # 1st step

UDPCLIENTSOCKET.sendto(bytesTosend, serverAddressPort)  # 2nd step

msg = "message from server{}".format(msgfromclient[0])  # 3rd step

print(msg)