"""
Faça um programa que leia um ano qualquer.
Mostre se ele é bissexto.
"""
import datetime

year = int(input('Digite um ano (digite 0 para o ano atual): '))

if year == 0:
    year = datetime.date.today().year #pegar o ano atual

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print('O ano {} é bissexto' .format(year))
else:
    print('O ano {} não é bissexto' .format(year))