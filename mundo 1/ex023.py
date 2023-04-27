"""
Faça um programa que leia um número de 0 a 9999
Mostre na tela cada um dos dígitos separados.
"""
n = int(input('Informe um número entre 0 e 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000
print('unidade: {} \ndezena: {} \ncentena: {} \nmilhar: {}' .format(u, d, c, m))

