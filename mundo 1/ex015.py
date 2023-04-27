"""
Escreva um programa que receba a quantidade de km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado.
Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por km rodado.
"""
km = float(input('Informe a quantidade de quilometros percorridos pelo carro: '))
dias = int(input('Informe a quantidade de dias pelos quais o carro foi alugado: '))
p = (60*dias) + (0.15*km)
print('O preço a pagar pelo aluguel do carro é R${:.2f}' .format(p))