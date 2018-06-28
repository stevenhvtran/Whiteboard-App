import socket
import time
TCP_IP = '127.0.0.1'
TCP_PORT = 49152
BUFFER_SIZE = 20

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  # INET is IPv4 protocol and SOCK_STREAM is for TCP usage
s.bind((TCP_IP, TCP_PORT))
s.listen(1)  # Waits until a client connects

(conn_obj, address) = s.accept()   # conn_obj is the connected client as an object
print('The connecting address is %s and the port is %s: ' % (address[0], address[1]))
while True:
    data = conn_obj.recv(BUFFER_SIZE).decode()
    if not data:
        break
    print('The chunk of data received was: ' + str(data))
    conn_obj.send(data.encode())

time.sleep(5)
conn_obj(send(b'hi'))
conn_obj.close()
