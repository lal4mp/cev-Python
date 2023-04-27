"""
Faça um programa que tenha uma lista chamada números e duas funções:
sorteia() -> sorteia 5 números e vai os coloca dentro da lista
somaPar() -> mostra a soma entre os valores pares sorteados pela função sorteia().
"""
import random
from time import sleep

def sorteia(list):
    print('Sorteando os valores...', end=' ')
    for x in range(0, 5):
        n = random.randint(1, 10)
        list.append(n)
        print(n, end='  ')
        sleep(0.5)
    print(f'\nOs valores sorteados, então, foram {list}')

def somaPar(list):
    soma = 0
    for x in list:
        if x % 2 == 0:
            soma += x
    print(f'A soma dos valores pares sorteados é {soma}')


# Programa Principal
numeros = []
sorteia(numeros)
somaPar(numeros)
