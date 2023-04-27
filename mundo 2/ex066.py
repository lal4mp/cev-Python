"""
Crie um programa que leia números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999.
Mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).
"""
n = soma = count = 0
while True:
    n = int(input('Insira um número inteiro (999 para sair): '))
    if n == 999:
        break
    count += 1
    soma += n
print('\nQuantidade de números digitados: {} \nA soma entre os números digitados: {}' .format(count, soma))
