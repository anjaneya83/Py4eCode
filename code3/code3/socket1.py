import socket

mysock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysock.connect(('data.pr4e.org', 80))
cmd = 'GET http://data.pr4e.org/romeo.txt HTTP/1.0\r\n\r\n'.encode()  # this is to convert data into utf8 format to be snet over the socket
mysock.send(cmd)

while True:
    data = mysock.recv(512)        #the data received is utf8  from the network, it needs to be converted into text for print using the decode method
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysock.close()
