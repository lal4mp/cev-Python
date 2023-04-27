"""
Escreva um programa que faça o computador “pensar” em um número inteiro entre 0 e 5.
Peça para o usuário tentar descobrir qual foi o número escolhido pelo computador.
O programa deverá escrever na tela se o usuário venceu ou perdeu.
"""
import random
from time import sleep

print('----------Jogo Adivinha----------')
n = random.randint(0, 5)
num = int(input('Escolha um número inteiro entre 0 e 5: '))
print('Processando...')
sleep(3)
if num == n:
    print('\nVocê acertou!! Parabéns :)')
else:
    print('\nVoce errou :( ')
print('O número sorteado era o {}!' .format(n))
