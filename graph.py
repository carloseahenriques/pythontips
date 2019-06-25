# Módulo para plotagem de gráficos, exportação de imagem PNG e muiyo mais
# https://matplotlib.org/
#
# Para instalar o módulo:
# pip3 install matplotlib


import matplotlib.pyplot

meses_x = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'jul', 'ago', 'set', 'out', 'nov', 'dez']
valores_y = [105235.56, 107697.23, 110256.5, 1092.36, 108859, 109986, 8192, 123544, 42222, 12233, 10331, 1172355]
teste_y = [5, 7, 8, 9, 75, 2044, 544889]
matplotlib.pyplot.plot(meses_x, valores_y, teste_y); matplotlib.pyplot.show()
