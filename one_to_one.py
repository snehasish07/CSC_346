#! /usr/bin/python3

from socket import *

import sys




def server_program(port):

	sock = socket()

	addr = ("0.0.0.0",PORT)
	sock.bind(addr)

	sock.listen(5)
	while True:
		(conn,addrs) =  sock.accept()
		data = conn.recv(1024).decode()
		if not data:
			break
		print(str(data))
		data = input(' -> ')
		conn.sendall(data.encode())

	conn.close()

def client_program(host,port):
	csock = socket()
	csock.connect((host,port))

	message = input(" -> ")
	while message.lower().strip() != ' ':
 	       csock.sendal(message.encode())
               data = csock.recv(1024).decode()
	       if not data:
			break
	       print(str(data))
	       message = input(' -> ')
	       csock.sendall(message.encode())

	csock.close()









if __name__ == '__main__':
	if sys.argv[1] == "server":
		server_program(sys.argv[2])
	else:
		client_program(sys.argv[1],sys.argv[2]) 



