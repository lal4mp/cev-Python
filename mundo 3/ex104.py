"""
Crie um programa que tenha a função leiaInt():
semelhante a função input(), mas só aceitando um valor numérico
"""


def leiaInt(msg):
    while True:
        n = str(input(msg))
        if n.isnumeric():
            num = int(n)
            break
        else:
            print('\033[31mERRO - digite um valor numérico\033[m\n')
    return num


# programa principal
num = leiaInt('Digite um número: ')
print(f'Você digitou o número {num}')