"""
Desenvolva um programa que leia quatro valores pelo teclado.
Guarde-os em uma tupla. No final, mostre:
A) Quantas vezes apareceu o valor 9.
B) Em que posição foi digitado o primeiro valor 3.
C) Quais foram os números pares.
"""

print('Informe 4 valores: ')
valores = (int(input('Valor 1: ')),
           int(input('Valor 2: ')),
           int(input('Valor 3: ')),
           int(input('Valor 4: ')))
print(f'Você digitou os valores {valores}')

print(f'\nO valor 9 apareceu {valores.count(9)} vezes')

if 3 in valores:
    print(f'\nO valor 3 foi digitado pela primeira vez na {valores.index(3) + 1}ª posição')
else:
    print('O valor 3 não foi digitado')

print('\nOs números pares digitados foram: ', end='')
countpar = 0
for x in valores:
    if x % 2 == 0:
        print(x, end=' ')
        countpar += 1
print(f'-> {countpar} número(s) par(es) no total')




