"""
Crie um programa que vai ler vários números e colocar em uma lista.
Depois disso, mostre:
A) Quantos números foram digitados.
B) A lista de valores, ordenada de forma decrescente.
C) Se o valor 5 foi digitado e está ou não na lista.
"""
lista = list()

count = 0
while True:
    lista.append(int(input('Informe um valor: ')))
    count += 1

    r = str(input('Você deseja adicionar mais valores[s/n]? ')).lower()
    while r not in 'sn':
        print('\033[31mOpção inválida. Tente novamente.\033[m')
        r = str(input('Você deseja adicionar mais valores[s/n]? '))
    print()
    if r in 'n':
        break

print(f'Você digitou {count} valores')
lista.sort(reverse=True)
print(f'Lista ordenada decrescentemente = {lista}')

if 5 in lista:
    print(f'O valor 5 está na lista, na posição {lista.index(5)}!')
else:
    print('O valor 5 não está na lista')