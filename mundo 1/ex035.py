"""
Desenvolva um programa que leia o comprimento de três retas.
Diga ao usuário se elas podem ou não formar um triângulo.
"""
print('Digite o comprimentos das retas: ')
r1 = float(input('Reta 1 = '))
r2 = float(input('Reta 2 = '))
r3 = float(input('Reta 3 = '))

if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print('Essa retas podem formar um triângulo')
else:
    print('Essa retas não podem formar um triângulo')