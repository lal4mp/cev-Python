"""
Desenvolva um programa que pergunte a distância de uma viagem em Km.
Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
"""
d = float(input('Qual a distancia da sua viagem? '))
p = d*0.5 if d <= 200 else 0.45*d
print('Sua passagem custa R${:.2f}'.format(p))