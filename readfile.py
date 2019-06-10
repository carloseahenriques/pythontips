

fileopened = open("mac_ip.conf", "r", encoding="utf-8")

#lista = fileopened.readlines()
#print (lista)

listaSemQuebraDeLinhas = fileopened.read().splitlines()
print (listaSemQuebraDeLinhas)
