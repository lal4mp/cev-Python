"""
Faça um programa que leia a largura e a altura de uma parede (em metros).
Calcule a sua área e a quantidade de tinta necessária para pintá-la.
Obs.: cada litro de tinta pinta uma área de 2m2.
"""
print('Informe a largura e altura da parede(em metros): ')
larg = float(input('Largura = '))
alt = float(input('Altura = '))
area = larg*alt
tinta = area/2
print('A área da parede é {}m². \nSão necessários {}L de tinta.' .format(area, tinta))