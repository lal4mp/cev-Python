"""
Aprimore o desafio anterior, mostrando no final:
A) A soma de todos os valores pares digitados.
B) A soma dos valores da terceira coluna.
C) O maior valor da segunda linha.
"""

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = soma_col3 = maior = 0

for lin in range(0, 3):
    for col in range(0, 3):
        n = int(input(f'Digite o elemento de [{lin}][{col}]: '))
        matriz[lin][col] = n

        if n % 2 == 0:
            soma_pares += n
        if col == 2:
            soma_col3 += n

for lin in range(0, 3):
    print()
    for col in range(0, 3):
        print(f'[{matriz[lin][col]:^5}]', end='')

print(f'\nA soma dos valores pares é {soma_pares}')
print(f'A soma dos valores da terceira coluna é {soma_col3}')
print(f'O maior valor da segunda linha é {max(matriz[1])}')


