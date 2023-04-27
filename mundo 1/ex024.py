"""
Crie um programa que leia o nome de uma cidade.
Diga se ela começa ou não com o nome “SANTO”.
"""
cidade = input('Informe o nome da sua cidade: ')
#print(cidade[:5].upper() == 'SANTO')
lista = cidade.upper().split()
print(lista[0] == 'SANTO')

