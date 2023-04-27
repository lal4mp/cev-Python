"""
Crie um programa que simule o funcionamento de um caixa eletrônico.
Pergunte ao usuário qual será o valor a ser sacado (número inteiro)
O programa vai informar quantas cédulas de cada valor serão entregues:
-cédulas de R$50, R$20, R$10 e R$1.
"""
count50 = count20 = count10 = count1 = 0

print('\t\tCAIXA ELETRÔNICO')

valor = int(input('Qual valor você deseja sacar? R$'))
print(f'\nValor do saque = R${valor}')

while valor >= 50:
    count50 += 1
    valor -= 50
while valor >= 20:
    count20 += 1
    valor -= 20
while valor >= 10:
    count10 += 1
    valor -= 10
while valor > 0:
    count1 += 1
    valor -= 1

print(f'{count50} nota(s) de R$50.00'
      f'\n{count20} nota(s) de R$20.00'
      f'\n{count10} nota(s) de R$10.00'
      f'\n{count1} nota(s) de R$1.00')

