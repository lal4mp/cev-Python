"""
Crie um programa onde o usuário possa digitar cinco valores numéricos.
Cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()).
No final, mostre a lista ordenada na tela.
"""
lista = list()
for x in range(0, 5):
    n = int(input(f'Digite o {x+1}° valor : '))
    if x == 0 or n > lista[len(lista)-1]:
        lista.append(n) # valor 'n' adicionado ao final da lista
    else:
        i = 0
        while i < len(lista):
            if n <= lista[i]:
                lista.insert(i, n) # valor 'n' adicionado na posição i da lista
                break
            i += 1
print(f'\nLista = {lista}')