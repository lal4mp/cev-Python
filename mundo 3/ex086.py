"""
Crie um programa que declare uma matriz de dimensão 3×3.
Preencha com valores lidos pelo teclado.
No final, mostre a matriz na tela, com a formatação correta.
"""
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for lin in range(0, 3):
    for col in range(0, 3):
        matriz[lin][col] = int(input(f'Digite o elemento de [{lin}][{col}]: '))

# diferentes opções de print
# 1
for lin in range(0, 3):
    print('|', end='')
    for col in range(0, 3):
        if col == 2:
            print(matriz[lin][col], end='')
        else:
            print(matriz[lin][col], end='  ')
    print('|')

# 2
for lin in range(0, 3):
    print()
    for col in range(0, 3):
        print(f'[{matriz[lin][col]}]', end='')

# 3
print(f'\n\n{matriz[0]}\n{matriz[1]}\n{matriz[2]}')


