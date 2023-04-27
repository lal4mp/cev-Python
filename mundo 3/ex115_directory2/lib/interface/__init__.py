def cabecalho(text):
    print()
    print('-='*10, f'\033[7m{text}\033[m', '=-'*10)


def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO - digite um número inteiro válido.\033[m\n')
        except(KeyboardInterrupt):
            print('\033[31mERRO - entrada de dados interrompida pelo usuario.\033[m\n')
            return 0
        else:
            return n


def menu(lista):
    cabecalho('MENU')
    for i, d in enumerate(lista):
        print(f'\033[35m[{i+1}] {d}\033[m')
    choice = leiaInt('O que você deseja realizar? ')
    return choice

