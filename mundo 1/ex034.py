"""
Escreva um programa que pergunte o salário de um funcionário.
Calcule o valor do seu aumento.
Para salários superiores a R$1250,00, calcule um aumento de 10%.
Para os inferiores ou iguais, o aumento é de 15%.
"""
s = float(input('Qual o seu salário? '))
if s > 1250:
    ns = 1.1*s
else:
    ns = 1.15*s
#ns = 1.1*s if s > 1250 else 1.15*s
print('Seu novo salário e {:.2f}' .format(ns))