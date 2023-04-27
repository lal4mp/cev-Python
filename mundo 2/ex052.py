"""
Faça um programa que leia um número inteiro.
Diga se ele é ou não um número primo.
"""
n = int(input('Digite um número: '))
count = 0

for x in range(1, n+1):
    if n % x == 0:
        print('\033[1:32m{}' .format(x), end=' ')
        count += 1
    else:
        print('\033[1:31m{}' .format(x), end=' ')

if count != 2:
    print('\033[m\nO número {} tem {} divisores. Ele NÃO é primo' .format(n , count))
else:
    print('\033[m\nO número {} tem apenas {} divisores, o 1 e ele mesmo. Ele É primo' .format(n , count))


'''
aux = 0
for x in range(2, n//2):
    if n % x == 0:
        aux = 1

if aux == 1:
    print('O número NÃO é primo')
else:
    print('O número É primo')
'''
