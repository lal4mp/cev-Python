"""
Reescreva a função leiaInt() que fizemos no desafio 104.
Inclua agora a possibilidade da digitação de um número de tipo inválido.
Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.
"""


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


def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except(ValueError, TypeError):
            print('\033[31mERRO - digite um número real válido.\033[m\n')
        except(KeyboardInterrupt):
            print('\033[31mERRO - entrada de dados interrompida pelo usuario.\033[m\n')
            return 0
        else:
            return n


# programa principal
num1 = leiaInt('Digite um número inteiro: ')
num2 = leiaFloat('Digite um número real: ')
print(f'\nVocê digitou o número inteiro {num1}')
print(f'Você digitou o número real {num2}')
