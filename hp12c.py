# Juros compostos:
# Cálculo de FV

# Taxa em % no exemplo é 50%
i=50

# Número de períodos
n=1

print (100 * ((1+(i/100)) ** n))

# ===========================================

# Em matemática financeira usamos muito a potenciação e radicição
# para o cálculo de Juros compostos por isso é importante entender
# esse conceito
# Obtendo a raíz n de um número:
# Ex: raiz quadrada de 81
print (81 ** (1/2))

# Ex: Raíz 9 de 1953125
print (1953125 ** (1/9))

# Notem que tratam-se de operações inversas por isso o que fazemos é
# elevar um dado número pelo inverso da potência, ou seja "1 / expoente"

# Digamos que seu gerente lhe ofereceu um CDB com uma taxa efetiva anual de 6,4% ao ano
# E você quer saber qual a rentabilidade mensal desta taxa.
print (((1+(6.4/100)) ** (1/12) - 1) * 100)

# Onde 12 é o número de meses de 1 ano e 6.4% é a taxa anual efetiva
# Fica uma dica de um ex-operador do mercado: Feche sempre na maior anual independentemente do prazo!

# Agora vamos fazer a operação inversa:
# Você desta vez está na merda recorrendo ao cheque especial, e quer saber qual é a sua taxa
# efetiva anual.
# Digamos que aquela gerente fofa com o riso largo e aquela simpatia estampada do rosto
# Lhe ofereceu uma módica taxa de "apenas" 15% ao mês...
# Olhe o tamanho da lombriga efetiva anual!

print ((100 * ((1+(15/100)) ** 12) / 100 -1) * 100)

# Pretendo fazer mais um appends nesse arquivo portanto fiquem atentos!
