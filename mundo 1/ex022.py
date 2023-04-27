"""
Crie um programa que leia o nome completo de uma pessoa e mostre:
O nome com todas as letras maiúsculas e minúsculas.
Quantas letras ao todo (sem considerar espaços).
Quantas letras tem o primeiro nome.
"""
nome = str(input('Informe seu nome completo: ')).strip()

print('Seu nome em maiúsulas é {}' .format(nome.upper()))
print('Seu nome em minúsculas é {}' .format(nome.lower()))

tam = len(nome) - nome.count(' ')
print('Seu nome tem ao todo {} letras' .format(tam))

#print('Seu primeiro nome tem {} letras' .format(nome.find(' ')))
lista = nome.split()
print('Seu primeiro nome é {} e ele tem {} letras' .format(lista[0], len(lista[0])))

