import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM)

host= socket.gethostbyname()
port= 444 # change as required

s.connect((host, port))

message= s.recv(1024) # max amount of data that can be received

s.close()

print(message.decode('ascii'))