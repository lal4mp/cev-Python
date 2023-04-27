"""
Faça um programa que leia o ângulo.
Mostre seu seno, seu cosseno e sua tangente.
"""
import math
ang = float(input('Informe o ângulo: '))
sin = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print("""\nO ângulo de {} tem: 
seno = {:.2f}
cosseno = {:.2f}
tangente = {:.2f}""" .format(ang, sin, cos, tan))