"""
Crie um programa onde 4 jogadores joguem um dado e tenham resultados aleatórios.
Guarde esses resultados em um dicionário em Python.
Coloque esse dicionário em ordem - o vencedor tirou o maior número no dado.
"""
from random import randint
from time import sleep
from operator import itemgetter

jog = dict()
for x in range(0, 4):
    jog[f'jogador {x+1}'] = randint(1, 6)

print('Jogando...')
for k, v in jog.items():
    sleep(1)
    print(f'O {k} tirou {v}')

print('\nRanking:')
# modo 1
sleep(1)
ranking = sorted(jog.items(), key=itemgetter(1), reverse=True)  # ranking = list()
print(ranking)
for i, y in enumerate(ranking):
    print(f'\t{i+1}° lugar: {y[0]} com {y[1]}')

# modo 2
print()
count = 1
for i in sorted(jog, key=jog.get, reverse=True):
    print(f'\t{count}° lugar: ', end='')
    count += 1
    print(f'{i} com {jog[i]}')
