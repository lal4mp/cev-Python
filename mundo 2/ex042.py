"""
Refaça o DESAFIO 35 dos triângulos:
Acrescente o recurso de mostrar que tipo de triângulo será formado:
-EQUILÁTERO: todos os lados iguais
-ISÓSCELES: dois lados iguais, um diferente
-ESCALENO: todos os lados diferentes
"""

print('Digite o comprimentos das retas: ')
r1 = float(input('Reta 1 = '))
r2 = float(input('Reta 2 = '))
r3 = float(input('Reta 3 = '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    if r1 == r2 == r3:
        print('\033[32mEssas retas formam um \033[1:32mtriângulo equilátero')
    elif r1 != r2 != r3 != r1:
        print('\033[32mEssas retas formam um \033[1:32mtriângulo escaleno')
    else:
        print('\033[32mEssas retas formam um \033[1:32mtriângulo isósceles')
else:
    print('\033[31mEssa retas não formam um triângulo')