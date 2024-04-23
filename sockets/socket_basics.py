#Basic of socket programming

import socket

sockfd = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sockfd.connect(('data.pr4e.org',80))
cmd = 'GET http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode() # this is to convert data into utf8 format to be snet over the socket
sockfd.send(cmd)
while True:
    data = sockfd.recv(512)
    if (len(data) < 1):
        break
    print(data.decode())              #the data received is utf8  from the network, it needs to be converted into text for print using the decode method
sockfd.close()