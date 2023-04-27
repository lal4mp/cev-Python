"""
O mesmo professor quer sortear a ordem de apresentação dos 4 alunos.
Faça um programa que leia os nomes dos alunos e mostre a ordem sorteada.
"""
from random import shuffle
print('Informe o nome dos alunos: ')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
lista = [a1, a2, a3, a4]
shuffle(lista)
print('A ordem de apresentação é {}' .format(lista))