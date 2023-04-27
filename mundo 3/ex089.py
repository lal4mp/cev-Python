"""
Crie um programa que leia nome e duas notas de vários alunos.
Guarde tudo em uma lista composta.
Mostre um boletim contendo a média de cada um.
Permita que o usuário possa mostrar as notas de cada aluno individualmente.
"""

alunos = list()
lista_aux = list()
count = 0

while True:
    lista_aux.append(str(input('Nome do aluno: ')).title())
    lista_aux.append(float(input('Nota 1: ')))
    lista_aux.append(float(input('Nota 2: ')))
    lista_aux.append((lista_aux[1]+lista_aux[2])/2)
    alunos.append(lista_aux[:])
    count += 1
    lista_aux.clear()

    r = str(input('Você deseja adicionar mais alunos? ')).lower()
    while r not in 'ns':
        print('Opção inválida. Digite apenas "s" ou "n".')
        r = str(input('Você deseja adicionar mais alunos? ')).lower()
    print()
    if r in 'n':
        break

print('-='*5, 'BOLETIM', '=-'*5)
print('N°      NOME            MÉDIA')
for x in range(0, count):
    print(f'{x:<8}{alunos[x][0]:<16}{alunos[x][3]}')

while True:
    n = int(input('\nVocê deseja ver as notas de qual aluno? (-1 para sair) '))
    if n not in range(0, count) and n != -1:
        print('Aluno não encontrado. Tente novamente.')
        n = int(input('\nVoce deseja ver as notas de qual aluno? (-1 para sair) '))
    if n == -1:
        break
    print(f'Aluno(a): {alunos[n][0]}\n'
          f'Nota 1 = {alunos[n][1]}\n'
          f'Nota 2 = {alunos[n][2]}\n'
          f'Média final = {alunos[n][3]}')


