"""
Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado.
A multa vai custar R$7,00 por cada Km acima do limite.
"""
v = float(input('Informe a velocidade(km/h) do carro: '))
if v > 80:
    m = 7*(v-80)
    print('\n', ' '*10, '\033[31m MULTADO \nVocê excedeu o limite de velocidade(80km/h) \nMulta no valor de R${:.2f}' .format(m))
else:
    print('\n', ' '*14, '\033[32m OK \nVelocidade dentro do limite(80km/h) \nTenha um bom dia!' .format(v))