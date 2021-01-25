import socket

server_s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # family= ipv4, type= tcp

host= socket.gethostbyname() # IP address of server
port= 444 # change as required

server_s.bind((host, port)) # can be hardcoded if required
server_s.listen(3) # listens to upto 3 connections at a time

while True:
    client_s, address= server_s.accept()

    print("Connection received from %s " %str(address))
    message= 'Connected successfully.'
    client_s.send(message.encode('ascii'))
    
    client_s.close()