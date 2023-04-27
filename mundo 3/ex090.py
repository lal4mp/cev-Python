"""
Faça um programa que leia nome e média de um aluno.
Guarde em um dicionário, assim como a situação do aluno.
No final, mostre o conteúdo da estrutura na tela.
"""
aluno = dict()
aluno['Nome'] = str(input('Informe o nome do aluno: ')).capitalize()
aluno['Media'] = float(input(f'Informe a media do {aluno["Nome"]}: '))

if aluno['Media'] >= 5:
    aluno['Situacao'] = 'Aprovado'
elif aluno['Media'] <= 3:
    aluno['Situacao'] = 'Reprovado'
else:
    aluno['Situacao'] = 'Recuperacao'

print('\n\033[34mAluno(a)        Media           Situacao\033[m')
for x in aluno.values():
    print(f'{x:<16}', end='')


