import socket
import time

TCP_IP = '127.0.0.1'
TCP_PORT = 49152
BUFFER_SIZE = 1024
SERVER_BUFFER_SIZE = 20
message = 'Hello THIS IS A VERY LONG MESSAGE THAT SHOULD BE LONGER THAN THE SERVER BUFFER LIMIT'

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is IPv4 protocol and SOCK_STREAM is for TCP usage
s.connect((TCP_IP, TCP_PORT))
s.send(message.encode())  # Sends the message encoded as a bytes object to the server

messageList = []  # Holds the information
while True:
    buf = s.recv(BUFFER_SIZE)
    if len(buf) < SERVER_BUFFER_SIZE:
        messageList.append(buf.decode())
        break
    else:
        messageList.append(buf.decode())

print(''.join(messageList))
s.close()

