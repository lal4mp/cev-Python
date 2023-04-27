"""
Faça um programa que calcule a soma entre todos os números que:
são múltiplos de três e
se encontram no intervalo de 1 até 500.
"""
soma = 0
for x in range(1, 501, 2):
    if x % 3 == 0:
        soma += x
print('A soma é {}' .format(soma))
