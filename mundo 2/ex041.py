"""
A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta.
Mostre sua categoria, de acordo com a idade:
–Até 9 anos: MIRIM
–Até 14 anos: INFANTIL
–Até 19 anos: JÚNIOR
–Até 25 anos: SÊNIOR
–Acima de 25 anos: MASTER
"""
import datetime

nasc = int(input('Em qual ano você nasceu? '))
atual = datetime.date.today().year
idade = atual - nasc

print('Categoria:', end=' ')
if idade <= 9:
    print('MIRIM')
elif idade <= 14:
    print('INFANTIL')
elif idade <= 19:
    print('JUNIOR')
elif idade <= 25:
    print('SENIOR')
else:
    print('MASTER')