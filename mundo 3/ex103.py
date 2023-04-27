"""
Faça um programa que tenha uma função chamada ficha():
recebe dois parâmetros opcionais:
o nome de um jogador e quantos gols ele marcou.
O programa deverá ser capaz de mostrar a ficha do jogador, mesmo que algum dado não tenha sido informado corretamente.
"""


def ficha(nome='<desconhecido>', gols=0):
    print(f'\nO jogador {nome} marcou {gols} gol(s).')


# programa principal
n = str(input('Nome do jogador: ')).title()
g = str(input(f'Número de gols marcados por {n}: '))

if g.isnumeric():
    g = int(g)
else:
    g = 0

if n.strip() == '':
    ficha(gols=g)
else:
    ficha(n, g)
