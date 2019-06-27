# Juros compostos:
# Cálculo de FV
# Taxa em % no exemplo é 50%
i=50

# Número de períodos
n=1

# Valor final
FV=150
print (100 * ((1+(i/100)) ** n))

# Cálculo do PV (valor presente)
print (FV / (1+(50/100)) ** 1)

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

print ((100 * ((1+(8/100)) ** 12) / 100 -1) * 100)

# Pretendo fazer mais um appends nesse arquivo portanto fiquem atentos!

# ===========================================

# Série de pagamentos uniforme mais conhecido como carnê no mei tempo e atualmente como boleto. É o método
# Para calcular valores relativos a financiamentos, prestações etc. Neste exemplo estamos tratando da 
# série postecipada que nas calculadoras financeiras são conhecidas como BGN/END (Begin e End)
# Digamos que você resolve comprar um carro velho para passear com a família fim de semana ou rodar
# no Uber, 99 e coisas do gênero em virtude de estar desempregado. A fubica custa R$ 15.000,00 a vista
# a taxa é de 2% ao mês, e você vai financia-lo sem entrada em 24 meses. Qual o valor da prestação?

print ((1 + (2/100)) ** 24 * (2/100) / ((1 + (2/100)) ** 24 - 1) * 15000)

# Agora vamos fazer a operação inversa, ou seja Dada a taxa de juros, o prazo e o valor da prestação você quer saber
# qual é o valor financiado.

print (793.06 / ((1+(2/100)) ** 24 * (2/100) / ((1+(2/100)) ** 24 - 1)))

# Para a mesma operação acima agora queremos calcular o número de períodos dadas a taxa de juros de 2% ao mês
# o valor financiado de R$ 15.000,00 e a prestação de 793.06. Nesse caso usaremos o módulo math do Python
# para calcular-mos o ln (logarítimo natural)

def periods():
    import math
    print (math.log(1 - ((15000/793.06) * (2/100))) / math.log(1 + (2/100)) * -1)

periods()

# Notem que importei o módulo math "por dentro da função" periods alguns acham isso gambiarra,
# mas tem muitas utilidades dependendo do que estiver-mos implementando. Fica a caráter de ilustração.


# Para o caso de tratar-se de uma série de pagamentos antecipada o cálculo é o mesmo bastando para isso deduzir
# o valor da entrada do valor financiado que no caso é R$ 15.000,00 e diminuir em 1 o prazo de financiamento
# ou seja 23 meses.

# Agora vamos dar outro exemplo, você quer comprar uma moto velha para ir trabalhar visto que o transporte
# público é uma merda mas você só pode arcar com uma prestação de no máximo R$ 500,00 por mês e você deseja
# saber qual a taxa que você ira pagar.

