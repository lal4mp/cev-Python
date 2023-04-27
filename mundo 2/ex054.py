"""
Crie um programa que leia o ano de nascimento de sete pessoas.
No final, mostre quantas pessoas ainda não atingiram a maioridade e
quantas já são maiores.
"""
import datetime

anoatual = datetime.date.today().year
count1 = 0
count2 = 0

print('Informe o ano em que cada pessoa nasceu.')
for x in range(0, 7):
    nasc = int(input('P{} : ' .format(x+1)))
    if anoatual - nasc < 18:
        count1 += 1
    else:
        count2 += 1

print('\n{} ainda são menores de idade' .format(count1))
print('{} já atingiram a maioridade' .format(count2))
