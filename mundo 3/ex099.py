"""
 Faça um programa que tenha uma função chamada maior():
 recebe vários parâmetros com valores inteiros.
 Seu programa tem que analisar todos os valores e dizer qual deles é o maior.
"""
from time import sleep

def maior(* numbers):
    # numbers é uma tupla que guarda os valores passados para a função
    if len(numbers) == 0:
        print('Nenhum valor informado')
        print('~' * 50)

    else:
        print('Analisando os valores...')
        sleep(0.5)
        max = count = 0

        for x in numbers:
            print(x, end='  ')
            sleep(0.2)
            if count == 0:
                max = x
            else:
                if x > max:
                    max = x
            count += 1

        print(f'\nForam informados {len(numbers)} valores')
        print(f'O maior valor é {max}')
        print('~'*50)


# Programa Principal
print('~'*50)
maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()

""" passando os valores por meio de uma lista 
def maior(list): 
    max = 0
    for i, v in enumerate(list):
        if i == 0:
            max = v
        else:
            if v > max:
                max = v
    print(f'O maior valor e {max}')


lista = []
count = 0
while True:
    count += 1
    print('Digite os valores que voce deseja comparar')
    n = int(input(f'Valor {count}: '))
    lista.append(n)

    while True:
        r = str(input('Voce deseja adicionar mais valores [s/n]? ')).lower()
        if r in 'ns':
            break
        print('Opcao invalida. Digite apenas "s" ou "n".')
    if r in 'n':
        break

maior(lista)
"""