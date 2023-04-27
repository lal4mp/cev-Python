"""
Crie um programa que leia um número real.
Mostre sua parte inteira.
"""
from math import trunc
num = float(input('Informe um número: '))

#com a biblioteca math
print('O número {} tem a parte inteira {}' .format(num, trunc(num)))

#sem a biblioteca
print('O número {} tem a parte inteira {}' .format(num, int(num)))
print('O número {} tem a parte inteira {:.2f}' .format(num, num))