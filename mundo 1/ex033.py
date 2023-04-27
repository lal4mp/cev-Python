"""
Faça um programa que leia três números.
Mostre qual é o maior e qual é o menor.
"""
print('Digite 3 números: ')
n1 = float(input('Num 1 = '))
n2 = float(input('Num 2 = '))
n3 = float(input('Num 3 = '))

# maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n1:
    menor = n3

print('O maior número é o {} \nO menor número é o {}'.format(maior, menor))
