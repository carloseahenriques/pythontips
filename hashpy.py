

import hashlib

Hashmd5sumDeUmaString = hashlib.md5()
Hashmd5sumDeUmaString.update("Minha String".encode('utf-8'))
print (Hashmd5sumDeUmaString.hexdigest())

Hashsha224sumDeUmaString = hashlib.sha224()
Hashsha224sumDeUmaString.update("Minha String2".encode('utf-8'))
print (Hashsha224sumDeUmaString.hexdigest())

Hashsha256sumDeUmaString = hashlib.sha256()
Hashsha256sumDeUmaString.update("Minha String3".encode('utf-8'))
print (Hashsha256sumDeUmaString.hexdigest())

Hashsharipemd160sumDeUmaString = hashlib.new('ripemd160')
Hashsharipemd160sumDeUmaString.update("Minha String 4".encode('utf-8'))
print (Hashsharipemd160sumDeUmaString.hexdigest())

#Printa todos os algoritimos disponíveis
print (hashlib.algorithms_available)

# Mais informações no site do projeto:
# https://docs.python.org/3/library/hashlib.html
