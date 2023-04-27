"""
Crie um algoritmo que leia um número.
Mostre seu dobro, triplo e raiz quadrada.
"""
n = int(input('Informe um número: '))
print('Seu dobro é {}. \nSeu triplo é {}. \nSua raiz quadrada é {:.2f}.' . format(n*2, n*3, n**(1/2)))