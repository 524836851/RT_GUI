#-*-coding:utf-8-*-

import time
import random
from sys import argv
from socket import *

if (len(argv)<2):
    print("usage:",argv[0],"port")
    exit(1)

port = int(argv[1])
server_sock = socket(AF_INET,SOCK_STREAM)
server_sock.bind(("localhost",port))
server_sock.listen(1)
t = 52667.0
x = -2170154.5575 
y = 4390713.7681    
z = 4072107.7859
cnt = 0
while True:
    print("Waiting connet...")
    connet_sock,client_ddr = server_sock.accept()
    print("Success connet from ",client_ddr)
    print("Sending Data...")
    try:
        while True:
            t += random.randint(1,2)
            x += random.uniform(-2.0,2.0)
            y += random.uniform(-2.0,2.0)
            z += random.uniform(-2.0,2.0)
            data = f" {t} {x} {y} {z} 0.0000     0.0000     0.0000    17  1.81    Fixed      11.00"
            connet_sock.sendall(data.encode())
            time.sleep(1)
    except ConnectionError as e:
        print("Send Error")