"""
Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
No final do programa, mostre:
-a média de idade do grupo
-qual é o nome do homem mais velho
-quantas mulheres têm menos de 20 anos
"""
soma = 0
maior = 0
velho = ''
quant = 0
for x in range(1, 5):
    print('\n-----Pessoa {}-----'.format(x))
    nome = str(input('Nome = ')).strip()
    idade = int(input('Idade = '))
    sexo = str(input('Sexo(M ou F) = ')).strip()

    #media
    soma += idade

    #o homem mais velho
    if sexo in 'Mm' and idade > maior:
        velho = nome
        maior = idade

    #mulheres com menos de 20 anos
    if sexo in 'Ff' and idade < 20:
        quant += 1

media = soma/4
print('\n\nA média de idade do grupo é {:.2f}' .format(media))
print('O homem mais velho é o', velho)
print('Têm {} mulhere(s) com menos de 20 anos' .format(quant))