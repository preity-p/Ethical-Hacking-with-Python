import socket

serversocket= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # family= ipv4, type= tcp

host= socket.gethostbyname() # IP address of server
port= 444 # change as required

serversocket.bind((host, port)) # can be hardcoded if required
serversocket.listen(3) # listens to upto 3 connections at a time

while True:
    clientsocket, address= serversocket.accept()

    print("Connection received from %s " %str(address))
    message= 'Thank you for connecting.'
    clientsocket.send(message.encode('ascii'))
    
    clientsocket.close()