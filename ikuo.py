import socket

def ikuoGetPrint():
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect(('mizuuchi.lab.tuat.ac.jp', 80))
	s.sendall(b'GET /~ikuo/ /HTTP/1.1\n')
	data = s.recv(1024)
	print(repr(data))
