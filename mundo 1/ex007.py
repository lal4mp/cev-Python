"""
Desenvolva um programa que leia duas notas de um aluno.
Calcule e mostre a média entre as notas.
"""
print('Informe sua notas: ')
n1 = float(input('Nota 1 = '))
n2 = float(input('Nota 2 = '))
m = (n1+n2)/2
print('A média entre as notas é {:.1f}' .format(m))