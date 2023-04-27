"""
Escreva um programa que leia um número N inteiro qualquer.
Mostre na tela os N primeiros elementos de uma Sequência de Fibonacci.
"""

print('    \033[1:35mSEQUÊNCIA FIBONACCI\033[m')
n = int(input('Quantos números da sequência você deseja visualizar? '))

t1 = 0
t2 = 1
print('{} {} ' .format(t1, t2), end='')
count = 3
while count <= n:
    t3 = t1 + t2
    print('{} ' .format(t3), end='')
    t1 = t2
    t2 = t3
    count += 1