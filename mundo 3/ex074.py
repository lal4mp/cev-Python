"""
Crie um programa que vai gerar cinco números aleatórios.
Coloque os em uma tupla. Depois disso, mostre a listagem de números gerados.
Indique o menor e o maior valor que estão na tupla.
"""
from random import randint
n1 = randint(1, 10)
n2 = randint(1, 10)
n3 = randint(1, 10)
n4 = randint(1, 10)
n5 = randint(1, 10)

tupla = (n1, n2, n3, n4, n5)

print(f'Tupla: {tupla}\n')

print(f'O menor valor é {min(tupla)} e o maior valor é {max(tupla)}')
