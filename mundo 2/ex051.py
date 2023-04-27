"""
Faça um programa que leia o primeiro termo e a razão de uma PA.
No final, mostre os 10 primeiros termos dessa progressão.
"""
print('PROGRESSÃO ARITMÉTICA')
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

for x in range(0, 10):
    n = a1 + (x*r)
    print('{}' .format(n), end=' ')

"""
outra solução:
a10 = a1 + (10-1)*r
for x in range(a1, a10+r, r):
    print('{}'.format(x), end=' ')
"""
