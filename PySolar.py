#!/usr/bin/env python3.6
# -*- coding: utf-8 -*

from pysolar.solar import *
import datetime

'''
O Pysolar é um módulo do Python para cálculo da posição do sol tomando como parâmetros
latitude, longitude, data e hora

Informações mais detalhes: http://pysolar.org/

As aplicações são inúmeras, destacando sistemas de orientação de painéis solares para maior eficiência.

'''

#Coordenadas em modo decimal.
coords=(-22.972018, -43.211024)
date=(datetime.datetime.now(pytz.timezone("America/Sao_Paulo")))
azmt=(get_azimuth(coords[0], coords[1], date))
altd=(get_altitude(coords[0], coords[1], date))
radn=(radiation.get_radiation_direct(date, get_altitude(coords[0], coords[1], date)))

print (date)
print ('Azimuth:', azmt, 'degrees')
print ('Altitude:', altd, 'degrees')
print ('Radiation', radn, 'W m²')
