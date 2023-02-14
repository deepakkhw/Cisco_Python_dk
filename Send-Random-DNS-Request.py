# This file is generated to test the capacity of the internal DNS server and the upper and lower limits of the policies. 
# Its use on a public or unauthorized network is prohibited.
# The owner is not responsible or unware of any kind of legal issues.
# tested with Python version 3.10.6
import sys
from scapy.all import *

# Change top_level domain as ".com"
top_level = ".local"
# change domain name as "test".
domain = "xyz"
dmn = str(domain)
# number of DNS request, you wants to generate. 
cnt = 10000
# your internal DNS server
dns_server = "192.168.0.1"

for i in range(0, cnt):
    s = RandString(RandNum(1,8))
    ss = str(s)
    s1 = ss.lower()
    s2 = s1
    q = s2+"."+dmn+top_level


    print (1 ,q)
    sr1(IP(dst=dns_server)/UDP(sport=RandShort())/DNS(rd=1,qd=DNSQR(qname=q)))

