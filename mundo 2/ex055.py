"""
Faça um programa que leia o peso de cinco pessoas.
No final, mostre qual foi o maior e o menor peso lidos.
"""
print('Informe o peso de cada pessoa.')
menor = 0
maior = 0
for x in range(0, 5):
    peso = float(input('P{} : '.format(x + 1)))
    if x == 1:
        maior = peso
        menor = peso
    else:
        if peso < menor:
            menor = peso
        if peso > maior:
            maior = peso

print('\nO maior peso é {:.2f}kg'
      '\nO menor peso é {:.2f}kg' .format(maior, menor))