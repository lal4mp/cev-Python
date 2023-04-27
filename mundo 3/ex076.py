"""
Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços, na sequência.
No final, mostre uma listagem de preços, organizando os dados em forma tabular.
"""

tupla = ('Lapis', 1.75,
         'Caneta', 2.60,
         'Borracha', 3,
         'Caderno', 15.9,
         'Livro', 32.90,
         'Estojo', 25,
         'Mochila', 120.50)

print('  \033[7mTABELA DE PREÇOS\033[m')
for p, x in enumerate(tupla):
    if p % 2 == 0:
        print(f'{x:<12}', end='')
    else:
        print(f'R${x:.2f}')