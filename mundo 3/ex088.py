"""
Faça um programa que ajude um jogador da MEGA SENA a criar palpites.
O programa vai perguntar quantos jogos serão gerados e vai sortear:
6 números entre 1 e 60 para cada jogo, cadastrando tudo em uma lista composta.
"""
import random
import time

print('-='*5, 'MEGA SENA', '=-'*5)
jogos_total = list()
jogo = list()
num_jogos = int(input('Quantos jogos voce quer fazer? '))

print(f'\n...Sorteando {num_jogos} jogos...\n')
for x in range(0, num_jogos):
    time.sleep(0.8)
    print(f'Jogo {x+1}: ', end='')
    for y in range(0, 6):
        jogo.append(random.randint(1, 60))
    jogo.sort()
    jogos_total.append(jogo[:])
    jogo.clear()
    print(jogos_total[x])
