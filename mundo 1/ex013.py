"""
Faça um algoritmo que leia o salário de um funcionário.
Mostre o novo salário com 15% de aumento.
"""
s = float(input('Informe o salário: R$'))
ns = 1.15*s
print('O novo salário é R${:.2f}' . format(ns))