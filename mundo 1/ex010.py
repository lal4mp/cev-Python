"""
Crie um programa que leia quantos reais uma pessoa possui.
Mostre quantos doláres ela pode comprar.
"""
r = float(input('Informe quantos reais você possui: R$'))
dolar = r/5.31
print('É possível comprar US${:.2f}' .format(dolar))