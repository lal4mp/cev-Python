"""
Crie um programa que faça o computador jogar Jokenpô com você.
"""
import random
from time import sleep

print('\033[1:35m='*5, 'JOKENPÔ', '='*5)
print('\033[mVamos jogar!! \033[36m\nVocê = ciano \033[33m\nComputador = amarelo'
      '\n\n\033[mOpções: 1 - pedra'
      '\n\t\t2 - papel'
      '\n\t\t3 - tesoura')
jog = int(input('Escolha uma das opções: '))
comp = random.randint(1, 3)

if jog != 1 and jog != 2 and jog != 3:
    print('Opção inválida')
    exit()

print('\n\033[1:35mJO')
sleep(1)
print('KEN')
sleep(1)
print('PÔ\n\033[m')
sleep(1)

if jog == 1:
    print('\033[36mPedra', end='\033[m x ')
elif jog == 2:
    print('\033[36mPapel', end='\033[m x ')
elif jog == 3:
    print('\033[36mTesoura', end='\033[m x ')

if comp == 1:
    print('\033[33mPedra')
elif comp == 2:
    print('\033[33mPapel')
elif comp == 3:
    print('\033[33mTesoura')

if (jog == 1 and comp == 2) or (jog == 2 and comp == 3) or (jog == 3 and comp == 1):
    print('\033[1:31mVocê PERDEU :(')
elif jog == comp:
    print('\033[1:30mEMPATE')
else:
    print('\033[1:32mVocê GANHOU :)')

