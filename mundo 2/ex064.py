"""
Crie um programa que leia vários números inteiros pelo teclado.
O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
No final, mostre quantos números foram digitados e qual foi a soma entre eles (desconsiderando o flag).
"""
n = soma = count = 0
n = int(input('Insira um número inteiro (999 para sair): '))
while n != 999:
    soma += n
    count += 1
    n = int(input('Insira um número inteiro (999 para sair): '))
print('\nQuantidade de números digitados: {} \nA soma entre os números digitados: {}' .format(count, soma))
