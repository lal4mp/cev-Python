"""
Crie um programa que leia a idade e o sexo de várias pessoas.
A cada pessoa cadastrada, pergunte se o usuário quer ou não continuar.
No final, mostre:
-Quantas pessoas tem mais de 18 anos.
-Quantos homens foram cadastrados.
-Quantas mulheres tem menos de 20 anos.
"""

count18 = 0
countHomens = 0
countMulheres20 = 0

while True:
    print('\t\t\tCADASTRO')
    idade = int(input('Qual sua idade? '))
    if idade > 18:
        count18 += 1

    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Qual seu sexo[M/F]? ')).upper()
    if sexo in 'M':
        countHomens += 1

    if sexo in 'F' and idade < 20:
        countMulheres20 += 1

    print('-'*30)
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Você deseja continuar[S/N]? ')).upper()
    print('-' * 30, '\n')
    if resp in 'N':
        break

print(f'Quantas pessoas tem mais de 18 anos? {count18}'
      f'\nQuantos homens foram cadastrados? {countHomens}'
      f'\nQuantas mulheres tem menos de 20 anos? {countMulheres20}')