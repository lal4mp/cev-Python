"""
Crie um programa que leia dois valores e mostre um menu na tela:
[ 1 ] somar
[ 2 ] multiplicar
[ 3 ] maior
[ 4 ] novos números
[ 5 ] sair do programa
"""
n1 = float(input('Digite dois valores: Valor 1 = '))
n2 = float(input('\t\t\t\t\t Valor 2 = '))
o = 0
print('\n\033[1:36mMENU: [1] soma')
print(' ' * 5, '[2] multiplicação')
print(' ' * 5, '[3] comparação(maior/menor)')
print(' ' * 5, '[4] digitar novos valores')
print(' ' * 5, '[5] sair do programa\033[m')

while o != 5:
    o = int(input('O que você deseja realizar? '))
    if o == 1:
        print('{} + {} = {}'.format(n1, n2, n1 + n2))
    elif o == 2:
        print('{} x {} = {}'.format(n1, n2, n1 * n2))
    elif o == 3:
        if n1 > n2:
            print('O valor 1 = {} é maior que o valor 2 = {}'.format(n1, n2))
        elif n1 < n2:
            print('O valor 2 = {} é maior que o valor 1 = {}'.format(n2, n1))
        else:
            print('O valor 1 = {} e valor 2 = {} são iguais'.format(n1, n2))
    elif o == 4:
        n1 = float(input('Digite novamente dois valores: Valor 1 = '))
        n2 = float(input('\t\t\t\t\t\t\t   Valor 2 = '))
    elif o == 5:
        print('Programa encerrado.')
    else:
        print('Opção inválida. Tente novamente!')
    print('\n')


