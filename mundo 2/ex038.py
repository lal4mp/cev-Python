"""
Escreva um programa que leia dois números inteiros e compare-os.
Mostrando na tela uma mensagem:
-O primeiro valor é maior
-O segundo valor é maior
-Não existe valor maior, os dois são iguais
"""
print('Digite dois números: ')
n1 = float(input('Number 1 = '))
n2 = float(input('Number 2 = '))

if n1 > n2:
    print('O primeiro valor é maior!')
elif n2 > n1:
    print('O segundo valor é maior!')
else:
    print('O dois valores são iguais!')