"""
Refaça o DESAFIO 51, lendo o primeiro termo e a razão de uma PA.
Mostre os 10 primeiros termos da progressão usando a estrutura while.
"""

print('    \033[1:35mPROGRESSÃO ARITMÉTICA\033[m')
a1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))

# modo 1
x = a1
a10 = a1 + 9*r
a11 = a1 + 10*r
while x != a11:
    print('\033[36m{}'.format(x), end='')
    print('\033[m -> ' if x != a10 else '', end='')
    x += r
print('')

# modo 2
x = a1
cont = 1
while cont <= 10:
    print('\033[36m{}'.format(x), end='')
    print('\033[m -> ' if cont < 10 else '', end='')
    x += r
    cont += 1

