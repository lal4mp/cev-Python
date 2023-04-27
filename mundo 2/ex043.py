"""
Desenvolva uma lógica que leia o peso e a altura de uma pessoa.
Calcule seu Índice de Massa Corporal (IMC).
Mostre seu status, de acordo com a tabela abaixo:
–Abaixo de 18,5: Abaixo do Peso
–18,5 até 25: Peso Ideal
–25 até 30: Sobrepeso
–30 até 40: Obesidade
–Acima de 40: Obesidade Mórbida
"""
peso = float(input('Peso (em kg) = '))
alt = float(input('Altura (em metros) = '))
IMC = peso/(alt**2)

print('IMC = \033[1:30m{:.1f}\033[m' .format(IMC))
print('Status:\033[1:30m ', end='')
if IMC < 18.5:
    print('Abaixo do Peso')
elif 18.5 <= IMC < 25:
    print('Peso Ideal')
elif 25 <= IMC < 30:
    print('Sobrepeso')
elif 30 <= IMC < 40:
    print('Obesidade')
else:
    print('Obesidade Mórbida')