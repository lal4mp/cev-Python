"""
Crie um programa que tenha uma função fatorial() que receba dois parâmetros:
o primeiro: indica o número a calcular
outro chamado show: um valor lógico (opcional) indicando se será mostrado ou não na tela o processo de cálculo do fatorial.
"""


def fatorial(num, show=False):
    """
    A função fatorial calcula o fatorial de um número.
    :param num: número cujo fatorial será calculado.
    :param show: opcional - mostra (True) ou não (False) a conta completa do fatorial.
    :return: retorna o valor do fatorial do número num.
    """
    facto = 1
    print(f'\nFatorial de {num} = ', end='')
    for x in range(num, 0, -1):
        if show:
            if x == 1:
                print(x, end=' = ')
            else:
                print(x, end=' x ')
        facto *= x
    return facto


# programa principal
n = int(input('Voce deseja calcular o fatorial de qual número? '))
while True:
    r = str(input('Voce deseja ver o processo de cálculo do fatorial [s/n]? ')).lower()
    if r in 'ns':
        break
    print('Opcao invalida. Digite apenas "s" ou "n".')
if r in 's':
    print(fatorial(n, True))
else:
    print(fatorial(n))

print()
help(fatorial)
