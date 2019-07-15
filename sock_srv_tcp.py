#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import socket

print ("Sockets em Python - TCP")

# A variável IPaddr se for deixada em branco
# o servidor escutará em todas as interfaces
# de rede do host

IPaddr = ''
servidor = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
servidor.bind((IPaddr, 12000))
# Define 10 conexões simultâneas de clientes
# e se não for declarada () é ilimitado
servidor.listen(10)

while True:
	conn, IPaddr = servidor.accept()
	#Define o tamanho do buffer em bytes
	data = conn.recv(2).decode("ascii")
	#data = conn.recv(1024)
	print(data)
	