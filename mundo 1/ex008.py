"""
Escreva um programa que leia um valor em metros.
Exiba esse valor convertido em centímetros e em milímetros.
"""
n = float(input('Informe um valor em metros: '))
cm = n*100
mm = n*1000
print('\nEm centímetros = {}cm \nEm milímetros = {}mm' .format(cm, mm))