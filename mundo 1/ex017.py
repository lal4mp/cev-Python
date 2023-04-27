"""
Faça um programa que leia o comprimento do cateto oposto e do cateto adjacente.
Calcule o comprimento da hipotenusa.
"""
import math
catop = float(input('Informe o comprimento do cateto oposto: '))
catad = float(input('Informe o comprimento do cateto adjacente: '))

#com a biblioteca math
hip = math.hypot(catop, catad)
print('O comprimento da hipotenusa é {:.2f}' . format(hip))

#sem a biblioteca
hip = (catop**2 + catad**2) ** (1/2)
print('O comprimento da hipotenusa é {:.2f}' . format(hip))