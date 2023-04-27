"""
Faça um programa que jogue par ou ímpar com o computador.
O jogo só será interrompido quando o jogador perder.
Mostre o total de vitórias consecutivas que ele conquistou no final do jogo.
"""
import random

print('\033[35m-------PAR OU ÍMPAR-------\033[m')

count = 0
while True:
    choice = ' '
    while choice not in 'PI':
        choice = str(input('Par ou Ímpar[P/I]? ')).upper()

    jog = int(input('Jogue um valor(0 a 10): '))
    comp = random.randint(0, 10)

    total = jog + comp
    if total % 2 == 0:
        resp = 'P'
    else:
        resp = 'I'
    print(f'\nVocê jogou {jog} e o computador {comp} = {total} -> {resp}')

    if choice != resp:
        break
    if choice == resp:
        print(f'\033[1;32mVocê ganhou!!!\n\033[mVamos jogar novamente...\n')
        count += 1

print(f'\033[1;31mVocê perdeu dessa vez :(\033[1;36m\nVitórias consecutivas = {count}')