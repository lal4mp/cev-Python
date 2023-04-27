"""
Faça um programa que tenha uma função chamada contador():
recebe três parâmetros: início, fim e passo.
Seu programa tem que realizar três contagens através da função criada:
a) de 1 até 10, de 1 em 1
b) de 10 até 0, de 2 em 2
c) uma contagem personalizada
"""
from time import sleep

def contador(inicio, fim, passo):
    print(' ' * 5, f'Contagem de {inicio} ate {fim} de {passo} em {passo}')

    if passo == 0:
        passo = 1
    if passo < 0:
        passo *= (-1)
    if inicio > fim:
        passo *= (-1)
        fim -= 2

    for x in range(inicio, fim+1, passo):
        sleep(0.2)
        print(x, end='  ')

    print('')
    print('-' * 42)

# Programa Principal
print('-' * 42)
contador(1, 10, 1)
contador(10, 0, 2)

print(' '*10, 'Contagem Personalizada')
i = int(input('Inicio:  '))
f = int(input('Fim: '))
p = int(input('Passo: '))
contador(i, f, p)
