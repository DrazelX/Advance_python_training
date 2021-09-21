# UDP Program
# UDP Server
import socket
localIP = '127.0.0.1'
localport = 20001

bufferSize = 1024

msgFromServer = "Hello UDP Client"

bytesToSend = str.encode(msgFromServer)

UDPSERVERSOCKET = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)  # 1st step

UDPSERVERSOCKET.bind((localIP, localport))  # 2nd step

print("UDP server up and listening...")

while True:
    bytesAddressPair = UDPSERVERSOCKET.recvfrom(bufferSize)  # 3rd step
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]

    clientmsg = "Message from client{}".format(message)
    clientIP = "Client IP address:{}".format(address)
    print(clientmsg)
    print(clientIP)
    UDPSERVERSOCKET.sendto(bytesToSend, address)  # 4th step
