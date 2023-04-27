"""
Crie um programa onde o usuário possa digitar sete valores numéricos.
Cadastre-os em uma lista única que mantenha separados os valores pares e ímpares.
No final, mostre os valores pares e ímpares em ordem crescente.
"""
numbers = [[], []]

for x in range(1, 8):
    n = int(input(f'Digite o {x}° valor: '))
    if n % 2 == 0:
        numbers[0].append(n)
    else:
        numbers[1].append(n)

numbers[0].sort()
numbers[1].sort()
print(f'\nPares: {numbers[0]} \nImpares: {numbers[1]} \nNumbers: {numbers}')
