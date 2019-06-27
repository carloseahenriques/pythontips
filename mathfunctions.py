# Algumas funções matemáticas com o módulo math nativo do Python
# Maiores detalhes podem ser obtidos no site do projeto:
# https://docs.python.org/3/library/math.html#constants

import math
import sys

# Retorna o interiro imediatamente superio a X
x=5.01
print (math.ceil(x))

# Converte radianos para graus
radian=3.141592
print (math.degrees(radian))

# Converte graus para radianos
degree=360
print (math.radians(degree))

# Retorna Pi o format e '.49g' define as casas decimais no máximo em até 49 casas decimais.
# 49 é o máximo que o Python consegue retornar
print (format(math.pi,'.49g'))

