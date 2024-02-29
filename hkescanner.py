import socket
import sys
from termcolor import colored,cprint
logo=colored('''
dP     dP  dP                .d88888b                                                        
88     88  88                88.    "'                                                       
88aaaaa88a 88  .dP  .d8888b. `Y88888b. .d8888b. .d8888b. 88d888b. 88d888b. .d8888b. 88d888b. 
88     88  88888"   88ooood8       `8b 88'  `"" 88'  `88 88'  `88 88'  `88 88ooood8 88'  `88 
88     88  88  `8b. 88.  ... d8'   .8P 88.  ... 88.  .88 88    88 88    88 88.  ... 88       
dP     dP  dP   `YP `88888P'  Y88888P  `88888P' `88888P8 dP    dP dP    dP `88888P' dP       
                                                                                             
                                                                                             
 ''','red')
print(logo)



ip_addr=input('enter the ip ')
ports=input('Enter the port(1/100,22,-p-) ')

open_ports=[]
if ports!='-p-':
  try:
     port_range=ports.split('/')
     port_min=int(port_range[0])
     port_max=int(port_range[1])
  except(ValueError,IndexError):
     port_min=int(ports)
     port_max=int(ports)
else:
    port_min=1
    port_max=65535
def scan_ports(ip_addr,ports):
   for port in range(port_min,port_max+1):
     with socket.socket(socket.AF_INET,socket.SOCK_STREAM)as s:
             s.settimeout(0.5)
             try:
               s.connect((ip_addr,port))
               open_ports.append(port)
             except(ConnectionRefusedError,TimeoutError):
               pass
 
   return open_ports
for p in  range(port_min,port_max+1): 
    scan_ports(ip_addr,p)

for i in open_ports:
    cprint(f"OPEN:{i}","yellow")
