"""
Crie um programa que leia duas notas de um aluno.
Calcule sua média e mostre uma mensagem no final, de acordo com a média atingida:
–Média abaixo de 5.0: REPROVADO
–Média entre 5.0 e 6.9: RECUPERAÇÃO
–Média 7.0 ou superior: APROVADO
"""
print('\033[1:34m\t  BOLETIM')
print('\033[mInforme suas notas:')
n1 = float(input('Nota 1 = '))
n2 = float(input('Nota 2 = '))
m = (n1+n2)/2

print('\033[30mMédia final = {:.2f}' .format(m))
if m < 5:
    print('\033[1:31m\t REPROVADO')
elif m >= 7:
    print('\033[1:32m\t  APROVADO')
else:
    print('\033[1:33m\tRECUPERAÇÃO')