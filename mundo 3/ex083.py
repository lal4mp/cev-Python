"""
Crie um programa onde o usuário digite uma expressão qualquer que use parênteses.
Seu aplicativo deverá analisar se a expressão está com os parênteses abertos e fechados na ordem correta.
"""

exp = str(input('Digite uma expressão: '))
lista = list()

for x in exp:
    if x == '(':
        lista.append('(')
    elif x == ')':
        if len(lista) > 0:
            lista.pop()
        else:
            lista.append(')')
            break

if len(lista) == 0:
    print('Expressão válida')
else:
    print('Expressão inválida')


