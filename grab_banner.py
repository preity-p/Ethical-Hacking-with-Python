import socket

s= socket.socket()

def banner(ip, port):
    s.connect((ip, port))
    print(s.recv(1024)) # limting the amount of data that can be printed

def main():
    ip= str(input("Please enter the target IP address: "))
    port= int(input("Please enter the target port: "))
    banner(ip, port)

main()