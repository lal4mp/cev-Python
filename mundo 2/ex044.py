"""
Elabore um programa que calcule o valor a ser pago por um produto.
Considere o seu preço normal e condição de pagamento:
–à vista dinheiro/cheque: 10% de desconto
–à vista no cartão: 5% de desconto
–em até 2x no cartão: preço formal
–3x ou mais no cartão: 20% de juros
"""
valor = float(input('Qual o valor do produto? R$'))
print('Formas de pagamento: 1 - à vista no dinheiro/cheque'
      '\n\t\t\t\t\t 2 - à vista no cartão'
      '\n\t\t\t\t\t 3 - em até 2x no cartão'
      '\n\t\t\t\t\t 4 - 3x ou mais no cartão')
x = int(input('De qual forma você irá pagar? '))

if x == 1:
    p1 = 0.9*valor
    print('\nPagando à vista no dinheiro/cheque, você recebe 10% de desconto!'
          '\nO produto sai por R${:.2f}' .format(p1))
elif x == 2:
    p2 = 0.95*valor
    print('\nPagando à vista no cartão, você recebe 5% de desconto!'
          '\nO produto sai por R${:.2f}' .format(p2))
elif x == 3:
    print('\nPaganado em até 2x no cartão, '
          'o produto sai pelo preço normal R${:.2f}' .format(valor))
elif x == 4:
    p3 = 1.2*valor
    print('\nParcelando de 3x ou mais no cartão, há um juros de 20% sobre o valor do produto.'
          '\nO produto sai por R${:.2f}' .format(p3))
else:
    print('Opção inválida')