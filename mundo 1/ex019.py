"""
Um professor quer sortear um dos seus 4 alunos para apagar o quadro.
Faça um programa que leia o nome dos alunos e retorne o nome do escolhido
"""
import random
print('Informe o nome dos alunos: ')
a1 = input('Aluno 1: ')
a2 = input('Aluno 2: ')
a3 = input('Aluno 3: ')
a4 = input('Aluno 4: ')
e = random.choice([a1, a2, a3, a4])
print('O aluno escolhido foi {}!!!' .format(e))

