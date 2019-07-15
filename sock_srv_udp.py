#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import socket

print ("Sockets em Python")
servidor = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
servidor.bind(('', 12000))

while True:
	msg_bytes, addrclient =  servidor.recvfrom(2048)
	msg_reponse = msg_bytes.decode()
	servidor.sendto(msg_reponse.encode(), addrclient)
	print (msg_reponse)
	