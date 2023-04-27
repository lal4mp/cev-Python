"""
Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
Pergunte o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
A prestação mensal não pode exceder 30% do salário ou então o empréstimo será negado.
"""
from time import sleep

print('\033[35m-'*13, 'Análise de Empréstimo', '-'*13)
print('\033[30mInforme seus dados para a análise do empréstimo: ')
v = float(input('\033[30mQual o valor da casa? R$'))
s = float(input('\033[30mQual o seu salário? R$'))
a = int(input('\033[30mEm quantos anos você irá pagar? '))

print('\n', '\033[34m.'*13, 'Analisando', '.'*13)
sleep(3)

p = v/(a*12)
print('\033[mPara pagar uma casa de R${:.2f} em {} anos, a prestação mensal será de R${:.2f}' .format(v, a, p))
if p > 0.3*s:
    print('\033[1:31m\nEmpréstimo negado!!')
else:
    print('\033[1:32m\nEmpréstimo concedido!!')