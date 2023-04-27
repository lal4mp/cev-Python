"""
Faça um programa que leia o nome completo de uma pessoa.
Mostre o primeiro e o último nome separadamente.
"""
nome = str(input('Informe seu nome completo: ')).strip().title()
list = nome.split()
print('Seu primeiro nome é {}' .format(list[0]))
print('Seu primeiro nome é {}' .format(list[len(list)-1]))

