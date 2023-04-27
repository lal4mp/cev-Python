"""
Faça um programa que leia 5 valores numéricos e guarde-os em uma lista.
Mostre qual foi o maior e o menor valor digitado e as suas respectivas posições.
"""
valores = list()
for x in range(0, 5):
    valores.append(int(input(f'Digite o valor da posição {x} da lista: ')))
print(f'\nLista = {valores}')

print(f'\nO maior valor digitado foi o {max(valores)} na(s) posição(ões) ', end='')
for p, e in enumerate(valores):
    if e == max(valores):
        print(f'{p} ', end='')

print(f'\nO menor valor digitado foi o {min(valores)} na(s) posição(ões) ', end='')
for p, e in enumerate(valores):
    if e == min(valores):
        print(f'{p} ', end='')

valores.sort()
print(f'\n\nLista ordenada = {valores}')
valores.sort(reverse = True)
print(f'Lista ordenada do maior para o menor = {valores}')