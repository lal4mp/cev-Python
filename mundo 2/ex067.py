"""
Faça um programa que mostre a tabuada de vários números.
 O programa será interrompido quando o número solicitado for negativo.
"""
while True:
    n = int(input('\nVocê deseja ver a tabuada de qual número? '))
    if n < 0:
        break

    print('----- TABUADA DO {} -----' . format(n))
    for x in range(0, 11):
        print('{} x {} = {}' .format(n, x, n*x))

