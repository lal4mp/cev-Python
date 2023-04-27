"""
Escreva um programa que receba uma temperatura em graus Celsius.
Converta-a para graus Fahrenheit.
"""
tc = float(input('Informe a temperatura (em Celsius): '))
tf = tc*1.8 + 32
print('A temperatura de {}°C é igual a {}°F' .format(tc, tf))