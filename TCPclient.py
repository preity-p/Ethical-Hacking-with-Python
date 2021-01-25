import socket

clientsocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= socket.gethostbyname()
port= 444 # change as required

clientsocket.connect((host, port))

message= clientsocket.recv(1024) # max amount of data that can be received

clientsocket.close()

print(message.decode('ascii'))