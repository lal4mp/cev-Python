"""

"""
dados = list()
aux = []
pesados = list()
leves = list()
count = 0
maior = menor = 0

while True:
    aux.append(str(input('Nome: ')))
    aux.append(float(input('Peso: ')))
    dados.append(aux[:])
    aux.clear()

    for x in dados:
        if len(dados) == 1:
            maior = menor = x[1]
        else:
            if x[1] > maior:
                maior = x[1]
            elif x[1] < menor:
                menor = x[1]

    r = str(input('Voce deseja adicionar mais pessoas[s/n]? ')).lower()
    while r not in 'ns':
        print('Opcao invalida. Digite apenas "s" ou "n".')
        r = str(input('Voce deseja adicionar mais pessoas? ')).lower()
    print('')
    if r in 'n':
        break

print(f'Foram cadastradas {len(dados)} pessoas: {dados}')

print(f'O mais leves sao ', end='')
for x in dados:
    if x[1] == menor:
        print(f'{x[0]} ', end='')
print(f', com {menor}kg')


print(f'O mais pesados sao ', end='')
for x in dados:
    if x[1] == maior:
        print(f'{x[0]} ', end='')
print(f', com {maior}kg')



