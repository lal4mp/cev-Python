"""
Crie um programa que leia nome, sexo e idade de várias pessoas.
Guarde os dados de cada pessoa em um dicionário e todos os dicionários em uma lista.
No final, mostre:
A) Quantas pessoas foram cadastradas
B) A média de idade
C) Uma lista com as mulheres
D) Uma lista de pessoas com idade acima da média
"""
grupo = list()
pessoa = dict()

count = soma = media = 0
while True:
    pessoa['Nome'] = str(input('Nome: ')).title()
    pessoa['Idade'] = int(input('Idade: '))
    while True:
        pessoa['Sexo'] = str(input('Sexo [m/f]: ')).upper().strip()
        if pessoa['Sexo'] in 'MF':
            break
        print('Opcao invalida. Digite apenas "f" ou "m".')

    grupo.append(pessoa.copy())
    # num de pessoas cadastradas
    count += 1

    # media das idades
    soma += pessoa['Idade']
    media = soma / count

    while True:
        r = str(input('Voce deseja adicionar mais pessoas [s/n]? ')).lower()
        if r in 'ns':
            break
        print('Opção inválida. Digite apenas "s" ou "n".')
    if r in 'n':
        break

    print()

print()
print('-='*40)
print(f'{count} pessoas foram cadastradas')
print(f'A media de idade das pessoas cadastradas e de {media:.2f} anos')

print('\nMulheres cadastradas: ')
for x in grupo:
    if x['Sexo'] in 'Ff':
        print(x['Nome'])

print('\nPessoas cadastradas com idade acima da média: ')
print('Nome', ' '*10, 'Idade', ' '*10, 'Sexo')
for y in range(0, len(grupo)):
    if grupo[y]['Idade'] > media:
        print(f'{grupo[y]["Nome"]:<16}{grupo[y]["Idade"]:<17}{grupo[y]["Sexo"]}')
print('-='*40)