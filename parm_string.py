
# Parâmetros posicionais em Python
# O equivalente aos $1, $2, $3, $n em
# shell script
#
#
# Exemplo: python3.6 parm_string.py "Essa é a string em questão"
# A Saída será:
#
# Essa é a string em questão É a string que passei
import sys
MinhaString=str(sys.argv[1])
print (MinhaString, "É a string que passei")
