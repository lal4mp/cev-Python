"""
Faça um algoritmo que leia o preço de um produto.
Mostre seu novo preço com 5% de desconto.
"""
p = float(input('Informe o preço do produto: R$'))
np = 0.95*p
print('O novo preço é R${:.2f}' .format(np))