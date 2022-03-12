#! /usr/bin/python3

from socket import *
import threading
import sys

def worker(sock,other_data):
	sock.listen(5)
	while True:
		data = sock.recv(1024).decode()
		sock.sendall(data.encode())
	sock.close()

def main():
	addr = ("0.0.0.0",sys.argv[2])
	sock.bind(addr)
	sock.listen(5)
	while True:
		(conn,addrs) = sock.accept()
		data = sock.recv(1024).decode()
		threading.Thread(target=worker, args=(sock,"abc_123")).start()
	sock.close()



