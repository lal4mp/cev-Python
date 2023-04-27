"""
Crie um programa que leia o nome e o preço de vários produtos.
O programa deverá perguntar se o usuário vai continuar ou não.
No final, mostre:
A)qual é o total gasto na compra.
B)quantos produtos custam mais de R$1000.
C)qual é o nome do produto mais barato.
"""

count = total = count1000 = precoBarato = 0
nomeBarato = ' '

while True:
    nome = str(input('Qual o nome do produto? '))
    preco = float(input('Qual o preco do produto? R$'))

    count += 1
    total += preco

    if preco > 1000:
        count1000 += 1

    if count == 1:
        nomeBarato = nome
        precoBarato = preco
    if preco < precoBarato:
        nomeBarato = nome
        precoBarato = preco

    print('-'*30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar[S/N]? ')).upper()
    print('-' * 30, '\n')
    if resp in 'N':
        break

print(f'O total gasto com a compra de {count} produtos foi R${total:.2f}'
      f'\n{count1000} produto(s) custou(ram) mais de R$1000.00'
      f'\nO produto mais barato foi o {nomeBarato} de R${precoBarato:.2f}')
