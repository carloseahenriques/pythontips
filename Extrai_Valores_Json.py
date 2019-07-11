
import json
import time

# Abre o arquivo .json em modo "r"ead only (somente leitura)
fp = open("/root/OCR/openalpr.json", "r")

# Declara o json como a variável "obj"
obj = json.load(fp)

# Fecha o arquivo json
fp.close()

# Extrai valores pré determinados do arquivo json e os armazena em variáveis
Placa=obj["results"][0]["plate"]
TimeStamp=obj["epoch_time"]/1000
Cor=obj["results"][0]["vehicle"]["color"][0]["name"]
Modelo=obj["results"][0]["vehicle"]["make_model"][0]["name"]
DateTime=(time.gmtime(TimeStamp))

#Retorna o tipo da variável no caso trata-se de um dicionário
print (type(obj))

# Imprime as variáveis armazenadas
print (Cor)
print (Modelo)
print (Placa)
print (time.strftime('%Y%m%d%H%M%S', DateTime))
