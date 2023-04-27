"""
Crie um programa que leia vários números inteiros pelo teclado.
No final da execução, mostre a média entre todos os valores e qual foi o maior e o menor valores lidos.
O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
"""
n = soma = count = maior = menor = 0
r = 'S'

while r in 'S':
    n = int(input('Insira um número inteiro: '))
    count += 1

    soma += n
    if count == 1:
        maior = menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n

    r = str(input('Você deseja digitar mais valores [S/N] ? ')).upper().strip()
    while r not in 'NS':
        print('\033[31mOpção inválida. Tente novamente.\033[m')
        r = str(input('Você deseja digitar mais valores [S/N] ? ')).upper().strip()

media = soma/count
print('\n\033[1;30mA média entre os valores digitados é {} \nO maior valor é o {} e o menor valor é o {}' .format(media, maior, menor))