# -*- coding: utf-8 -*-
"""
    简单端口扫描程序
    SYN扫描

"""
import logging
import threading
logging.getLogger("scapy.runtime").setLevel(logging.ERROR)
from scapy.layers.inet import IP, TCP, UDP, ICMP
from scapy.all import *

#target = str(input("请输入目标IP: "))
target="127.0.0.1"
a=int(input("请输入扫描起始端口："))
b=int(input("请输入扫描终止端口："))
portslist=(list(range(a,b)))
'''
portslist=[21, 22, 34, 135, 139, 80, 445]
'''
def syn_scan(port):
    sport = RandShort()
    pkt = sr1(IP(dst=target) / TCP(sport=sport, dport=port, flags="S"), timeout=1, verbose=0)
    if pkt != None:
        if pkt.haslayer(TCP):
            if pkt[TCP].flags == 18:
                print(f"[+] Port {str(port)} Is Open\n")
    else:
        print(f"[+] Port {str(port)} Is Close\n")

def syn_scanner(target,portslist):
    print(f"Scanning {target} for Open TCP_SYN Ports\n")
    for x in portslist:
        threading.Thread(target=syn_scan,args=(x,)).start()

#syn_scanner(target,portslist)    
#print('Scan Is Completed!\n')
