"""
Crie um programa que vai ler vários números e colocar em uma lista.
Crie duas listas extras que vão conter os valores pares e os valores ímpares, respectivamente.
Ao final, mostre o conteúdo das três listas geradas.
"""

lista_total = list()
lista_par = list()
lista_impar = list()

while True:
    x = int(input('Informe um valor: '))
    lista_total.append(x)
    if x % 2 == 0:
        lista_par.append(x)
    else:
        lista_impar.append(x)

    r = str(input('Você deseja adicionar mais valores[s/n]? ')).lower()
    while r not in 'sn':
        print('\033[31mOpção inválida. Tente novamente.\033[m')
        r = str(input('Você deseja adicionar mais valores[s/n]? '))
    print()
    if r in 'n':
        break

print(f'Lista Total = {lista_total}\nLista Par = {lista_par}\nLista Impar = {lista_impar}')

