"""
Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
Caso esteja errado, peça a digitação novamente até ter um valor correto.
"""
s = str(input('Informe seu sexo(M/F): ')).upper().strip()

while s not in 'MF':
    print('Opção inválida. Digite novamente.')
    s = str(input('Informe seu sexo(M/F): ')).upper().strip()

if s == 'M':
    print('\nSexo: Masculino')
else:
    print('\nSexo: Feminino')


