"""
Refaça o DESAFIO 9,
Mostre a tabuada de um número que o usuário escolher
*utilize um laço for.
"""
n = int(input('Você deseja ver a tabuada de qual número? '))
print('\n----- TABUADA DO {} -----' . format(n))

for x in range(0, 11):
    print('{} x {} = {}' .format(n, x, n*x))