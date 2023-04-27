"""
Desenvolva um programa que leia seis números inteiros.
Mostre a soma apenas daqueles que forem pares.
Se o valor digitado for ímpar, desconsidere-o.
"""
soma = 0
print("Digite 6 números inteiros:")
for x in range(0, 6):
    n = int(input('N{}: ' .format(x+1)))
    if n % 2 == 0:
        soma += n
print('A soma dos números pares digitados é {}' .format(soma))