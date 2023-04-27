"""
Crie um programa onde o usuário possa digitar vários valores.
Cadastre-os em uma lista. Caso o número já exista lá dentro, não o adicione.
No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
"""
lista = list()

while True:
    x = int(input('Informe um valor: '))
    if x not in lista:
        lista.append(x)
        print('\033[32mValor adicionado com sucesso!\033[m')
    else:
        print('\033[31mValor duplicado. Não adicionado!\033[m')

    r = str(input('Você deseja adicionar mais valores[s/n]? ')).lower()
    while r not in 'sn':
        print('\033[31mOpção inválida. Tente novamente.\033[m')
        r = str(input('Você deseja adicionar mais valores[s/n]? '))
    print()
    if r in 'n':
        break

print(f'Lista = {lista}')
lista.sort()
print(f'Lista em ordem crescente = {lista}')