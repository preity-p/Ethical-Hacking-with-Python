import socket

s= socket.socket(socket.AF_INET, socket.SOCK_STREAM) # ipv4, tcp
s.settimeout(5) # ditch after timeout

ip= input("Please enter the IP address to be scanned: ")
port= int(input("Please enter the port to be scanned: "))

def portScanner(port):
    if s.connect_ex((ip, port)):
        print("The port is closed.")
    else:
        print("The port is open.")

portScanner(port)