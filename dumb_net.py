#! /usr/bin/python3

from socket import *

import sys

sock = socket()

addr = (sys.argv[1],sys.argv[2])
sock.connect(addr)

message = input(" -> ")
message+= "\r\n"

sock.sendall(message.encode())
while True:
	data = sock.recv(1024).decode()
	print(data)
sock.close()




