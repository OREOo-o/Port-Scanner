# -*- coding: utf-8 -*-
"""
    简单端口扫描程序
    UDP扫描

"""
from scapy.all import *
from scapy.layers.inet import IP, UDP 
import threading

target="127.0.0.1"
a=int(input("请输入扫描起始端口："))
b=int(input("请输入扫描终止端口："))
portslist=(list(range(a,b)))
'''
portslist=[21, 22, 34, 135, 139, 80, 445]
'''
def UDP_scan(target,port):
    pkt=IP(dst=target)/UDP(dport=int(port))
    res=sr1(pkt,timeout=0.1,verbose=0)
    if res==None:
         print(f"[+] Port {str(port)} Is Open\n")

def udp_scanner(target,portslist):
    print(f"Scanning {target} for Open UDP Ports\n")
    for port in portslist:
        t=threading.Thread(target=UDP_scan,args=(target,port))
        t.start()

if __name__=='__main__':
    udp_scanner(target,portslist)
