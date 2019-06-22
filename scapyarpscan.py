from scapy.all import *
import optparse
from threading import *
def send_rec(packet):
    try:
        reply=srp1(packet,timeout=1,verbose=0,iface='eth0')
        print("Word1:\"IP_@\"->Word2:\"MAC_ls\":"+reply.psrc+"->"+reply.hwsrc)
    except:
        pass
def structure():
    eth=Ether()
    eth.dst="ff:ff:ff:ff:ff:ff"
    eth.type=0x806
    arp=ARP()
    packet=eth/arp
    return packet
def opparse():
    parser=optparse.OptionParser("usage%prog"+"-H<target host segment/eg:(192.168.1.)>")
    parser.add_option("-H",dest="tgthost",type="string",help="specify target")
    return parser
def forscan(packet,host):
    for n in range(1,254):
        #packet[ARP].pdst=host+str(n)
	packet[ARP].pdst='10.10.10.108'
        send_rec(packet)
def main():
    parser=opparse()
    (options,args)=parser.parse_args()
    host=options.tgthost
    if host==None:
        print(parser.usage)
        exit(0)
    packet=structure()
    forscan(packet,host)
if __name__=="__main__":
    main()
