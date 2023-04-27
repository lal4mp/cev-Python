"""
Faça um programa que leia o ano de nascimento de um jovem.
Informe, de acordo com a sua idade, se:
-ele ainda vai se alistar ao serviço militar
-se é a hora exata de se alistar
-se já passou do tempo do alistamento
Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.
"""
from datetime import date

print('\033[34m='*5, 'ALISTAMENTO MILITAR', '='*5,)

ano_atual = date.today().year
nascimento = int(input('\033[mEm que ano voce nasceu? '))
idade = ano_atual - nascimento
alistamento = nascimento + 18
p = idade - 18
f = 18 - idade

if idade > 18:
    print('Seu alistamento foi em {}, há {} ano(s).' .format(alistamento, p))
elif idade == 18:
    print('Você deve se alistar!!')
else:
    print('Seu alistamento será em {}. Ainda faltam {} ano(s).' .format(alistamento, f))