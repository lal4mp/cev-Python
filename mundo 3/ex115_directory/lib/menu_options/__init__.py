def cadastramento():
    lista = list()
    pessoa = dict()

    count = 0
    while True:
        count += 1
        print(f'\033[36mPessoa {count}\033[m')
        pessoa['Nome'] = str(input('Nome: ')).title()
        pessoa['Idade'] = int(input('Idade: '))

        lista.append(pessoa.copy())

        while True:
            r = str(input('Voce deseja cadastrar mais pessoas [s/n]? ')).lower()
            if r in 'ns':
                break
            print('Opção inválida. Digite apenas "s" ou "n".')
        if r in 'n':
            break
        print()
    return lista


def listar(lista):
    print('\033[36mNome', ' ' * 10, 'Idade\033[30m')
    for y in range(0, len(lista)):
        print(f'{lista[y]["Nome"]:<16}{lista[y]["Idade"]}')
    print('\033[m')
