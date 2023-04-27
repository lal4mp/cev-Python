"""
Escreva um programa em Python que leia um número inteiro qualquer.
Peça para o usuário escolher qual será a base de conversão:
    1 para binário, 2 para octal e 3 para hexadecimal
"""
from time import sleep

print('\033[35m='*10,'CONVERSOR', '='*10)

n = int(input('\033[mDigite um número inteiro: '))
print('\n\033[36mBases de conversão: 1 = para binário\n', '\t'*4, '   2 = para octal\n', '\t'*4, '   3 = para hexadecimal')
base = int(input('\033[mEscolha a base de conversão: '))

print('\033[34m\n...Convertendo...\n\033[m')
sleep(3)

if base == 1:
    print('O número {} em binário é {}' .format(n, bin(n)[2:]))
elif base == 2:
    print('O número {} em octal é {}'.format(n, oct(n)[2:]))
elif base == 3:
    print('O número {} em hexadecimal é {}'.format(n, hex(n)[2:]))
else:
    print('Opção inválida. Tente novamente!')