"""
Faça um programa que tenha uma função chamada área():
recebe as dimensões de um terreno retangular (largura e comprimento).
Mostre a área do terreno.
"""

def area(larg, comp):
    print(f'\nA área do terreno {larg:.2f} x {comp:.2f} é de {larg*comp:.2f}m2.')

# Programa Principal
print(' '*5, 'Dimensões do Terreno')
l = float(input('Largura (m): '))
c = float(input(('Comprimento (m): ')))
area(l, c)