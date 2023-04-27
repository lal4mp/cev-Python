"""
Crie um programa que tenha uma tupla com várias palavras (não usar acentos).
Depois disso, você deve mostrar, para cada palavra, quais são as suas vogais.
"""
palavras = ('LIBERDADE', 'computador', 'ViagEm', 'JAva', 'PYThoN')

for word in palavras:
    count = 0
    print(f'A palavra \033[35m{word.capitalize()}\033[m possui as vogais: ', end='')
    for letra in word:
        if letra in 'AaEeIiOoUu':
            print(f'\033[35m{letra.upper()}\033[m', end=' ')
            count += 1
    print(f'- {count} vogal(is)')

